class Solution(object):
    def travel(self,i,j,grid,visit,row,col):
        if (i<0 or i>=row or j<0 or j>=col or grid[i][j]=='0' or visit[i][j]): return 

        visit[i][j]=True

        self.travel(i-1,j,grid,visit,row,col)
        self.travel(i+1,j,grid,visit,row,col)
        self.travel(i,j-1,grid,visit,row,col)
        self.travel(i,j+1,grid,visit,row,col)

    def numIslands(self, grid):
        if not grid: return 0

        row=len(grid)
        col=len(grid[0])

        visit=[[False for _ in range(col)] for _ in range(row)]
        ans=0

        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and not visit[i][j]:
                    self.travel(i,j,grid,visit,row,col)
                    ans+=1
    
        return ans
