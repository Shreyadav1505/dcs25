def isSymmetricTree(values):
    if not values: return True

    def mirror(i, j):
        if i >= len(values) and j >= len(values): return True
        if i >= len(values) or j >= len(values): return False
        if values[i] != values[j]: return False
        return mirror(2*i+1, 2*j+2) and mirror(2*i+2, 2*j+1)

    return mirror(1, 2)

print(isSymmetricTree([1, 2, 2, 3, 4, 4, 3]))
# print(isSymmetricTree([1, 2, 2, null, 3, null, 3]))
# print(isSymmetricTree([1]))
# print(isSymmetricTree([]))
# print(isSymmetricTree([1, 2, 2, 3, null, null, 3]))
