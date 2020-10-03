'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
def mirror(root):
    # Code here
    curr = root
    if curr == None:
        return 0
    else:
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        
    mirror(curr.left)
    mirror(curr.right)
