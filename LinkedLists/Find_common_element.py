# Find the first common node in two singly linked list
# Microsoft Interview question
# O(n) using Hashing

class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        
def Common_Node(head1,head2):
    H = set()
    temp1 = head1
    while temp1.next != None:
        H.add(temp1.data)
        temp1 = temp1.next
    temp2 = head2
    while temp2.next != None:
        if temp2.data in H:
            return temp2.data
        else:
            temp2 = temp2.next
    return -1
    
def Push(head,val):
    new_node = Node()
    new_node.data = val
    new_node.next = head
    head = new_node
    return head
    
    
Head1 = None
Head2 = None

Head1 = Push(Head1,4)
Head1 = Push(Head1,3)
Head1 = Push(Head1,2)
Head1 = Push(Head1,1)

Head2 = Push(Head2,7)
Head2 = Push(Head2,3)
Head2 = Push(Head2,6)
Head2 = Push(Head2,5)

print(Common_Node(Head1,Head2))
