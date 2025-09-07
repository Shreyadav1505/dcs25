class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

def build_tree(arr):
    if not arr:
        return None
    nodes = [None if v is None else TreeNode(v) for v in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root, nodes

# arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
# arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
arr = [1, 2]

root, nodes = build_tree(arr)

p = None
q = None
# for node in nodes:
#     if node and node.val == 5:
#         p = node
#     if node and node.val == 1:
#         q = node
# for node in nodes:
#     if node and node.val == 5:
#         p = node
#     if node and node.val == 4:
#         q = node
for node in nodes:
    if node and node.val == 1:
        p = node
    if node and node.val == 2:
        q = node

lca = lowestCommonAncestor(root, p, q)
print(lca.val)
