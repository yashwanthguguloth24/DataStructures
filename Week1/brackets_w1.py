def ismatch(a,b):
    return a+b in ['()','[]','{}']

def isbalanced(str):
    stack = []
    for i,char in enumerate(str):
        if char in "[{(":
            stack.append([i+1,char])
        if char in "}])":
            if len(stack) == 0:
                return i+1

            elif ismatch(stack[-1][1],char):
                stack.pop()
                continue
            else:
                return i+1

    if len(stack) != 0:
        return stack[-1][0]
    return 'Success'

str = input()
print(isbalanced(str))
# (({})
