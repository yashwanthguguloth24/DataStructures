'''
Given a Binary Search Tree and a node value X. Delete the node with the given value X from the BST. If no node with value x exists, then do not make any change. 

Example 1:

Input:
      2
    /   \
   1     3
X = 12
Output: 1 2 3
Explanation: In the given input there
is no node with value 12 , so the tree
will remain same.
'''


'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# Return the root of the modified BST after deleting the node with value X
def FindMax(root):
    node = root
    if node == None:
        return None
    while node.right != None:
        node = node.right
    return node
    
    
def deleteNode(root, X):
    temp = None
    if root != None:
        if root.data == X:
            if root.left == None and root.right == None:
                return None
            else:
                if root.left == None:
                    temp = root.right
                    return temp
                if root.right == None:
                    temp = root.left
                    return temp
                maxNode = FindMax(root.left)
                root.data = maxNode.data
                root.left = deleteNode(root.left,maxNode.data)
        else:
            if root.data > X:
                root.left = deleteNode(root.left, X)
            else:
                root.right = deleteNode(root.right, X)
    return root
   
