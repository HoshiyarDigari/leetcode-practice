"""
algo:
1.use two pointers slow - it moves one step in the list, fast - moves two steps in the list
2. when fast reaches end, slow will be at the middle
3. switch pointers to remove the middle from the list

"""

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # method to add another node
    def add(self, node):
        temp = self
        while temp.next!=None:
            temp=temp.next
        temp.next=node
        return self
    
    # function to print the linked list
    def __str__(self):
        result = ''
        current = self
        while current:
            result+=str(current.val)
            current = current.next
        return '-->'.join(result)

    
def deleteMiddle( head: Optional[ListNode]) -> Optional[ListNode]:
    """
    What’s the Best Way?
    Use two pointers: slow and fast.
    Keep track of the node before slow (let's call it prev).
    When fast reaches the end, slow will be at the middle.
    Update prev.next = slow.next to remove the middle node.
    """

    slow, fast = head, head

    # return None if list is empty or has only one node
    if not head or not head.next:
        print('return empty')
        return None
    
    # traverse till fast reaches end of the list. Fast hops 2 nodes while slow goes 1 step. Thefore, slow is at half distance of fast which is the middle
    # we stop when fast itself is None or its pointing to None, because then it cannot hop 2 steps
    # we keep track of previous node before slow so we can update its next pointer
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    print('slow', slow, 'prev', prev, 'fast', fast)
    prev.next = slow.next
    print(head)
    return head



if __name__ == "__main__":
    val = [1,2,3]
    head = None
    for value in val:
        if not head:
            head=ListNode(value)
            #print('new head created')
        else:
            temp = ListNode(value)
            #print('new node', temp)
            head.add(temp)
         
        #print(head)
         

         
    #head = ListNode(1,ListNode(3, ListNode(4,ListNode(7,ListNode(1,ListNode(2,ListNode(6)))))))
    

    
          
    deleteMiddle(head)
