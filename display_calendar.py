import os
import re
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QScrollArea,
    QWidget,
)

MAX_WIDTH = 1600


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Advent of Code - Puzzle Calendar")
        self.setGeometry(100, 100, MAX_WIDTH, 800)  # Adjust size as needed

        scroll = QScrollArea()
        self.setCentralWidget(scroll)

        widget = QWidget()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)

        # Load images
        image_folder = "puzzle_visualisations"
        image_files = [
            os.path.join(image_folder, f)
            for f in os.listdir(image_folder)
            if f.endswith(".png")
        ]

        # Sort the files by the numeric prefix
        image_files.sort(
            key=lambda x: int(re.search(r"_(\d+)", x).group(1)),
        )

        # Create grid layout
        grid_layout = QGridLayout()
        widget.setLayout(grid_layout)

        # Maximum width for images
        max_width = int((MAX_WIDTH * 0.95) / 5)

        # Puzzle names
        puzzle_names = [
            "Day 1: Trebuchet?!",
            "Day 2: Cube Conundrum",
            "Day 3: Gear Ratios",
            "Day 4: Scratchcards",
            "Day 5: If You Give A Seed A Fertilizer",
            "Day 6: Wait For It",
            "Day 7: Camel Cards",
            "Day 8: Haunted Wasteland",
            "Day 9: Mirage Maintenance",
            "Day 10: Pipe Maze",
            "Day 11: Cosmic Expansion",
        ]

        # Extend the puzzle names list to 25 elements
        puzzle_names.extend(["???" for _ in range(25 - len(puzzle_names))])

        # Add labels and images to the grid
        for i in range(25):
            label_name = QLabel(puzzle_names[i])
            label_name.setAlignment(Qt.AlignCenter)
            grid_layout.addWidget(label_name, i // 5 * 2, i % 5)

            if i < len(image_files):
                pixmap = QPixmap(image_files[i])
                scaled_pixmap = pixmap.scaled(
                    max_width,
                    pixmap.height(),
                    Qt.KeepAspectRatio,
                )
                label_image = QLabel()
                label_image.setPixmap(scaled_pixmap)
            else:
                label_image = QLabel("")

            label_image.setAlignment(Qt.AlignCenter)
            grid_layout.addWidget(label_image, i // 5 * 2 + 1, i % 5)

        # Adjust widget size to grid layout
        widget.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
