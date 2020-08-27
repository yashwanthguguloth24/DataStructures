# python3

import sys
import threading


def compute_height(n, parents):
    heights = [0]*n
    # max_height = 0
    for vertex in range(n):
        if heights[vertex] != 0:
            continue
        height = 0
        current = vertex

        while current != -1:
            if heights[current] != 0:
                height += heights[current]
                break
            height += 1
            current = parents[current]
        heights[vertex] = height
        # max_height = max(max_height, height)
    return max(heights)



n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
