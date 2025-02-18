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
    # define a hash function 
    def __hash__(self):
        return hash((self.val, self.left, self.right))  # Tuple of immutable attributes

    # turn a list to a binary tree in BFS
    @staticmethod
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

    # find a node of given value in a Tree
    @staticmethod
    def find_node_iterative(root, value):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == value:
                    return node
                stack.append(node.right)
                stack.append(node.left)
        return None

    @staticmethod
    def find_node_recursive(root, value):
        if not root:
            return None
        if root.val == value:
            return root
        leftSearch = TreeNode.find_node_recursive(root.left, value)
        if leftSearch:
            return leftSearch
        rightSearch = TreeNode.find_node_recursive(root.right, value)
        
        if rightSearch:
            return rightSearch
        return None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Algo:
        - DFS walk on the tree
        - return when the node is either p and q
        - when both recursive calls are done, check if we got p and q both.
        - if yes, then the current node is the LCA
        """
        print('examining', root)
        if not root:
            return 
        if root == p:
            return root
        if root == q:
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            print('lca is ', root)
            return root
        
        print(left or right)


        
        
if __name__ == "__main__":
    answer = Solution()
    root = TreeNode.list_to_tree([3,5,1,6,2,0,8,None,None,7,4])
    p = TreeNode.find_node_recursive(root, 5)
    
    q = TreeNode.find_node_recursive(root,4)
    answer.lowestCommonAncestor(root, p, q)
    #done

         
