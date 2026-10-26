class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    # Found a new island, traverse it using BFS
                    island_sum = 0
                    queue = [(i, j)]
                    island_sum += grid[i][j]
                    grid[i][j] = 0  # Mark as visited
                    
                    head = 0
                    while head < len(queue):
                        r, c = queue[head]
                        head += 1
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                    
                    if island_sum % k == 0:
                        count += 1
                        
        return count