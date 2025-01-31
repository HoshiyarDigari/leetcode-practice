def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    algo:
    - first row is the column_heads
    - create a list of the first element of each list in the grid - call it row_heads
      - check if number in column_heads is in the row_heads?
       - yes? create list with this numbers index in each of the sublist.
       - compare if this matches a list in the grid. if yes counter increase by 1 
       - return counter
    """
    n = len(grid)
    print('this is', n,'by', n, 'grid')
    column_heads = grid[0]
    # create the row_heads
    row_heads = set([grid[x][0] for x in range(n)])
    print('row heads',row_heads, 'col heads', grid[0])

    count = 0
    for index, number in enumerate(column_heads):
        if number in row_heads:
            temp_tuple = tuple([grid[x][index] for x in range(n)])
            print(temp_tuple)
            for i in range(n):
                if temp_tuple == tuple(grid[i]):
                    count+=1
    print(count)
if __name__ == "__main__":
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    equalPairs(grid)