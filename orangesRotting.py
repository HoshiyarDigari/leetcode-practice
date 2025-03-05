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
        rottens = {(x,y) for x in range(grid_rows) for y in range(grid_columns) if grid[x][y]==2}
        fresh = {(x,y) for x in range(grid_rows) for y in range(grid_columns) if grid[x][y]==1}
        if not fresh:
            return 0 #there are no fresh oranges to rot
        
        #BFS queue will be a list of lists that start with current rotten cells
        queue = deque()
        queue.append([x for x in rottens])
        
        minutes = 0
        while queue and fresh:
            print('entering while, the queue is', queue, '\n fresh is ', fresh)
            current_rottens = queue.popleft()
            print('queue after pop', queue)
            print('current rottens are ', current_rottens)
            future_rottens=[] # this will hold the next batch of rotten oranges
            for rotten in current_rottens:
                #check the neighbors of this rotten orange
                neighbors = [(rotten[0]-1,rotten[1]), (rotten[0]+1,rotten[1]), (rotten[0],rotten[1]-1), (rotten[0],rotten[1]+1)]
                print(rotten, 'neighbors are', neighbors)
                for neighbor in neighbors:
                    if (
                0<=neighbor[0]<grid_rows and
                0<=neighbor[1]<grid_columns and
                neighbor in fresh):
                        print('neighbor rotted', neighbor)
                        future_rottens.append(neighbor)
                        
                        fresh.remove(neighbor)
            if future_rottens:
                queue.append(future_rottens)
            minutes+=1
            print('minutes now is ', minutes)
        if not fresh:
            return minutes
        else:
            return -1 # there are fresh oranges left after BFS processing
                        
                
        
if __name__ == "__main__":
    solution=Solution()

    #test 1
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    
    result =solution.orangesRotting(grid)
    assert result == 4

    #test2
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    assert solution.orangesRotting(grid) == -1


    #test 3
    grid =[[0,2]]
    assert solution.orangesRotting(grid) == 0
