from copy import deepcopy
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
    ...

 
def step(grid: Grid) -> Grid:
    DELTAS =[(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    DELTAS1 =[(1,0),(1,-1),(0,-1)]
    DELTAS1_1 =[(-1,0),(-1,1),(0,1)]
    DELTAS1_2 =[(0,1),(1,1),(1,0)]
    DELTAS1_3 =[(0,-1),(-1,-1),(-1,0)]
    DELTAS2 =[(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    DELTAS2_1 =[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
    DELTAS3 =[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    DELTAS3_1 =[(-1,0),(-1,1),(0,1),(1,1),(1,0)]
    H = len(grid)
    W = len(grid[0])
    new_grid = deepcopy(grid)
    for i in range(H):
        for j in range(W):
            life_cell = 0
            if j == 1 and i == 1:
                for di, dj in DELTAS1:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1                
            elif i == H+1 and j == W+1:
                for di, dj in DELTAS1_1:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1
            elif j == 1 and i == H+1:
                for di, dj in DELTAS1_2:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1
            elif i == 1 and j == W+1:
                for di, dj in DELTAS1_3:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1
            elif i == 1 and not(j == 1 or j == W+1):
                for di, dj in DELTAS2:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1
            elif i == H+1 and not(j == 1 or j == W+1):
                for di, dj in DELTAS2_1:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1
            elif j == 1 and not(i == 1 or i == H+1):
                for di, dj in DELTAS3:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1
            elif j == W+1 and not(i == 1 or i == H+1):
                for di, dj in DELTAS3_1:
                    new_cell =  grid[i+di][j+dj]
                    if new_cell == 1:
                        life_cell+=1 
            else:
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