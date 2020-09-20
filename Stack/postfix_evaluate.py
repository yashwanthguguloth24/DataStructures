'''
Given a postfix expression, the task is to evaluate the expression and print the final value. Operators will only include the basic arithmetic operators like *,/,+ and - . 

Input:
The first line of input will contains an integer T denoting the no of test cases . Then T test cases follow. Each test case contains an postfix expression.

Output:
For each test case, in a new line, evaluate the postfix expression and print the value.

Constraints:
1 <= T <= 100
1 <= length of expression <= 100

Example:
Input:
2
231*+9-
123+*8-
Output:
-4
-3
'''

def postfix(arr):
    stack = []
    for item in arr:
        if item == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1*n2)
            
        elif item == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2//n1)
            
        elif item == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
            
        elif item == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1+n2)
            
            
        else:
            stack.append(int(item))
            
    print(stack.pop())
            
for _ in range(int(input())):
    arr = list(map(str, input()))
    postfix(arr)
    
