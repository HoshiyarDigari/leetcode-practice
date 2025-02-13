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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pass



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
    root = [10,5,-3,3,2,None,11,3,-2,None,1]
    targetSum = 8
    answer = Solution()
    answer.pathSum(list_to_tree(root), targetSum)

         
