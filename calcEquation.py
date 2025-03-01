class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        """
        Algo:
        1. represent equation and values as graph with values as edge weights.
        2. use a dict of dict a/b=2 is {a:{b:2}}, we also know that b/a=1/2 from this which is {b:{a:1/2}}
        3. To solve query[a, c] , we have to find path from a to c in this graph  and multiply the edge weights
        """
        # check if equations and values have same number of items , sanity check
        if len(equations) != len(values):
            print('value mismatch')
            return None
        # read data into the dictionary
        length = len(values)
        graph = {}
        for i in range(length):
            #add nodes to the dictionary
            if equations[i][0] not in graph:
                graph[equations[i][0]] = {equations[i][1]:values[i]}
            else:
                graph[equations[i][0]].update({equations[i][1]:values[i]})
            if equations[i][1] not in graph:
                graph[equations[i][1]] = {equations[i][0]:1/values[i]}
            else:
                graph[equations[i][1]].update({equations[i][0]:1/values[i]})
            

        print(graph)

if __name__ == '__main__':
    solution = Solution()
# test case 1
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = solution.calcEquation(equations, values, queries)
assert result == [6.00000,0.50000,-1.00000,1.00000,-1.00000]