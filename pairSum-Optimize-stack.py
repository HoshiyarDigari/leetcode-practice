"""
algo:
- twins are at the end of the list.
- we creat a stack with the values of first half of the list
- than we move forward and add pop this stack and add to the current node 
- in the list(1,2,3,4), stack will be (1, 2), then we move to 3 and pop 2 and add to it, then goes to 4 and pops1 to add to it.
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

def pairSum( head: Optional[ListNode]) -> Optional[ListNode]:
    # 
    #slow and fast pointers to get to middle of list, input list is at least 2 items
    slow = head
    fast = head
    stack = list()
    while fast and fast.next:
        print('slow is at ', slow, 'fast is at', fast)
        #make the stack
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    # we reverse the list from the middle, slow is at the middle of the list
   
    # now the stack is 
    print(stack, slow)
    pairSum = 0
    while slow:
        pairSum = max(pairSum, stack.pop() + slow.val)
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
