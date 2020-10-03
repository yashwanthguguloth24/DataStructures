'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def post(root,arr):
    if root == None:
        return 
    post(root.left,arr)
    post(root.right,arr)
    arr.append(root.data)
    
def postOrder(root):
    '''
    :param root: root of the given tree.
    :return the list containing post order traversal of the given binary tree.
    '''
    arr = []
    post(root,arr)
    return arr
