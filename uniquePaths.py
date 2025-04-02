class Solution:
    def uniquePaths(m: int, n: int) -> int:
        """
        DAG shows that we can get to any cell (i,j) via cell to its left(i,j-1) or cell above it (i-1,j)
        so the total number of ways is the sum of the ways that lead to this left cell and the cell above
        ways(i,j) = ways(i-1,j) + ways(i,j-1)
        we will do the DP in this, we will create a list that will store the number of ways to each cell in a grid[i][j]
        """
        # We will use this 2D list to store the paths to each cell, it will be None if we haven't calculated it yet
        grid = [[None for _ in range(n)]for _ in range(m)]
        print(grid)
        # intialize grid
        # the top row cells have only one path and so does first column
        
        for i in range(m):
            for j in range(n):
                if i==0 or j == 0:
                    grid[i][j]=1
                else:
                    grid[i][j]=grid[i-1][j] + grid[i][j-1]
                
        print(grid[m-1][n-1])
        return grid[m-1][n-1]
        



assert Solution.uniquePaths(2,3) == 3