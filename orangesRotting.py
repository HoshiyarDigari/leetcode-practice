from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Algo:
        - this is also a BFS search but we have to start BFS not from a single cell but from all the cells with a rotten orange.
        - We mark all the neighbors of these as rotten in one iteration of the BFS
        - we will use queue of list of lists, where inner list will be all the rotten oranges for that particular iteration
        
        """
        # From the grid, find the sets of rotten and fresh orange cells
        if not grid:
            return 0 #there is nothing to do for empty grid
        grid_rows= len(grid)
        grid_columns = len(grid[0])
        #we store sets of fresh and rotten oranges
        rotten = {(x,y) for x in range(grid_rows) for y in range(grid_columns) if grid[x][y]==2}
        fresh = {(x,y) for x in range(grid_rows) for y in range(grid_columns) if grid[x][y]==1}

        #BFS queue will be a list of lists that start with current rotten cells
        queue = deque([rotten])
        print(queue)
        
        
if __name__ == "__main__":
    solution=Solution()

    #test 1
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    
    result =solution.orangesRotting(grid)
    assert result == 4

    #test2
