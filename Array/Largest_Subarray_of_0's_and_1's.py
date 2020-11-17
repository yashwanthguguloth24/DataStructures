'''
Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.

Example 1:

Input:
N = 4
A[] = {0,1,0,1}
Output: 4
Explanation: The array from index [0...3]
contains equal number of 0's and 1's.
Thus maximum length of subarray having
equal number of 0's and 1's is 4.
'''


def maxLen(arr, N):
    for i in range(N):
        if arr[i] == 0:
            arr[i] = -1
            
    max_len = 0
    hash_map = {}
    curr_sum = 0

    for i in range(N):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = i+1

        if curr_sum in hash_map:
            if max_len < i-hash_map[curr_sum]:
                max_len = i-hash_map[curr_sum]

        else:
            hash_map[curr_sum] = i
    
    return max_len
