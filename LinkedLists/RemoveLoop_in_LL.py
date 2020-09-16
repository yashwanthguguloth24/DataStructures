'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
def detectloop(head):
    fastptr = head
    slowptr = head
    while fastptr.next and fastptr.next.next and slowptr.next:
        fastptr = fastptr.next.next
        slowptr = slowptr.next
        if fastptr == slowptr:
            return slowptr,fastptr
    return None

def removeLoop(head):
    if detectloop(head) == None:
        return 
    slowptr,fastptr = detectloop(head)
    firstptr = head
    if slowptr == head:
        while firstptr.next != head:
            firstptr = firstptr.next
        firstptr.next = None
    else: 
        slowptr = head
        while slowptr.next != fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next
        fastptr.next = None
        
        
        
        
