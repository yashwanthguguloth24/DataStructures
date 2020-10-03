'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def findMax(root):
    '''
    :param root: root of the given tree.
    :return: max 
    
    '''
    curr = root
    if curr == None:
        return -1
    maxval = curr.data
    left = findMax(curr.left)
    right = findMax(curr.right)
    if left>maxval:
        maxval = left
    if right>maxval:
        maxval = right
    return maxval
    
    
def findMin(root):
    '''
    :param root: root of the given tree.
    :return: min 
    
    '''
    curr = root
    if curr == None:
        return 10**6
    minval = curr.data
    left = findMin(curr.left)
    right = findMin(curr.right)
    if left<minval:
        minval = left
    if right<minval:
        minval = right
    return minval
