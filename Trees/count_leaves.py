'''
Given a Binary Tree of size N , You have to count leaves in it. For example, there are two leaves in following tree

        1
     /      \
   10      39
  /
5
'''

#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def countLeaves(root):
    curr = root
    count = 0
    if curr == None:
        return 0
    if curr.right == None and curr.left == None:
        count += 1
    count += countLeaves(curr.left)
    count += countLeaves(curr.right)
    return count
