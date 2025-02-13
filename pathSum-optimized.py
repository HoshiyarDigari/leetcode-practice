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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Algo:
        - at the root, we find the remaining =(target - root).
        - we walk down the tree from the root
        - update the remaining to remaining - current node
            - if remaining is 0, we have found a pathSum that equals target. Update count for it
            - else continue the walk down the tree
        - when whole tree has been traversed, change root of tree to the roots left and right children


        """
        if not root:
            return 0
     
        count = 0 
        
        #helper function to walk down the tree
        def treeWalk (node, remaining):
            nonlocal count  # Allow modification of outer `count`
            # we have nothing to do if we at a None node
            print('got the node in as ', node)
            if not node:
                print('None node exiting')
                return 0
            remaining = remaining - node.val
            
            print('\nroot for current search is', node.val, 'remaining is', remaining)
            
            if remaining == 0:
                print('found a pathSum at ', node.val)
                count+=1
                #return None
            
            
            print('calling left and right child of node', node.val)
            treeWalk(node.left, remaining)
            treeWalk(node.right,remaining)
        
       

        treeWalk(root,targetSum)

        count = count + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

        
        print(count, 'final answer')
        return count





        
if __name__ == "__main__":
    root = [1,-2,-3,1,3,-2,None,-1]
    targetSum = -1
    answer = Solution()
    answer.pathSum(list_to_tree(root), targetSum)

         
