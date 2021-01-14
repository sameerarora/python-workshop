def find(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                markall(grid, i, j)
    return count


def markall(grid, x, y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return
    if grid[x][y] == 1:
        grid[x][y] = 0
        markall(grid, x + 1, y)
        markall(grid, x - 1, y)
        markall(grid, x, y - 1)
        markall(grid, x, y + 1)


print(find([[1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]))
