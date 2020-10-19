class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.result = 0
        self.m, self.n = len(grid), len(grid[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    start = [i, j]
                    
                if grid[i][j] == 2:
                    end = [i, j]
                    
        vis = [[False for i in range(self.n)] for j in range(self.m)]
        
        self.backtrack(grid, start, end, vis)
        
        return self.result
    
    def validateSuccess(self, grid, vis):
        for i in range(self.m):
            for j in range(self.n):
                if vis[i][j] == False and grid[i][j] != -1:
                    return False
                
        return True
    
    def isValid(self, grid, idxs, vis):
        if 0 <= idxs[0] < self.m and 0 <= idxs[1] < self.n and grid[idxs[0]][idxs[1]] != -1 and vis[idxs[0]][idxs[1]] != True:
            return True
        
        return False
                
    
    def backtrack(self, grid, start, end, vis):
        
        if not self.isValid(grid, start, vis):
            return
        
        i, j = start
        
        if start == end:
            vis[i][j] = True

            if self.validateSuccess(grid, vis):
                self.result += 1
                
            vis[i][j] = False
            return        
        
        vis[i][j] = True
        
        self.backtrack(grid, [start[0]-1, start[1]], end, vis)
        
        self.backtrack(grid, [start[0]+1, start[1]], end, vis)

        self.backtrack(grid, [start[0], start[1]-1], end, vis)

        self.backtrack(grid, [start[0], start[1]+1], end, vis)
        
        vis[i][j] = False
