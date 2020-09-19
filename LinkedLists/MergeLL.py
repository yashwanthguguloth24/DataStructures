'''
For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
'''


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        out = ListNode(0)
        temp1 = A
        temp2 = B
        i = 0
        j = 0
        temp = out
        while temp2 != None and temp1 != None:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
                i += 1
                temp = temp.next
            else:
                temp.next = temp2
                temp2 = temp2.next
                j += 1
                temp = temp.next
                
        while temp1 != None:
            temp.next = temp1
            temp1 = temp1.next
            i += 1
            temp = temp.next            
        
        while temp2 != None:
            temp.next = temp2
            temp2 = temp2.next
            j += 1
            temp = temp.next 
            
        return out.next
    
