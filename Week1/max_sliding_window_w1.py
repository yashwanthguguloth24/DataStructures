from collections import deque

def max_sliding_window(array,k,n):

    "deque stores the index of max and min elements"
    Q = deque()

    for i in range(k):
        while Q and array[i] >= array[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k,n):

        print(str(array[Q[0]]) + " ", end="")

        #remove the elements out of window
        while Q and Q[0] <= i-k:
            Q.popleft()

        #remove all elements if they are less than array[i]
        while Q and array[i] >= array[Q[-1]]:
            Q.pop()

        Q.append(i)

    # print last elements
    print(str(array[Q[0]]))


if __name__ == "__main__":
    n = int(input())
    array = list(map(int,input().split()))
    k = int(input())
    max_sliding_window(array,k,n)