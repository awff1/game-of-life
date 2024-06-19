from copy import deepcopy
from random import randint

Grid = list[list[int]]
# [[1,2,3],
# [4,5,6],
# [7,8,9]]


def get_empty_grid(width: int, height: int) -> Grid:
    empty_grid = []
    for i in range(height):
        a = []
        for j in range(width):
            a.append(0)
        empty_grid.append(a)
    return empty_grid


def get_random_grid(width: int, height: int) -> Grid:
    random_grid = []
    for i in range(height):
        a = []
        for j in range(width):
            a.append(randint(0, 1))
        random_grid.append(a)
    return random_grid


def step(grid: Grid) -> Grid:
    DELTAS = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
    H = len(grid)
    W = len(grid[0])
    new_grid = deepcopy(grid)
    for i in range(H):
        for j in range(W):
            life_cell = 0
            for di, dj in DELTAS:
                if (0 <= i + di < H) and (0 <= j + dj < W):
                    new_cell = grid[i + di][j + dj]
                    if new_cell == 1:
                        life_cell += 1
            print(i, j, life_cell)
            if grid[i][j]:
                if 1 < life_cell < 4:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if life_cell == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
    return new_grid
