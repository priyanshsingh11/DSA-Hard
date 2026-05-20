from collections import deque 

class Solution(object):
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh = 0
        rotten = 0
        
        vis = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 2):
                    q.append(((i, j), 0))
                    vis[i][j] = True
                elif grid[i][j] == 1:
                    fresh += 1


        time = 0
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]
        
        while q:
            (r, c), t = q.popleft()
            time = max(time, t)

            for i in range (4):
                nrow = r + row[i]
                ncol = c + col[i]

                if(0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] != True and grid[nrow][ncol] == 1):
                    q.append(((nrow, ncol), t + 1))
                    vis[nrow][ncol] = True
                    rotten += 1

        if rotten != fresh: return -1
                
        return time 
        
