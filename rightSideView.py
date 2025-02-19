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
    def rightSideView(self,root: Optional[TreeNode]) -> int:
        """
        Goal:
        Find all the nodes at the right end of each level in the binary tree
        Algo:
        - make a list of nodes at each level from left to right.
        - we have to return the last node of each level queue
        
        """
        #lets implement basic BFS to start
        queue = deque([root])
        level = 0
        rightView = []
        while queue:
            level_size = len(queue) # as we come into the while , we should process all items added in previous whiles
            print('there are ', level_size, 'nodes at level', level)
            for i in range(level_size):
                node = queue.popleft()
                if i+1 == level_size:
                    rightView.append(node.val)
                if node:
                    print('\n ', node.val, 'level', level)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level+=1 
        
        print(rightView)
            

        
        
if __name__ == "__main__":
    root = [1,2,3,None,5,None,4]
    answer = Solution()
    answer.rightSideView(list_to_tree(root))

         
