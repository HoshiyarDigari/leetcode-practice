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


def list_to_tree(list):
    if not list:
        return None
    
    root = TreeNode(list[0])
    queue = deque([root])
    i=1
    while queue and i < len(list):
        node = queue.popleft()
        if list[i]:
            node.left = TreeNode(list[i])
            queue.append(node.left)
        i+=1
        if i < len(list):
            if list[i] and i < len(list):
                node.right = TreeNode(list[i])
                queue.append(node.right)
            i+=1
    # print(root)
    return root 

    

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Algo:
        - prefix sum of a node  - sum of values from  root to that node
        - we keep this prefix sum in a dictionary.
        - when we go down the tree, we update prefix sum of the child to dictionary
        - a valid path to a node must satisfy:
            - current sum = target sum
            - current sum - targetSum = some previous prefix sum
        - when we backtrack , which is after the node.left and node.right calls, we remove current prefix sum from the dictionary. This way it doesn't impact any other branches
        """
        
if __name__ == "__main__":
    root = [0,1,0]
    targetSum = 1
    answer = Solution()
    answer.longestZigZag(list_to_tree(root), targetSum)

         
