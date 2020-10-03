'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
def inorder(root,arr):
    if root == None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)
    
def InOrder(root):
    arr = []
    inorder(root,arr)
    return arr
