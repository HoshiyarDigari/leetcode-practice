"""
algo:
- scan through the list. Each scan track current node and its left and right nodes.
- change current node's next pointer to left_node, that way the direction of arrow is reversed.
- move the scanner by updating left node to current node, current node to right node and right node to right node's next pointer
-  


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

    
def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
    # base case , empty or 1 item list
    if not head or not head.next:
        print(head)
        return head
    
    # we have 3 pointers, left-node, right-node and current-node
    current_node = head
    left_node = None
    right_node = head.next
    
    # we scan till the current node is last one, its right-node is None

    while right_node:
        print('current',current_node,'left',left_node,'right',right_node)
        #temporary variables to hold left, right and current, we can delete some of them afterwards
        #temp_right = right_node
        
        #update the pointers using the temp variables
        current_node.next = left_node
        # move current one place
        left_node = current_node
        current_node=right_node
        right_node = right_node.next

        

    current_node.next = left_node    
    print('current',current_node,'left',left_node,'right',right_node)
    #print(head)

    
    
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
    

    
          
    reverseList(head)
