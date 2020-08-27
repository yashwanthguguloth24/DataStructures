# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        # recursive call
        def InOrderRecursive(i,result):
            if self.left[i] != -1:
                InOrderRecursive(self.left[i],result)
            result.append(self.key[i])
            if self.right[i] != -1:
                InOrderRecursive(self.right[i],result)
        InOrderRecursive(0,result)

        return result

    def preOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        def PreOrderRecursive(i, result):
            result.append(self.key[i])
            if self.left[i] != -1:
                PreOrderRecursive(self.left[i], result)
            if self.right[i] != -1:
                PreOrderRecursive(self.right[i], result)
        PreOrderRecursive(0,result)

        return result

    def postOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        def PostOrderRecursive(i,result):
            if self.left[i] != -1:
                PostOrderRecursive(self.left[i],result)
            if self.right[i] != -1:
                PostOrderRecursive(self.right[i],result)
            result.append(self.key[i])
        PostOrderRecursive(0,result)
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
