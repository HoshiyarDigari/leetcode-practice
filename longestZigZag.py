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
        
        if lst[i] is not None and i < len(lst):
            node.right = TreeNode(lst[i])
            queue.append(node.right)
            i+=1
        else:
            i+=1
    # print(root)
    return root 

    

class Solution:
    def longestZigZag(self,root: Optional[TreeNode]) -> int:
        """
        Algo:
        - this task is similar to finding the prefix sum
        - we can walk down the tree with each of the nodes as root and find the longest path seen across the walks.
        - to optimize, we need a way to reduce the number of walks or get the answer in one walk if possible 
        """
        path = list()
        if not root:
            return 0
        #helper function for traversing the tree
        def treeWalk(node:TreeNode):
            print(node)
            if not node:
                return
            
            treeWalk(node.left)
            treeWalk(node.right)
            
        treeWalk(root)

        
if __name__ == "__main__":
    root = [0,2,0]
    targetSum = 1
    answer = Solution()
    answer.longestZigZag(list_to_tree(root))

         
