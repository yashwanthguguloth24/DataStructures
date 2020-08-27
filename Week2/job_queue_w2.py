# # python3
#
# from collections import namedtuple
#
# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
#
#
# def assign_jobs(n_workers, jobs):
#     # TODO: replace this code with a faster algorithm.
#     result = []
#     next_free_time = [0] * n_workers
#     for job in jobs:
#         next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#         result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#         next_free_time[next_worker] += job
#
#     return result
#
#
# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     assert len(jobs) == n_jobs
#
#     assigned_jobs = assign_jobs(n_workers, jobs)
#
#     for job in assigned_jobs:
#         print(job.worker, job.started_at)



class MinHeap:
    def __init__(self, num_workers):
        self.data = []
        self.n = num_workers
        for i in range(self.n):
            self.data.append((i,0))

    '''
    Min heap has methods ChangePriority,RepairHeap,Parent,LeftChild,rightChild,CompareWorkers,ShiftUp,ShiftDown

    '''

    def ChangePriority(self, index, priority):
        old_p = self.data[index][1]
        self.data[index] = (self.data[index][0], priority)
        if priority < old_p:
            self.SiftUp(index)
        else:
            self.SiftDown(index)

        self.SiftDown(index)


    def RepairHeap(self):
        for i in range(int(self.n / 2), -1, -1):
            self.SiftDown(i)


    def Parent(self,i):
        return (i-1)//2

    def LeftChild(self,i):
        return 2*i+1

    def RightChild(self,i):
        return 2*i+2

    def CompareWorker(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]

    def SiftUp(self, i):
        while i > 0 and self.CompareWorker(self.data[i], self.data[self.Parent(i)]):
            self.data[i], self.data[self.Parent(i)] = self.data[self.Parent(i)], self.data[i]
            i = self.Parent(i)

    def SiftDown(self, i):
        minIndex = i
        left = self.LeftChild(i)
        if left < self.n and self.CompareWorker(self.data[left], self.data[minIndex]):
            minIndex = left

        right = self.RightChild(i)
        if right < self.n and self.CompareWorker(self.data[right], self.data[minIndex]):
            minIndex = right
        if i != minIndex:
            self.data[i], self.data[minIndex] = self.data[minIndex], self.data[i]
            self.SiftDown(minIndex)

class JobQueue:
    def read_data(self):
        self.num_workers , m = map(int,input().split())
        self.jobs = [int(x) for x in input().split()]
        assert m == len(self.jobs)

    def write_output(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i],self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        min_heap = MinHeap(self.num_workers)
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = min_heap.data[0][0]
            self.start_times[i] = min_heap.data[0][1]
            min_heap.ChangePriority(0, min_heap.data[0][1] + self.jobs[i])


    def Solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_output()



if __name__ == "__main__":
    jobqueue = JobQueue()
    jobqueue.Solve()
