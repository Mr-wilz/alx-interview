#!/usr/bin/python3
""" Island perimeter solution
"""


def island_perimeter(grid):
    """
    calculates the perimeter of and island in 2D grid
    :grid: Lists - 2D grid of 0s and 1s
    :return: perimeter of island
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
                    
    return perimeter
