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
        
        #helper function
        @staticmethod
        def findResult(start, goal, graph):
            nonlocal query_answers
            stack = [start]
            visited = {start}
            #print('visited set to ', visited , 'stack', stack)
            predecessors = {} # help construct the path from start to goal
            
            while stack:
                
                current_node = stack.pop()
                
                #print('current is', current_node, 'goal', goal, 'and the graph for it is ', graph[current_node], 'visited', visited)
                if current_node == goal:
                    break
                    pass # we need to generate the path now that we have found the goal node
                for neighbor in graph[current_node]:
                    print('looking at neighbor', neighbor, visited)
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
                        predecessors[neighbor] = current_node
            #trace the path using the predecessors dictionary
            else: # if we didn't find a path to the goal node
                query_answers.append(float(-1.0))
                print('added -1 as no path from', start, 'to', goal, 'predecessors', predecessors)
                return
            result = 1
            temp = goal
            while temp!=start:
                result*=graph[predecessors[temp]][temp]
                temp = predecessors[temp]
            query_answers.append(result)

                   
        query_answers = [] # list to hold the query answers
        #iterate through the queries and generate the answers
        for query in queries:
            # check if both the nodes exist in our graph
            if query[0] not in graph or query[1] not in graph:
                print('adding -1 as either of these is missing in graph', query[0], query[1])
                query_answers.append(float(-1.0))
            elif query[0]==query[1]:
                query_answers.append(float(1))
            elif query[1] in graph[query[0]]:
                query_answers.append(graph[query[0]][query[1]])
                
            else:
                # find path from query[0] to query[1]
                findResult(query[0], query[1],graph)
        return query_answers
                    
    

if __name__ == '__main__':
    solution = Solution()
# test case 1
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = solution.calcEquation(equations, values, queries)
assert result == [6.00000,0.50000,-1.00000,1.00000,-1.00000]

