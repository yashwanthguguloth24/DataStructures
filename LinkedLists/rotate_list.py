'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        l = 1
        temp = A
        temp1 = A
        while temp.next != None:
            l += 1
            temp = temp.next
        temp.next = A
    
        i = 1
        new_B = B%l
        t = l-new_B
        while i < t:
            temp1 = temp1.next
            i += 1
        node = temp1.next
        temp1.next = None
        A = node
        return A
