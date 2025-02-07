# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

    # function to print the linked list
    def __str__(self):
        result = ''
        current = self
        while current:
            result+=str(current.val)
            current = current.next
        return '-->'.join(result)

    def get_next(self):
        return self.next
    
    def size(self):
        current = self
        size = 0
        while current:
            size+=1
            current = current.next
        return size
    
def deleteMiddle( head: Optional[ListNode]) -> Optional[ListNode]:
        def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        temp = head
        size=0
        node_list = {}
        while temp is not  None:
            #build dictionary
            node_list.update({size:temp.next})
            size+=1
            temp=temp.next
    
        middle = size//2
    
        # the next pointer of the middle node is in the dictionary , we assign this value to the node before the middle node. We have to get to the node that has middle's pointer so it can be replaced to break the middle node out of the link list
        temp2 = head
        # print(node_list)
        if middle == 0:
            return head.next
        elif middle == 1:
            # print('mid is ',middle,'updating heads pointer to', node_list[middle])
            head.next = node_list[middle]
            return head
        else:
            # directly go to the middle's predecessor address
            node_to_update = node_list[middle-2]
            node_to_update.next = node_list[middle]
            return head


        


if __name__ == "__main__":
    val = [1,3,4,7,1,2,6]
    head = ListNode(1,ListNode(3, ListNode(4,ListNode(7,ListNode(1,ListNode(2,ListNode(6)))))))
    
    print(head.get_next())
    print(head.size())
    
          
    deleteMiddle(head)
