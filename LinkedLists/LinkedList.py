
class LinkedList:
    class Node:
        def __init__(self, val):
            self.data = val
            self.next = None

    def __init__(self):
        self.head = None

    def push(self,val):
        NewNode = self.Node(val)
        if self.head == None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

    def PrintList(self):
        temp = self.head
        while temp!= None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def Removehead(self):
        temp = self.head
        self.head = temp.next

    def deleteNode(self,num):
        # base case
        if self.head.data == num:
            self.Removehead()
        else:
            temp = self.head
            while temp.next.data != num:
                temp = temp.next
            temp.next = temp.next.next

    def All_Nodes_of_K(self,k):
        currNode = self.head
        if self.head.data == k:
            self.head = self.head.next
        else:
            while currNode != None:
                nextNode = currNode.next
                if nextNode != None and nextNode.data == k:
                    currNode.next = nextNode.next
                else:
                    currNode = currNode.next

    def Delete_LinkedList(self):
        self.head = None

    def reverse_LL(self):
        curr = self.head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


    def Remove_duplicates_for_sortedLL(self):
        temp = self.head
        while temp != None:
            if temp.next != None and temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def Length(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def Nth_Node_from_start(self,n):
        # assuming we dont choose the value of n that doesnt exist
        count = 1
        temp = self.head
        while temp != None and count < n:
            count += 1
            temp = temp.next
        print(temp.data)

    def Nth_Node_from_end(self,n):
        L = self.Length()
        if n > L:
            print("Error")
        else:
            n_0 = L-n+1
            self.Nth_Node_from_start(n_0)


# L = LinkedList()
# L.push(10)
# L.push(9)
# L.push(2)
# L.push(3)
# L.push(4)
# L.push(2)
# L.push(5)
# L.PrintList()
# L.reverse_LL()
# L.PrintList()

L2 = LinkedList()
for k in [10,10,3,3,2,2,1,1,1,1]:
    L2.push(k)
# L2.Remove_duplicates_for_sortedLL()
# L2.Nth_Node_from_start(10)
L2.Nth_Node_from_end(11)
L2.PrintList()
