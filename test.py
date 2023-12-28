from itertools import product

def generate_trickle_combinations(lst):
    num_ones = lst.count(1)
    possibilities = [0, 1]
    
    # Generate all possible combinations of 0 and 1 for the same length as lst
    all_combinations = list(product(possibilities, repeat=len(lst)))
    
    # Filter combinations to ensure they have the same number of 1s as the original list
    valid_combinations = [comb for comb in all_combinations if comb.count(1) == num_ones]
    
    # Apply the trickle-down logic to valid combinations
    trickle_combinations = []
    for valid_comb in valid_combinations:
        result = []
        for i, val in enumerate(lst):
            if val == 1:
                result.append(1)
            else:
                result.append(valid_comb.pop(0))
        trickle_combinations.append(result)
    
    return trickle_combinations

input_list = [1, 0, 1, 0]
combinations = generate_trickle_combinations(input_list)
print(combinations)
