# My min heap class

class MyMinHeap:
    def __init__(self,l = []):
        # 0 based indexing
        self.arr = l
        if self.arr == []:
            self.size = 0
        else:
            self.size = len(self.arr)
        i = (self.size-2)//2
        while i >= 0:
            self.MinHeapify(self.size,i)
            i -= 1

    def parent(self,i):
        return (i-1)//2

    def lChild(self,i):
        return 2*i+1

    def rChild(self,i):
        return 2*i+2

    def showHeap(self):
        return self.arr

    def insert(self,val):
        if self.size == 0:
            self.arr.append(val)
            self.size += 1
            return
        self.arr.append(val)
        self.size += 1
        child = self.size-1
        parent = self.parent(child)
        while parent >= 0 and self.arr[parent] > self.arr[child]:
            self.arr[parent],self.arr[child] = self.arr[child],self.arr[parent]
            child = parent
            parent = self.parent(child)


    def MinHeapify(self,n,i):
        left = self.lChild(i)
        right = self.rChild(i)
        smallest = i
        if left < n and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right < n and self.arr[right] < self.arr[smallest]:
            smallest = right
        if smallest != i:
            self.arr[i],self.arr[smallest] = self.arr[smallest],self.arr[i]
            self.MinHeapify(n,smallest)

    def extractMin(self):
        if self.size == 0:
            return float('inf')
        result = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.arr.pop()
        self.size -= 1
        self.MinHeapify(self.size,0)
        return result

    def decreaseKey(self,i,x):
        self.arr[i] = x
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i],self.arr[p] = self.arr[p],self.arr[i]
            i = p

    def deleteKey(self,i):
        if self.size == 0 and i >= self.size:
            return
        else:
            self.decreaseKey(i,float('-inf'))
            self.extractMin()

    def heapSort(self):
        return [self.extractMin() for _ in range(self.size)]

heap = MyMinHeap([5,4,3,2,1])
heap.decreaseKey(2,0)
print(heap.heapSort())
print(heap.arr)


