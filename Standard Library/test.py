def test(exp):
    ops = ['+', '-', '*', '/']
    prec = {"+": 0, "-": 0, "*": 1, "/": 1, '(': -1}
    output = []
    stack = []

    for atom in exp:
        if atom in ops:
            while stack and prec[stack[-1]] >= prec[atom]:
                output.append(stack.pop())
            stack.append(atom)
        elif atom == '(':
            stack.append('(')
        elif atom == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(atom)
    while stack:
        output.append(stack.pop())

    return output
arr = '2 + 3 - 5'.split()
print(test(arr))