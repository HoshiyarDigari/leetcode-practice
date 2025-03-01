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
        - we will create a adjacency list for all the nodes
        - we will start a DFS walk from 0 to all of its neighbors.
        - we will compare if the (node, neighbor) is in connection, if not we have a reversal
        - we try iterarive version first 
        """
        
        reversals = 0
        adjacency_list = {x:set() for x in range(n)}
        for edge in connections:
            adjacency_list[edge[0]].add(edge[1])
            adjacency_list[edge[1]].add(edge[0])
        
        # we note which all neighbors lead into the node
        incoming_neighbors = {x:set()for x in range(n)}
        for edge in connections:
            incoming_neighbors[edge[1]].add(edge[0])
        print(incoming_neighbors)
        
        # DFS walk
        stack = [0]
        visited = {0}
        while stack:
            current_node = stack.pop()
            for neighbor in adjacency_list[current_node]:
                print('looking at neighbor', neighbor, 'of', current_node, incoming_neighbors[current_node])
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    if neighbor not in incoming_neighbors[current_node]:
                        reversals+=1
        print(reversals)



        
            
        
                    
        
        
        
if __name__ == "__main__":
    connections = [[1,0],[1,2],[3,2],[3,4]]
    n = 5
    answer = Solution()
    answer.minReorder(n,connections)

         
