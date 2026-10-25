class Solution(object):
    def closedIsland(self, grid):
        """:type grid: List[List[int]] :rtype: int"""
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Out of bounds or water
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 1:
                return
            # Mark current land as visited by turning it into water (1)
            grid[r][c] = 1
            # Visit all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1: Eliminate all land cells connected to the top and bottom borders
        for c in range(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m - 1][c] == 0:
                dfs(m - 1, c)
                
        # Step 2: Eliminate all land cells connected to the left and right borders
        for r in range(m):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][n - 1] == 0:
                dfs(r, n - 1)
                
        # Step 3: Count remaining closed islands in the interior
        closed_islands_count = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    dfs(r, c) # Flood fill this entire closed island
                    
        return closed_islands_count