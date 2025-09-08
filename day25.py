class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    
    return helper(root, float('-inf'), float('inf'))
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# print(isValidBST(root))

# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)

# print(isValidBST(root)) 

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print(isValidBST(root)) 
