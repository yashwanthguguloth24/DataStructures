# #!/usr/bin/python3
#
# import sys, threading
#
# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**25)  # new thread will get stack of such size
#
#
# def read():
#     n = int(sys.stdin.readline())
#     if n == 0:
#         print("CORRECT")
#         sys.exit()
#     key = [0 for i in range(n)]
#     left = [0 for i in range(n)]
#     right = [0 for i in range(n)]
#     for i in range(n):
#         [a, b, c] = map(int, sys.stdin.readline().split())
#         key[i] = a
#         left[i] = b
#         right[i] = c
#     return key,left,right
#
#
# def inOrder(key,left,right):
#     result = []
#     # recursive call
#     def InOrderRecursive(i,result):
#         if left[i] != -1:
#             InOrderRecursive(left[i],result)
#         result.append(key[i])
#         if right[i] != -1:
#             InOrderRecursive(right[i],result)
#     InOrderRecursive(0,result)
#
#     return result
#
# def IsBinarySearchTree(result):
#     if len(result) > 1:
#         for i in range(1,len(result)):
#             if (result[i] < result[i-1]):
#                 return False
#     return True
#
#
# def main():
#     key,left,right = read()
#     re = inOrder(key,left,right)
#     if IsBinarySearchTree(re):
#         print("CORRECT")
#     else:
#         print("INCORRECT")
#
# threading.Thread(target=main).start()

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
def IsBinarySearchTree(j, mn, mx):
  if not j in tree: return True
  if tree[j][0] < mn or tree[j][0] > mx: return False
  return IsBinarySearchTree(tree[j][1], mn, tree[j][0] - 1) and IsBinarySearchTree(tree[j][2], tree[j][0] + 1, mx)
def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, int_max, int_min = {}, 2147483647, -2147483648
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
    print(tree)
  else:
    print("INCORRECT")
threading.Thread(target = main).start()
