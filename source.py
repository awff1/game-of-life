Grid = list[list[int]]
# [[1,2,3],
# [4,5,6],
# [7,8,9]]

def get_empty_grid(width: int, height: int) -> Grid:
    ...


def get_random_grid(width: int, height: int) -> Grid:
    ...

 
def step(grid: Grid, width: int, height: int) -> Grid:
    DELTAS =[(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    life_cell = 0
    for i in range(width+1):
        for j in range(height+1):
            for dj, di in DELTAS:
                new_cell = (i + di, j + dj)
                if new_cell == 1:
                    life_cell+=1
            if grid[i][j]:
                if 1 < life_cell < 4: 
                    grid[i][j] = 1
                    life_cell = 0
            else:
                if life_cell == 3: 
                    grid[i][j] = 1
                    life_cell = 0
                else:
                    grid[i][j] = 0
                    life_cell = 0