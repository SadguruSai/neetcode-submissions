class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        rows,cols=len(grid),len(grid[0])
        def dfs(i,j):
            if i>=rows or i<0 or j>=cols or j<0:
                return 0
            elif grid[i][j]==1:
                grid[i][j]=0
            else:
                return 0
            area = 1
            area+=dfs(i+1,j)
            area+=dfs(i-1,j)
            area+=dfs(i,j+1)
            area+=dfs(i,j-1)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    max_area=max(max_area,area)
        return max_area
                