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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        algo:
        - function leafSequence will generate the leaf Sequence for a tree
        - we will compare root1 and root2 leaf sequences

        """
        leafs1 = self.leafSequence(root1,leafs=[] )
        leafs2 = self.leafSequence(root2,leafs=[])
        print('leafs 1 ', leafs1, 'leafs 2 ', leafs2)
        return leafs1 == leafs2
    

    def leafSequence(self,node: Optional[TreeNode], leafs) -> list:
        """
        algo:
        - if current node is leaf , add to leaf list
        - if not recursively check the left node and right node
        """
        # base case
        if not node:
            return []
        if not node.left and not node.right:
            print(node.val, 'leaf found')
            leafs.append(node.val)
            print('returning ', leafs)
            #return leafs
        if node.left:
            print('left tree check for ', node.val)
            self.leafSequence(node.left, leafs)
        if node.right:
            print('right tree check for ', node.val)
            self.leafSequence(node.right,leafs)
        return leafs
        
    

        

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
    root1 = [3,5,1,6,2,9,8,None,None,7,4]
    root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    answer = Solution()
    answer.leafSimilar(list_to_tree(root1), list_to_tree(root2))

         
