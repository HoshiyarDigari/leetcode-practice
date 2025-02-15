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
        - prefix sum of a node  - sum of values from  root to that node
        - we keep this prefix sum in a dictionary.
        - when we go down the tree, we update prefix sum of the child to dictionary
        - a valid path to a node must satisfy:
            - current sum = target sum
            - current sum - targetSum = some previous prefix sum
        - when we backtrack , which is after the node.left and node.right calls, we remove current prefix sum from the dictionary. This way it doesn't impact any other branches
        """
        # this helps us check the case where prefix sum equals targetSum
        prefixSums = {0:1} 
        print(prefixSums)
        if not root:
            return 
        
        
        count = 0 # to count occurences of valid paths
        # function to do the DFS 
        def isPathSum(node:TreeNode, prefixSums:dict, sum:int, targetSum:int):
            nonlocal count # so it can access this count across recursive calls
            print('\n Examining node', node, 'prefixSums is ', prefixSums)
            if not node:
                return
            current_sum = node.val + sum
            #add prefix sums to dictionary
            
            if prefixSums.get(current_sum - targetSum, 0) !=0:
                count+=prefixSums[current_sum -targetSum]
                print('\n found valid path at ', node.val)
            # we add this sum to the prefixSums after we have checked above condition. if we do this before the above if, it can lead to issues, specially with edge case of 0 targetSum    
            prefixSums[current_sum]= prefixSums.get(current_sum,0)+1
            isPathSum(node.left, prefixSums, current_sum, targetSum)
            isPathSum(node.right, prefixSums, current_sum, targetSum)

            # when both left and node have been recursed, we are backtracking, we need to remove the prefix Sum now , so it doesn't impact non- linked sub trees
            
            if prefixSums[current_sum]==1:
                del(prefixSums[current_sum])
            else:
                prefixSums[current_sum]-=1
            print('removed current sum at backtrack',node, prefixSums)
        
        isPathSum(root, prefixSums,0, targetSum)
        print('count is ', count)

if __name__ == "__main__":
    root = [0,1,0]
    targetSum = 1
    answer = Solution()
    answer.pathSum(list_to_tree(root), targetSum)

         
