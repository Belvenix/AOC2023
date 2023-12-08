# Advent of Code 2023

## Project Overview

Welcome to my Advent of Code 2023 repository! Here, I've taken on the challenge of solving the Advent of Code puzzles using Python, focusing primarily on enhancing my programming skills. My approach leans towards using Python's built-in methods and libraries, but I'm open to leveraging additional libraries for optimization or complex calculations.


## Goals and Philosophy

* Efficiency: Aim to solve puzzles in a reasonable timeframe (ideally a few hours).
* Simplicity: Start with brute force or simple solutions, and optimize only when necessary. This approach mirrors real-world problem-solving in a business context.


## Repository Structure

```
AOC2023/
│
├── 01_solution.py
├── 02_solution.py
├── 03_solution.py
├── ...
├── 25_solution.py
│
├── puzzle_visualisations/
│   ├── day_01_visualisation.jpg
│   ├── day_02_visualisation.jpg
│   ├── ...
│   └── day_25_visualisation.jpg
│
├── data/
│   ├── example/
│   │   ├── 01/
│   │   ├── 02/
│   │   ├── ...
│   │   └── 25/
│   └── puzzle_input/  # To be added
│
└── display_calendar.py  # Advent calendar visualization using PyQt5
```


## Coding Standards

### Linting and Formatting
In this project, we are committed to maintaining a high standard of code quality. To achieve this, we use ruff and black for linting and formatting our code.

* **ruff**: A fast and highly configurable Python linter that helps us identify and fix various coding issues, ensuring code adheres to the best practices and coding conventions.

* **black**: Known as "The Uncompromising Code Formatter". Black takes care of code formatting so that we can focus on solving puzzles instead of worrying about stylistic nuances.

### Usage

In order to run these linters over the code, after the libraries are installed please run the following command.

```sh
black .   # Formats code in the root directory
ruff check . --fix  # Lints and auto-fixes issues
```


## Dependencies
* tqdm: For progress bars in scripts.
* numpy: For numerical operations.
* PyQt5: For GUI elements and visualizations.
* ruff: For linting.
* black: For code formatting.


## Visualisation

display_calendar.py: A mockup Advent calendar visualisation using PyQt5. In order to run it simply use this command.

```sh
python display_calendar.py
```


## NOTICE

Image Credits: Visual representations of puzzles created using DALL·E, provided by OpenAI.
