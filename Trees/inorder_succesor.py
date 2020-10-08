'''
Given a BST,  and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.
 

Example 1:

Input:
      2
    /   \
   1     3

K(data of x) = 2

Output: 3
'''

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# returns the inorder successor of the Node x in BST (rooted at 'root')
def Find(root,x):
    curr = root
    while curr != None:
        if curr.data == x.data:
            return curr
        elif curr.data > x.data:
            curr = curr.left
        else:
            curr = curr.right
    return None
    
def FindMin(root):
    node = root
    if node == None:
        return None
    while node.left != None:
        node = node.left
    return node
    
def inorderSuccessor(root, x):
    temp = Find(root,x)
    if temp == None:
        return None
    if temp.right != None:
        return FindMin(temp.right)
    else:
        succesor = None
        ancestor = root
        while (ancestor != temp):
            if temp.data < ancestor.data:
                succesor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return succesor
        
