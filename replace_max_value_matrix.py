import numpy as np
grid = np.random.randint(76, size=(5, 5))
print(grid)

#print(m[0][0])
tmp1=0
tmp2=0
max=grid[0][0]
for row_index, row in enumerate(grid):
    for col_index, item in enumerate(row):
        if item>max:
            max=grid[row_index][col_index]
            tmp1=row_index
            tmp2=col_index
        grid[tmp1][tmp2]=0
print(grid)
