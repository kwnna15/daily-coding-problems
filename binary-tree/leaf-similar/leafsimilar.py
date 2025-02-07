import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, leafs):
    if not root:
        return
    dfs(root.left, leafs)
    if not root.left and not root.right:
        leafs.append(root.val)
    dfs(root.right, leafs)


def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
    v1 = []
    v2 = []
    dfs(root1, v1)
    dfs(root2, v2)
    return v1 == v2
