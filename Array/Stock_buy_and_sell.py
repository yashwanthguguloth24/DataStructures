'''
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output: (0 3) (4 6)
Explanation: We can buy stock on day 
0, and sell it on 3rd day, which will 
give us maximum profit. Now, we buy 
stock on day 4 and sell it on day 6.

'''

# Use local max and local min approach

def stockBuySell(A,n):
    if n == 1:
        return 
    
    values = []
    i = 0
    while i < n-1 :
        while i < n-1 and A[i+1] <= A[i]:
            i += 1
            
        if i == n-1:
            break
        buy = i
        i += 1
        
        while i < n and A[i] >= A[i-1]:
            i += 1
            
        sell = i-1
        
        k = '('+str(buy)+' '+str(sell)+')'
        values.append(k)
    if values == []:
        print("No Profit")
    else:
        print(*values)
    
