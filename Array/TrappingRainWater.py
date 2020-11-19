'''
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output: 10
'''

def trappingWater(arr,n):
    left_max = 0
    right_max = 0
    l = 0
    r = n-1
    ans = 0
    while l < r:
        if arr[l] < arr[r]:
            if arr[l] >= left_max:
                left_max = arr[l]
            else:
                ans += left_max-arr[l]
            l += 1
        else:
            if arr[r] >= right_max:
                right_max = arr[r]
            else:
                ans += right_max-arr[r]
            r -= 1
    return ans
                
