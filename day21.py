stack = [1, 2, 3, 4]
stack = [3, 2, 1]
stack = [5]
stack = [-5, -10, -15]
stack = []
stack = [3, 3, 3]

def reverse(stack):
    if not stack:
        return
    x = stack.pop()
    reverse(stack)
    def put_bottom(stack, x):
        if not stack:
            stack.append(x)
            return
        y = stack.pop()
        put_bottom(stack, x)
        stack.append(y)
    put_bottom(stack, x)

reverse(stack)
print(stack)
