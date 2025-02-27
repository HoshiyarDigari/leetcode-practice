from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
    #repr method for representing the node
    def __str__(self):
        result=''
        str_left = str(self.left) 
        str_right = str(self.right)
        result+='TreeNode{val:'+str(self.val) +',Left:'+str_left + ',Right:'+ str_right
        return result

    
    # equals function
    def __eq__(self,other):
        if not isinstance(other, TreeNode):
            return False # other object is not even the same type of object
        return id(self) == id(other) 
    # we have a hash function too 
    def __hash__(self):
        return hash(self.val, self.right, self.left)

def list_to_tree(lst):
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    i=1
    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None and i < len(lst):
            node.left = TreeNode(lst[i])
            queue.append(node.left)
            i+=1
        else:
            i+=1
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
                i+=1
            else:
                i+=1
    # print(root)
    return root 

    

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        """
        Algo:
        - consider that all edges are undirected
        - create adjacency matrix
        - Check for each key in adjacency matrix, starting from 0
            - reverse the direction of  the edge if it is going from 0 to that neighbor in the connections list
            - update connections list to show this new directed edge. Remove the older one
            - now we have all paths leading into 0. We add 0 to the visited list.
             
        
        """
        # adjacency matrix 
        adj_matrix = {x:[] for x in range(n)}
        for connection in connections:
            temp = connection[0]
            adj_matrix[connection[0]].append(connection[1])
            adj_matrix[connection[1]].append(temp)
        #print('the adjacency matrix is ',adj_matrix)
        # the adjacencies of 0 can directly reach it,we flip these in connections if any
        reversals = 0
        visited = set()
        # we will visit neighbors of 0, and then neighbors of 0's neighbors and so on , till we have visited all the nodes

        queue = deque([0])
        while queue:
            current_node = queue.popleft()
            visited.add(current_node)

            print('current node is ', current_node)
            for neighbor in adj_matrix[current_node]:
                print('examing the neighbor', neighbor)
                if neighbor not in visited:
                    print('it has not been visited yet', visited)
                    queue.append(neighbor)
                    step = [neighbor, current_node]
                    if step not in connections: # if step is not in connections, its reverse must be in connections thats why we have this edge in adj matrix.
                        connections.append(step)
                        connections.remove([step[1],step[0]])
                        reversals+=1
                        print('reversal done for step', step, reversals)
        print('total reversals done', reversals)



        
            
        
                    
        print(adj_matrix[0], 'reversals done', reversals)
        
        
if __name__ == "__main__":
    connections = [[4,0],[4,2],[3,2],[3,1]]
    n = 5
    answer = Solution()
    answer.minReorder(n,connections)

         
