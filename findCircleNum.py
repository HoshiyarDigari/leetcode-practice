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
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        Goal:
        this is an application of the union find algorithm.
        We have to find all the disjoint sets of connections.
        Algo:
        - we keep a parent list, that tracks the parent of each of the nodes.
        - all nodes have same weightage, so when we find two nodes are connected, we can make any one as the parent.
        - after we have found parent of each node, we look at all the parents to get our sets. 

        """
        n = len(isConnected)
        parent = [x for x in range(n)] # start with each node as its own parent
        print('input is ', n , 'long and parent list is ', parent)
        rank = [0]*n # start with 0 ranking for each 

        def find(node):
            if parent[node] == node: #base case
                return node
            parent[node] = find(parent[node]) # find the ultimate parent recursively and update 
            return parent[node]
        

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2 : #both are in same set so nothting to do
                return 
            if rank[root1]<rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1]+=1 


        
        # process the input matrix
        for i in range(n):
            for j in range(i+1,n):
                
                if isConnected[i][j] == 1:
                    print(i,j , 'connected')
                    union(i,j)
                    print(parent, 'updated')

                    
                
        #check the parents list to find how many unique parents we have now
        numberProvinces = len(set(find(x) for x in range(n)))
        print(numberProvinces)
            


                
        
        
        
if __name__ == "__main__":
    isConnected = [
    [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
    [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]

    key = 7
    answer = Solution()
    answer.findCircleNum(isConnected)

         
