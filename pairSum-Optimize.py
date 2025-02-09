"""
algo:
- we will create a list of prefix sums as we traverse the list.



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
    
    # generate list of prefix sums
    prefixSums=[head.val]
    current = head.next
    size = 0
    while current:
        prefixSums.append(current.val + prefixSums[-1])
        print(prefixSums)
        current = current.next



    

        

    
    
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
