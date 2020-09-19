'''
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    # def Addhead(self,head,data):
    #     if head == None:
    #         head = ListNode(data)
    #     newNode = ListNode(data)
    #     newNode.next = head
    #     head = newNode
    #     return head
        
    def lPalin(self, A):
        l = 0
        temp = A
        while temp != None:
            l = l+1
            temp = temp.next
            
        if l%2 == 0:
            i = 1
            mid = l//2
            temp = A
            prev = None
            while i <= mid:
                nextVal = temp.next
                temp.next = prev
                prev = temp
                temp = nextVal
                i += 1
            end = temp
            start = prev
    
            while start != None and end != None:
                if start.val != end.val :
                    return 0
                else:
                     start = start.next
                    end = end.next
            return 1
            
        else:
            i = 1
            mid = l//2 + 1
            temp = A
            prev = None
            while i < mid:
                nextVal = temp.next
                temp.next = prev
                prev = temp
                temp = nextVal
                i += 1
            end = temp.next
            start = prev
    
            while start != None and end != None:
                if start.val != end.val :
                    return 0
                else:
                    start = start.next
                    end = end.next
            return 1
            
            
        # rev = None
        # curr = A
        # while curr != None:
        #     rev = self.Addhead(rev,curr.val)
            
        # temp = A
        # revtemp = rev
        
        # wh
        # return 1ile temp != None and revtemp != None:
        #     if temp.val != revtemp.val:
        #         return 0
        #     else:
        #         temp = temp.next
        #         revtemp = revtemp.next
                
