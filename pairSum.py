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

    
def pairSum( head: Optional[ListNode]) -> Optional[ListNode]:
    #dump into a dictionary and then use the dictionary to find the twin sums directly without need of link list traversal
    node = head
    node_dict = {}
    size = 0
    while node:
        node_dict.update({size:node.val})
        node = node.next
        size+=1
    print(node_dict, 'size is ', size)

    # now we know the size(n) of the list and we need to find the twin nodes i and (n-1-i)th tuples
    twin_nodes = set()
    for i in range(size//2):
        twin_nodes.add((i, size-1-i))
    print(twin_nodes)

    # now we know all the twin pairs, look up in dictionary and add their values and return the maximum one
    pairSum = 0
    for i,twin in twin_nodes:
        pairSum = max(pairSum,(node_dict[i] + node_dict[twin]))
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
