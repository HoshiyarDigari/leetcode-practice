class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        pass


if __name__ == '__main__':
    solution = Solution()
# test case 1
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = solution.calcEquation(equations, values, queries)
assert result == [6.00000,0.50000,-1.00000,1.00000,-1.00000]