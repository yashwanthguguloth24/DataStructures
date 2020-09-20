def prefix(arr):
    stack = []
    for item in arr[::-1]:
        if item == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 * n2)

        elif item == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 // n1)

        elif item == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)

        elif item == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 + n2)


        else:
            stack.append(int(item))

    print(stack.pop())

prefix(['*','+','2','3','5'])
