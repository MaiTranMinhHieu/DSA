def evalRPN(tokens) -> int:
    stack = []
    for t in tokens:
        if t not in "+-*/":
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == '+': stack.append(l + r)
            elif t == '-': stack.append(l - r)
            elif t == '*': stack.append(l * r)
            else: stack.append(int(l / r))
    return stack[0]

tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))