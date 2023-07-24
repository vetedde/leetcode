# Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(nums):
    i = 0
    l = len(nums)
    tree = TreeNode(val=nums[0])
    stack = [tree]
    while stack:
        node = stack.pop(0)
        if i + 1 < l:
            left_node = TreeNode(val=nums[i + 1])
            node.left = left_node
            stack.append(left_node)

        if i + 2 < l:
            right_node = TreeNode(val=nums[i + 2])
            node.right = right_node
            stack.append(right_node)

        i += 2

    return tree
def inorderTraversal(node):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    left = []
    right = []
    if node.left:
        left = inorderTraversal(node.left)

    if node.right:
        right = inorderTraversal(node.right)
    return left + [node.val] + right

def inorderTraversal_1(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right


tree = createTree([1,2,3,4,5,6,7,8,9,10])
print(inorderTraversal(tree))