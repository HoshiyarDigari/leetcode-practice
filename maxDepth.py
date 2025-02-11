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

    # def __str__(self):
    #     left_str = str(self.left) if self.left else "None"
    #     right_str = str(self.right) if self.right else "None"
    #     return f"{left_str} <-- {self.val} --> {right_str}"


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        algo:
        - height of tree is 1 + max of left sub tree and right sub tree
        - this can go on recursively, till we get to the leafs
        
        """
        # if we are at a leaf, we return 0, this is the base case
        if not root:
            return 0
        
        height =  1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        print(root.val, height)
        return height

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
        if list[i]:
            node.right = TreeNode(list[i])
            queue.append(node.right)
        i+=1
    # print(root)
    return root 

    
        
if __name__ == "__main__":
    root = [1,None,2]
    answer = Solution()
    answer.maxDepth(list_to_tree(root))

         
