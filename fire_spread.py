import numpy as np

def simulate_fire(grid, wind_dir="E"):
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # burning cell
                directions = []

                if wind_dir == "E":
                    directions = [(0, 1), (1, 0)]
                elif wind_dir == "W":
                    directions = [(0, -1), (-1, 0)]
                elif wind_dir == "N":
                    directions = [(-1, 0), (0, 1)]
                elif wind_dir == "S":
                    directions = [(1, 0), (0, -1)]

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == 0:
                            new_grid[ni][nj] = 1

    return new_grid
