

import heapq

pq = [30,5,10,2,3]
heapq.heapify(pq)
print(pq)                                    # 1
heapq.heappush(pq,4)
print(pq)                                    # 2

# extracts min element
print(heapq.heappop(pq))                     # 3
print(pq)                                    # 4

# nlargest elements
print(heapq.nlargest(2,pq))                  # 5
# nsmallest elements
print(heapq.nsmallest(2,pq))                 # 6

# heappushpop --> first pushes the element into the heap then extracts min elements
print(heapq.heappushpop(pq,6))               # 7
print(pq)                                    # 8

print(heapq.heappushpop(pq,0))               # 9
print(pq)                                    # 10

# heapreplace --> replaces the root with the given value
print(heapq.heapreplace(pq,-1))              # 11
print(pq)                                    # 12



'''
Output:
# 1   - [2, 3, 10, 5, 30]
# 2   - [2, 3, 4, 5, 30, 10]
# 3   - 2
# 4   - [3, 5, 4, 10, 30]
# 5   - [30, 10]
# 6   - [3, 4]
# 7   - 3
# 8   - [4, 5, 6, 10, 30]
# 9   - 0
# 10  - [4, 5, 6, 10, 30]
# 11  - 4
# 12  - [-1, 5, 6, 10, 30]
'''


