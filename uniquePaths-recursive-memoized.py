import time
from functools import lru_cache

class Solution: 
    def uniquePaths( m: int, n: int) -> int:
        """
        DAG shows that we can get to any cell (i,j) via cell to its left(i,j-1) or cell above it (i-1,j)
        so the total number of ways is the sum of the ways that lead to this left cell and the cell above
        ways(i,j) = ways(i-1,j) + ways(i,j-1)
        we can either do a recursive solution or a bottoms up dynamic programming one
        the recursive solution needs memoization in order to be feasible and complete in reasonable time.

        """
        memo = {} #dictionary for caching the results
            
        def ways(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            #base case 
            if i==0 and j==0:
                return 1
            cost = 0
            #we have to check if left cell exist
            if j-1>=0:
                cost += ways(i,j-1)
            # if there is cell above
            if i-1>=0:
                cost+= ways(i-1,j)
            memo[(i,j)]=cost
            return cost
        return ways(m-1,n-1)


start = time.time()
assert Solution.uniquePaths(2,4) == 4
end = time.time()
print (f'runtime in ms ', (end-start)*1000)