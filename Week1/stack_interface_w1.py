#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__track = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__stack) == 1:
            self.__track.append(a)
        elif a > self.__track[-1]:
            self.__track.append(a)
        else:
            self.__track.append(self.__track[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__track.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__track[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)





##Naive Algorithm
# # def max_element(arr):
# #     return max(arr)
# n = int(input())
# main_list = []
# for i in range(n):
#     main_list.append([x for x in input().split()])
#
#
# stack = []
# for s in main_list:
#
#     if s[0] == 'push':
#         stack.append(int(s[1]))
#
#     elif s[0] == 'max':
#         print(max(stack))
#
#     elif s[0] == 'pop':
#         stack.pop()

