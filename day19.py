expression = "2 1 + 3 *"
expression = "5 6 +"
expression = "3 4 2 * 1 5 - 2 3 ^ ^ / +"
expression = "-5 6 -"
expression = "15 7 1 1 + - / 3 * 2 1 1 + + -"
expression = "5"

stack = []
tokens = expression.split()

for token in tokens:
    if token.lstrip('-').isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        elif token == '/':
            stack.append(int(a / b))

return stack[0]

