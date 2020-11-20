'''
iven a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is String str.

Output:
Print length of smallest substring with maximum number of distinct characters.
Note: The output substring should have all distinct characters.

Constraints:
1 ≤ T ≤ 100
1 ≤ size of str ≤ 10000

Example:
Input:
2
abababcdefababcdab
geeksforgeeks

Output:
6
7
'''


def Distinct(S):
    d = [-1]*256
    curr_len = 0
    max_len = 0
    i = 0
    for j in range(len(S)):
        i = max(i,d[ord(S[j])]+1)
        max_len = max(max_len,j-i+1)
        d[ord(S[j])] = j
        
        
    return max_len
    
for _ in range(int(input())):
    S = input()
    print(Distinct(S))
    
    
    
