'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def pre(root,arr):
    if root == None:
        return 
    arr.append(root.data)
    pre(root.left,arr)
    pre(root.right,arr)

def preorder(root):
    '''
    :param root: root of the given tree.
    :return: a list containing pre order Traversal of the given tree.
    {
        class Node:
        def _init_(self,val):
            self.data = val
            self.left = None
            self.right = None
    }
    '''
    arr = []
    pre(root,arr)
    return arr
