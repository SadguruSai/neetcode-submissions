class Solution:
    def dfs(self,grid,r,c):
        rows,cols=len(grid),len(grid[0])
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        if grid[r][c]!="1":
            return 
        grid[r][c]='0'
        self.dfs(grid,r+1,c)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r,c+1)
        self.dfs(grid,r,c-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        islands=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    self.dfs(grid,r,c)
                    islands+=1
        return islands
                