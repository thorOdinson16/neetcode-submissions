class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        def dfs(row: int, col: int) -> None:
            if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0]) - 1:
                return None
            elif (row, col) in visited:
                return None
            elif grid[row][col] == "0":
                return None
            elif grid[row][col] == "1":
                visited.add((row,col))
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in visited:
                    continue
                else:
                    dfs(i,j)
                    if grid[i][j] == "1":
                        islands+=1
        return islands