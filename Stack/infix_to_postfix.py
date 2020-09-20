def Infix_to_Postfix(s):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    stack = []
    out = ""
    for token in s:
        if token in "+-*/^":
            while len(stack) != 0 and stack[len(stack)-1] != '(' and precedence[token] <= precedence[stack[len(stack)-1]]:
                a = stack.pop()
                out = out + " " + a
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            a = None
            while len(stack) != 0 and a != "(":
                a = stack.pop()
                if a != "(":
                    out = out + " " + a

        else:
            out = out + " " + token

    while len(stack) != 0:
        a = stack.pop()
        out = out + " " + a

    print(out)


Infix_to_Postfix("a+(b*c)")
