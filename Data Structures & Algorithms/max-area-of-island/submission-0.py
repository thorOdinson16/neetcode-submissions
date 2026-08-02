class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        largest = 0
        def dfs(row: int, col: int) -> int:
            size = 0
            if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0]) - 1:
                return 0
            elif (row, col) in visited:
                return 0
            elif grid[row][col] == 0:
                return 0
            elif grid[row][col] == 1:
                visited.add((row,col))
                size += 1
                a = dfs(row-1,col)
                b = dfs(row+1,col)
                c = dfs(row,col-1)
                d = dfs(row,col+1)
                size = size + a + b + c + d
                return size
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in visited:
                    continue
                else:
                    if grid[i][j] != 0:
                        x = dfs(i,j)
                        if x > largest:
                            largest = x
        return largest