'''
Input:
LinkList1 = {10,20,5,10}
LinkList2 = {30,40,50,5,10}
Output: 5
Explanation:The point of intersection of
two linked list is 5, means both of them
get linked (intersects) with each other
at node whose value is 5.
'''

def intersetPoint(head_a,head_b):
    #code here
    l1 = 0
    l2 = 0
    temp1 = head_a
    temp2 = head_b
    while temp1 != None:
        l1 += 1
        temp1 = temp1.next
    while temp2 != None:
        l2 += 1
        temp2 = temp2.next
    if l1 > l2:
        diff = l1-l2
        while diff > 0:
            head_a = head_a.next
            diff -= 1
        while head_a != head_b:
            head_a = head_a.next
            head_b = head_b.next
        if head_a == None:
            return -1
        else:
            return head_a.data
    else:
        diff = l2-l1
        while diff > 0:
            head_b = head_b.next
            diff -= 1
        while head_a != head_b:
            head_a = head_a.next
            head_b = head_b.next
        if head_a == None:
            return -1
        else:
            return head_a.data        
         
