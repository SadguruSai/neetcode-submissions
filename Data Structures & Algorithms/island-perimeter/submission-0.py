class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        hash=set()
        def dfs(r,c):
            if(r<0 or r>=len(grid) or c<0 or c>=len(grid[0])):
                return 1
            if((r,c) in hash):
                return 0
            if(grid[r][c]==0):
                return 1
            if((r,c) not in hash and grid[r][c]==1):
                hash.add((r,c))
                return dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    return dfs(r,c)
        return 0