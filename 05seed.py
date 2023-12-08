import logging
from dataclasses import dataclass

import numpy as np
from tqdm import tqdm

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

EXAMPLE_ALAMANAC = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

EXAMPLE_CLOSEST_LOCATION_P1 = 35
EXAMPLE_CLOSEST_LOCATION_P2 = 46


@dataclass
class Mapping:
    source_start: int
    source_end: int
    offset: int | None = None


class Mapper:
    def __init__(self, almanac: str, naive=True):
        self.naive = naive
        self.seeds = []
        self.seed_to_soil = []
        self.soil_to_fertilizer = []
        self.fertilizer_to_water = []
        self.water_to_light = []
        self.light_to_temperature = []
        self.temperature_to_humidity = []
        self.humidity_to_location = []
        self.seed_to_location = {}

        self.almanac = self._prepare_almanac()
        self.category_pipeline = self._prepare_category_pipeline()

        self.transform_input(almanac)

    def transform_input(self, almanac: str):
        lines = almanac.splitlines()
        if self.naive:
            self.seeds = self.naive_seed_transform(lines.pop(0))
        else:
            self.seeds = self.range_seed_transform(lines.pop(0))

        current_category_mapping = None
        for line in lines:
            if not line:
                continue

            if "map" in line:
                mapping, _ = line.split()
                current_category_mapping = self.almanac.get(mapping)
                continue

            current_category_mapping.append(self.range_category_transform(line))

    def naive_seed_transform(self, line: str) -> list[str]:
        return line.split(":")[1].split()

    def range_seed_transform(self, line: str) -> list[Mapping]:
        seed_ranges = self.naive_seed_transform(line)
        range_seed_mappings = []
        if len(seed_ranges) % 2 == 1:
            raise ValueError("The seed ranges should be even!")
        for i in range(0, len(seed_ranges) // 2 + 1, 2):
            seed_mapping = Mapping(
                source_start=int(seed_ranges[i]),
                source_end=int(seed_ranges[i]) + int(seed_ranges[i + 1]),
                offset=None,
            )
            range_seed_mappings.append(seed_mapping)
        return range_seed_mappings

    def range_category_transform(self, line: str) -> Mapping:
        target_start, source_start, range_length = line.split()
        target_start, source_start, range_length = (
            int(target_start),
            int(source_start),
            int(range_length),
        )
        return Mapping(
            source_start=source_start,
            source_end=source_start + range_length,
            offset=target_start - source_start,
        )

    def naive_find_range_closest_location(self):
        available_ranges = []
        previous_range, current_range = [], []

        # Here is the seed that is Mapping(start, end, None)
        for seed in tqdm(self.seeds, desc="Transforming seeds..."):
            # Here is previous_range, which we want to test
            # and its result transformation will be stored in current_range, which is currently empty
            # types: list[Mapping], list[Mapping]
            previous_range, current_range = [seed], []

            # Since there are multiple categories runs we want to run it actually in this particular loop
            # to go over each category
            for category_mapping in self.category_pipeline:
                # Now we loop over range we want to test
                for prev in previous_range:
                    # Here we loop over all the mappings that category has
                    for current_category_mapping in category_mapping:
                        # And we want to transform the ranges according to it's overlap and offset!
                        new_ranges = self.overlapping_ranges(
                            prev,
                            current_category_mapping,
                        )

                        # Here is a problem with values overstaying. The issue is that there are 2 mappings:
                        # One that doesnt change the range, and the other that fully changes it,
                        # Like 5,9 and 3,10,100 and 5,9 and 10,12,200
                        current_range.extend(new_ranges)

                # here we fix multiple ranges
                current_range.sort(
                    key=lambda r: (r.offset is None, r.source_start, r.source_end),
                )

                actual_range_used = []
                final_ranges = []
                for r in tqdm(current_range, desc="Removing redundant ranges"):
                    current_actual_range_used = len(actual_range_used)
                    if current_actual_range_used > 1000000:
                        crop = 100
                        to_be_checked = actual_range_used[-crop:]
                    elif current_actual_range_used > 100000:
                        crop = int(current_actual_range_used * 0.005)
                        to_be_checked = actual_range_used[-crop:]
                    elif current_actual_range_used > 10000:
                        crop = int(current_actual_range_used * 0.01)
                        to_be_checked = actual_range_used[-crop:]
                    elif current_actual_range_used > 100:
                        crop = int(current_actual_range_used * 0.1)
                        to_be_checked = actual_range_used[-crop:]
                    else:
                        to_be_checked = actual_range_used

                    if r.offset is not None:
                        if (
                            r.source_start - r.offset,
                            r.source_end - r.offset,
                        ) in to_be_checked:
                            continue

                        actual_range_used.append(
                            (r.source_start - r.offset, r.source_end - r.offset),
                        )
                        final_ranges.append(r)
                    else:
                        if (r.source_start, r.source_end) in to_be_checked:
                            continue
                        actual_range_used.append([r.source_start, r.source_end])
                        final_ranges.append(r)
                logging.warn(
                    f"Removed ranges percentage: {(len(current_range) - len(final_ranges)) / len(current_range)} %",
                )

                logging.debug(f"Ranges that shouldn't be overlapping: {final_ranges}")
                previous_range, current_range = final_ranges, []
            available_ranges.extend(previous_range)
        logging.debug(f"Here is the available ranges: {available_ranges}")
        return min(available_ranges, key=lambda r: r.source_start).source_start + 1

    def overlapping_ranges(self, range_1: Mapping, range_2: Mapping):
        # TODO: FIX THIS ERROR
        range_1_start, range_1_end, curr_offset = (
            range_1.source_start,
            range_1.source_end,
            range_1.offset,
        )
        range_2_start, range_2_end, offset = (
            range_2.source_start,
            range_2.source_end,
            range_2.offset,
        )

        # 1) 2-5 and 6-9 + 6-9 and 2-5
        if range_1_end < range_2_start or range_1_start > range_2_end:
            return [range_1]

        # 2) 1-9 and 2-5
        if range_1_start <= range_2_start and range_1_end >= range_2_end:
            return [
                Mapping(range_1_start, range_2_start, curr_offset),
                Mapping(
                    range_2_start + offset,
                    range_2_end + offset,
                    offset + (curr_offset or 0),
                ),
                Mapping(range_2_end, range_1_end, curr_offset),
            ]

        # 3) 2-5 and 4-6
        if range_1_start <= range_2_start and range_1_end <= range_2_end:
            return [
                Mapping(range_1_start, range_2_start, curr_offset),
                Mapping(
                    range_2_start + offset,
                    range_1_end + offset,
                    offset + (curr_offset or 0),
                ),
            ]

        # 4) 4-6 and 2-5
        if range_1_start >= range_2_start and range_1_end >= range_2_end:
            return [
                Mapping(
                    range_1_start + offset,
                    range_2_end + offset,
                    offset + (curr_offset or 0),
                ),
                Mapping(range_2_end, range_1_end, curr_offset),
            ]

        # 5) 79-93 and 50-98
        if range_1_start >= range_2_start and range_1_end <= range_2_end:
            return [
                Mapping(
                    range_1_start + offset,
                    range_1_end + offset,
                    offset + (curr_offset or 0),
                ),
            ]

        raise ValueError("There is uncaught case")

    def naive_find_lowest_seeds_location(self):
        if self.naive:
            seed_iterator = self.seeds
        else:
            seed_iterator: list[int] = []
            for s in tqdm(self.seeds, desc="Unrolling seeds"):
                ss, se = s.source_start, s.source_end
                seed_range = tqdm(
                    list(range(ss, se)),
                    f"Unrolling seed range ({ss}, {se})",
                )
                for seed in seed_range:
                    seed_iterator.append(int(seed))

        for seed in tqdm(seed_iterator):
            current_category = int(seed)
            # list[list[Mapping]]
            for category_mapping in self.category_pipeline:
                # list[Mapping]
                for current_category_mapping in category_mapping:
                    # Mapping
                    if (
                        current_category_mapping.source_start
                        <= current_category
                        <= current_category_mapping.source_end
                    ):
                        current_category += current_category_mapping.offset
                        break

                logging.debug(f"Current category value: {current_category}")

            logging.debug(
                f"Finished going through categories for seed: {seed} got {current_category}",
            )
            self.seed_to_location[seed] = current_category
        return min(self.seed_to_location.values())

    def numpy_naive_find_lowest_seeds_location(self):
        if self.naive:
            seed_iterator = np.array(self.seeds)
        else:
            seed_ranges = [
                np.arange(s.source_start, s.source_end + 1)
                for s in tqdm(self.seeds, desc="Unrolling seeds")
            ]
            seed_iterator = np.concatenate(seed_ranges)

        pipeline = self._retrieve_pipeline_numpy_array()

        for stage in tqdm(pipeline, desc="Going through pipelines"):
            transformed_this_stage = np.zeros_like(
                seed_iterator,
                dtype=bool,
            )  # Initialize a mask to track transformations in this stage
            for start, end, offset in tqdm(
                zip(stage["start"], stage["end"], stage["offset"], strict=True),
                desc="Going through transformations",
                total=len(stage),
            ):
                # Identify seeds that fall within the current range
                mask = (
                    (seed_iterator >= start) & (seed_iterator <= end)
                ) & ~transformed_this_stage

                # Apply the offset to all seeds in the range
                seed_iterator[mask] += offset

                # Update the mask to indicate these seeds have been transformed
                transformed_this_stage = transformed_this_stage | mask

        logging.info("Finishing work...")
        return np.min(seed_iterator)

    def _retrieve_pipeline_numpy_array(self):
        pipeline_array = np.empty(len(self.category_pipeline), dtype=object)

        for i, category_mapping in enumerate(self.category_pipeline):
            # For each stage, create a structured NumPy array
            stage_array = np.array(
                [
                    (m.source_start, m.source_end, m.offset or 0)
                    for m in category_mapping
                ],
                dtype=[("start", int), ("end", int), ("offset", int)],
            )
            pipeline_array[i] = stage_array
        return pipeline_array

    def _prepare_almanac(self) -> dict[str, list[Mapping]]:
        almanac = {}
        almanac["seed-to-soil"] = self.seed_to_soil
        almanac["soil-to-fertilizer"] = self.soil_to_fertilizer
        almanac["fertilizer-to-water"] = self.fertilizer_to_water
        almanac["water-to-light"] = self.water_to_light
        almanac["light-to-temperature"] = self.light_to_temperature
        almanac["temperature-to-humidity"] = self.temperature_to_humidity
        almanac["humidity-to-location"] = self.humidity_to_location
        return almanac

    def _prepare_category_pipeline(self) -> list[list[Mapping]]:
        return [
            self.seed_to_soil,
            self.soil_to_fertilizer,
            self.fertilizer_to_water,
            self.water_to_light,
            self.light_to_temperature,
            self.temperature_to_humidity,
            self.humidity_to_location,
        ]


def test_overlap():
    # 1)
    x, y = Mapping(2, 5), Mapping(6, 9, 100)
    overlaps = Mapper.overlapping_ranges(None, x, y)
    assert overlaps == [Mapping(2, 5)], f"Found overlap: {overlaps}"
    x, y = Mapping(6, 9), Mapping(2, 5, 100)
    overlaps = Mapper.overlapping_ranges(None, x, y)
    assert overlaps == [Mapping(6, 9)], f"Found overlap: {overlaps}"

    # 2)
    x, y = Mapping(1, 9), Mapping(2, 5, 100)
    overlaps = Mapper.overlapping_ranges(None, x, y)
    assert overlaps == [
        Mapping(1, 2),
        Mapping(102, 105, 100),
        Mapping(5, 9),
    ], f"Found overlap: {overlaps}"

    # 3)
    x, y = Mapping(2, 5), Mapping(4, 6, 100)
    overlaps = Mapper.overlapping_ranges(None, x, y)
    assert overlaps == [
        Mapping(2, 4),
        Mapping(104, 105, 100),
    ], f"Found overlap: {overlaps}"

    # 4)
    x, y = Mapping(4, 6), Mapping(2, 5, 100)
    overlaps = Mapper.overlapping_ranges(None, x, y)
    assert overlaps == [
        Mapping(104, 105, 100),
        Mapping(5, 6),
    ], f"Found overlap: {overlaps}"

    # 5)
    x, y = Mapping(79, 93), Mapping(50, 98, 100)
    overlaps = Mapper.overlapping_ranges(None, x, y)
    assert overlaps == [Mapping(179, 193, 100)]


if __name__ == "__main__":
    test_overlap()

    # mapper = Mapper(EXAMPLE_ALAMANAC)
    # closest_location = mapper.naive_find_lowest_seeds_location()
    # assert closest_location == EXAMPLE_CLOSEST_LOCATION_P1, \
    #     f"The closest location provided is not {EXAMPLE_CLOSEST_LOCATION_P1}, but {closest_location}. Mapping: {mapper.seed_to_location}"
    mapper = Mapper(EXAMPLE_ALAMANAC, naive=False)
    closest_location = mapper.numpy_naive_find_lowest_seeds_location()
    assert (
        closest_location == EXAMPLE_CLOSEST_LOCATION_P2
    ), f"The closest location provided is not {EXAMPLE_CLOSEST_LOCATION_P2}, but {closest_location}."
    # print(f"Closest location is {real_closes_location}")

    # HELP ME GOD
    # real_mapper = Mapper(REAL_ALMANAC, naive=False)
    # closest_location = real_mapper.numpy_naive_find_lowest_seeds_location()
    # logging.info(f"Closest location is: {closest_location}")
