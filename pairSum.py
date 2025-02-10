"""
algo:
- create a list with the values in the linked list. 
- Twins  in even list are the items at front and end of list. 
- We use front and end pointer to move inwards in the list 
- we return the max of twin sums


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
    #dump into a list and then use the list to find the twin sums directly without need of link list traversal
    node = head
    node_list = []
    while node:
        node_list.append(node.val)
        node = node.next
    print(node_list)


    # scan the list from both ends and return the max twin sum
    pairSum = 0
    front, end = 0, len(node_list)-1
    
    while front < end:
        pairSum=max(pairSum, node_list[front] + node_list[end])
        front +=1
        end-=1
    print(pairSum)



    

        

    
    
if __name__ == "__main__":
    val = [1,8,3,4,8,9]
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
