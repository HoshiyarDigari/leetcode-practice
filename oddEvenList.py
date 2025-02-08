"""
algo:


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

    
def oddEvenList( head: Optional[ListNode]) -> Optional[ListNode]:
    # cases for empty list, 1 item or 2 item list
    if not head or not head.next or not head.next.next:
        print(head)
        return head
    
    # if there are at least 3 items, we have to reorder

    #these will keep track of start of odd and even nodes
    odd_head = head
    even_head = head.next

    # these will move through the linked list 
    odd = head
    even = head.next
    
    while odd and even and even.next:
        if odd.next:
            odd.next = odd.next.next
        even.next = even.next.next
        
        odd = odd.next
        even = even.next
    
    
    odd.next = even_head
    
    print(even_head)
    
    print(odd_head)
   

    
    
if __name__ == "__main__":
    val = [1,2,3,4,5,6,7,8]
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
    

    
          
    oddEvenList(head)
