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
    def deleteNode(self,root: Optional[TreeNode], key:int) -> Optional[TreeNode]:
        """
        Algo:
        - find the node whose value equals the key, keep track of the parent as well.
        - edge cases
            when root is to be deleted
            empty tree
            value not in tree
        if found, replace it with one of its child
        transfer other child to the 'child' that replaced the node
        details:
        -promote left child to the deleted Node's place. If no left child, promote right child.
        - if left and right exists, then we need to insert the right child to the newly promoted sibling(left child) at the right place.
        - we insert it in the right subtree leaf right node.

        """
        # empty tree
        if not root:
            return None
        
        parent = root # keep track of parent of the node being evaluated
        toDelete = None
        side = None # keep track of which side of the parent needs to be updated
        temp = root
        while temp:
            if temp.val == key:
                toDelete = temp
                break
            elif key > temp.val:
                parent = temp
                temp = temp.right
                side = 'right'
                
            else:
                parent = temp
                temp = temp.left
                side = 'left'
                
            
        # if the node doesn't exist, we return the current root as we have nothing to delete
        print('todelete is', toDelete, '\n parent is ', parent.val, 'side is ', side)
        if not toDelete:
            return root
        
        #special case where root is to be deleted
        if toDelete == root:
            print('root needs deleting')
        
            # make leftsubtree the root
            temp = root.right
            if root.left:
                root = root.left
            else: 
                return root.right # there is no left child, so return the right one
            if temp:
                self.insertNode(root, temp, 'right')

        else:
            if toDelete.left:
                setattr(parent, side, toDelete.left)
            else:
                setattr(parent, side, toDelete.right)
                return root
            if toDelete.right:
                self.insertNode(toDelete.left, toDelete.right, 'right' )
        #print(setattr(parent, side, toDelete.left))
        print(root)

    def insertNode(self,root:TreeNode, node:TreeNode, side:'str'):
        """
        function inserts the node into the root   into the root BST as a child of the given side
        """
        print('\n insert ', node , '\n into ', root, 'on the ' , side)
        other_side = 'right' if side == 'left' else 'left'
        if not getattr(root, side): # if there is not a subtree, we simply add the other side
            setattr(root, side, node)
            return
        temp = getattr(root,other_side)
        #get the right leaf node 
        while getattr(temp, side):
            temp = getattr(temp, side)
        #insert the node 
        setattr(temp, side, node)
        return 
    
            



                
        
        
        
if __name__ == "__main__":
    root = [5,3,6,2,4,None,7]

    key = 7
    answer = Solution()
    answer.deleteNode(list_to_tree(root),key)

         
