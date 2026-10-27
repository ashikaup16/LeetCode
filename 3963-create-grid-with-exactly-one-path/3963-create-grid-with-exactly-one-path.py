class Solution(object):
    def createGrid(self, m, n):
        """:type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # Open the first row
        for j in range(n):
            grid[0][j] = '.'
            
        # Open the last column
        for i in range(m):
            grid[i][n - 1] = '.'
            
        return ["".join(row) for row in grid]