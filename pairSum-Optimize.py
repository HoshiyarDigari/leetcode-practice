"""
algo:
- twins are at the end of the list.
- we will reverse the second half of the list and then add to the first half.
    - we use slow and fast pointer to get to the middle of the list.

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

def reverseList(head:Optional[ListNode])-> Optional[ListNode]:
    # list is empty or single element
    if not head or not head.next:
        return head
    # 2 or more elements, we use left right and current pointers to reverse pointer direction
    current = head
    left = None
    right = current.next

    while right:
        print('we are at ', current, 'with left', left , 'and right', right)
        current.next, left, current, right = left, current, right, right.next
    current.next = left
    print('reversed list', current)
    return (current)
def pairSum( head: Optional[ListNode]) -> Optional[ListNode]:
    # 
    #slow and fast pointers to get to middle of list, input list is at least 2 items
    slow = head
    fast = head

    while fast and fast.next:
        print('slow is at ', slow, 'fast is at', fast)
        slow = slow.next
        fast = fast.next.next
    # we reverse the list from the middle, slow is at the middle of the list
    slow = reverseList(slow)
    # now the two lists to compare are 
    print(head, slow)
    pairSum = 0
    while head and slow:
        pairSum = max(pairSum, head.val + slow.val)
        head = head.next
        slow = slow.next
    print(pairSum)


    

        

    
    
if __name__ == "__main__":
    val = [1,2,3,4]
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
    

    
          
    pairSum(head)
