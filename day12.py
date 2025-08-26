
# s = "({[})"
# s = "{[}"
# s = ""
# s = "()"
# s = "([)]"
# s = "[{()}]"
s = "({}[{}])"
def isvalid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            return False
    return not stack
print(isvalid(s))
