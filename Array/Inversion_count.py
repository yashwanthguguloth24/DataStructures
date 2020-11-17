'''
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
'''


def _mergeSort(arr, temp_arr, left, right): 

    inv_count = 0

    if left < right: 

        mid = (left + right)//2
  
        inv_count += _mergeSort(arr, temp_arr,left, mid) 
  
        inv_count += _mergeSort(arr, temp_arr,mid + 1, right) 
  
        # It will merge two subarrays in  
        # a sorted subarray 
  
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  

def merge(arr, temp_arr, left, mid, right): 
    i = left     # Starting index of left subarray 
    j = mid + 1 # Starting index of right subarray 
    k = left     # Starting index of to be sorted subarray 
    inv_count = 0
  
    while i <= mid and j <= right: 
  
        # There will be no inversion if arr[i] <= arr[j] 
  
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            # Inversion will occur. 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  

    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  

    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1

    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count 
    
    
def inversionCount(a,n):
    # Your Code Here
    temp_arr = [0]*n 
    arr = a
    return _mergeSort(arr, temp_arr, 0, n-1) 
    


