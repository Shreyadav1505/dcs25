def sortStack(stack):
    if not stack or len(stack) == 1:
        return

    top = stack.pop()

    sortStack(stack)

    insertInSortedOrder(stack, top)


def insertInSortedOrder(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    top = stack.pop()
    insertInSortedOrder(stack, element)
    
    stack.append(top)

stack1 = [3, 1, 4, 2]
sortStack(stack1)
print(stack1)

stack2 = [7, 1, 5]
sortStack(stack2)
print(stack2)

stack3 = [5]
sortStack(stack3)
print(stack3)

stack4 = [-3, 14, 8, 2]
sortStack(stack4)
print(stack4)

stack5 = []
sortStack(stack5)
print(stack5)

stack6 = [3, 3, 3]
sortStack(stack6)
print(stack6)
