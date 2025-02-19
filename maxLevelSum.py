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
    def maxLevelSum(self,root: Optional[TreeNode]) -> int:
        """
        Goal:
        Find the level with nodes that have the max sum among all levels
        Algo:
        we just keep count of levels and add the nodes at each level
        we just solved the rightsideview problem keeping track of each level nodes
        """
        # if no level, we return 0
        if not root:
            return 0
        
        maxLevelSum = float('-inf')
        levels_with_maxSum = 0
        queue = deque([root])
        level = 1
        while queue:
            level_size = len(queue)
            levelSum = 0
            print('\n we are at level', level)
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    levelSum+=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if levelSum > maxLevelSum:
                print('found greater sum at level', level, 'before it was ', maxLevelSum, 'it is now', levelSum)
                maxLevelSum = levelSum
                levels_with_maxSum = level

            
            level+=1
            
        print(levels_with_maxSum)        
        
        
        
if __name__ == "__main__":
    root = [-100,-200,-300,-20,-5,-10,None]
    answer = Solution()
    answer.maxLevelSum(list_to_tree(root))

         
