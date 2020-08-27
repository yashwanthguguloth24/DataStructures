# python3


# def build_heap(data):
#     """Build a heap from ``data`` inplace.
#
#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps,data

class Minheap:
    def __init__(self):
        self.swaps = []
        self.data = []

    def read_input_data(self):
        #reads input
        n = int(input())
        x = [int(i) for i in input().split()]
        for j in range(len(x)):
            self.data.append(x[j])

    def write_output(self):
        #writes output
        print(len(self.swaps))
        for i in range(len(self.swaps)):
            print(*self.swaps[i])

    def ShiftDown(self,i):
        #swaps the elements if the value of parent is greater than the child
        minIndex = i
        l = 2*i+1
        r = 2*i+2

        if l < len(self.data) and self.data[l] < self.data[minIndex]:
            minIndex = l

        if r < len(self.data) and self.data[r] < self.data[minIndex]:
            minIndex = r

        if i != minIndex:
            self.swaps.append((i,minIndex))
            self.data[i],self.data[minIndex] = self.data[minIndex],self.data[i]
            self.ShiftDown(minIndex)

    def BuildHeap(self):
        #Build minheap
        for i in range(len(self.data)//2,-1,-1):
            self.ShiftDown(i)

    def solve_these_steps(self):
        #solve the problem in this sequence
        self.read_input_data()
        self.BuildHeap()
        self.write_output()


if __name__ == "__main__":
    minHeap = Minheap()
    minHeap.solve_these_steps()
