# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if A.next == None and B == 1:
            return None
        l = 0
        temp = A
        while temp != None:
            l += 1
            temp = temp.next
        if B > l:
            A = A.next
            return A
        node = l-B+1
        if node == 1:
            A = A.next
            return A
        i = 1
        temp = A
        while i < node-1:
            temp = temp.next
            i += 1
        if temp.next == None:
            temp.next = None
        else:
            temp.next = temp.next.next
        return A
