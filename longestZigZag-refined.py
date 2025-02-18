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
    def longestZigZag(self,root: Optional[TreeNode]) -> int:
        """
        Algo:
        - start at root
        - use a helper function to walk down the tree
            - function takes a node, the previous direction and current zig zag path length 
                - it moves opposite direction to previous direction and increments the current path length
                - if it can't move in opposite direction, it resets the current path length and moves in same direction

        """
        maxValidPathLength = 0
        
        if not root:
            return 0
        
        #helper function for traversing the tree
        def treeWalk(node:TreeNode, prevDirection:str, currentPathLength:int):
            
            if not node:
                print('\n none NODE')
                return
            print('examining', node.val, 'current path length is ', currentPathLength, 'prevDirection got ', prevDirection)
            nonlocal maxValidPathLength
            if prevDirection=='left':
                currentPathLength+=1
                print('we can go right and length is now', currentPathLength)
                treeWalk(node.right,'right',currentPathLength)
                #lets also traverse left node but reset the curentpath to 0
                treeWalk(node.left, 'left', 0)
           
            if prevDirection=='right':
                currentPathLength+=1
                print('we can go left and length is now', currentPathLength)
                treeWalk(node.left, 'left',currentPathLength)
                #lets also traverse right node but reset the curentpath to 0
                treeWalk(node.right, 'right', 0)
            # root case
            treeWalk(node.left,'left', 0)
            treeWalk(node.right, 'right',0)


            
            
            maxValidPathLength = max(currentPathLength, maxValidPathLength)
            print('stack POPPED , maxValidPathLength is now', maxValidPathLength)
            print('left node is ', node.left, 'right is ', node.right)

        
        treeWalk(root,' ', 0)
                
        #treeWalk(root.right, 'right',1)
        print(maxValidPathLength)

        
if __name__ == "__main__":
    root = [1,None,2,3,4,None,None,5,6,None,7,None,None,None,8]
    answer = Solution()
    answer.longestZigZag(list_to_tree(root))

         
