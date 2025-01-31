def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    algo:
    - create hash  list of rows and columns
    - compare the two to get the count of identical lists

    """
    n = len(grid)
    print('this is', n,'by', n, 'grid')
    columns={}
    for x in range(n):
        column_tuple = tuple([grid[i][x] for i in range(n)])
        columns[column_tuple]= columns.get(column_tuple, 0)+1
    
    print(columns)
    rows ={}
    for x in range(n):
        row_tuple = tuple([grid[x][i] for i in range(n)])
        rows[row_tuple]= rows.get(row_tuple, 0)+1
    
    print(rows)

    #compare to get count
    count = 0
    for key in rows.keys():
        if key in columns.keys():
            count+=max(rows[key], columns[key])
    print(count)
if __name__ == "__main__":
    grid = [[13,13],[13,13]]
    equalPairs(grid)