from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    flag = True
    time = 0
    m, n = len(grid), len(grid[0])
    while flag:
        flag = False
        time += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        grid[i - 1][j] = 3
                        flag = True
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        grid[i][j - 1] = 3
                        flag = True
                    if j + 1 < n and grid[i][j + 1] == 1:
                        grid[i][j + 1] = 3
                        flag = True
                    if i + 1 < m and grid[i + 1][j] == 1:
                        grid[i + 1][j] = 3
                        flag = True

        for i2 in range(m):
            for j2 in range(n):
                if grid[i2][j2] == 3:
                    grid[i2][j2] = 2

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1

    return time - 1


orangesRotting([[2,1,1],[1,1,0],[0,1,1]])