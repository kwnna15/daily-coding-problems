class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, curr_max):
    if not root:
        return 0
    good = 1 if root.val >= curr_max else 0
    curr_max = max(curr_max, root.val)
    return good + dfs(root.left, curr_max) + dfs(root.right, curr_max)


def count(root: TreeNode) -> int:
    return dfs(root, float("-inf"))
