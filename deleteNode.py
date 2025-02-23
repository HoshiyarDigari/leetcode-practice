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
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """
        Algo:
        1. visit room 0
        2. if there is at least one room key, visit that room
        3. pick up keys if any and visit other rooms
        4. when all rooms are visited or no more keys left , we are done
        """
        canVisit = [0]
        visitedRooms = {0}
        while canVisit:
            print('we are visiting room', canVisit[-1])
            keys = rooms[canVisit.pop()]
            print('this room has keys', keys, 'and visited rooms so far', visitedRooms)
            if keys:
                for key in keys:
                    if key not in visitedRooms:
                        canVisit.append(key)
                        print('added ', key, 'to ', canVisit)
                        visitedRooms.add(key)
        print( len(rooms)==len(visitedRooms))

        

            



                
        
        
        
if __name__ == "__main__":
    rooms = [[1],[2],[3],[]]

    key = 7
    answer = Solution()
    answer.canVisitAllRooms(rooms)

         
