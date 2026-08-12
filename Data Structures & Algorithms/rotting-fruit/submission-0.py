from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
                else:
                    continue
        if fresh == 0:
            return 0
        while q:
            size = len(q)
            for _ in range(size):
                x = q.popleft()
                for dr, dc in directions:
                    nr = x[0] + dr
                    nc = x[1] + dc
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            fresh -= 1
                        else:
                            continue
            minutes += 1
            if fresh == 0:
                break
        if fresh > 0:
            return -1
        else:
            return minutes