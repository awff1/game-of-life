from copy import deepcopy
Grid = list[list[int]]
# [[1,2,3],
# [4,5,6],
# [7,8,9]]

def get_empty_grid(width: int, height: int) -> Grid:
    ...


def get_random_grid(width: int, height: int) -> Grid:
    ...

 
def step(grid: Grid) -> Grid:
    DELTAS =[(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    H = len(grid)
    W = len(grid[0])
    new_grid = deepcopy(grid)
    for i in range(H):
        for j in range(W):
            life_cell = 0
            for di, dj in DELTAS:
                new_cell =  grid[i+di][j+dj]
                if new_cell == 1:
                    life_cell+=1
            if grid[i][j]:
                if 1 < life_cell < 4: 
                    new_grid[i][j] = 1
            else:
                if life_cell == 3: 
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
    return new_grid
