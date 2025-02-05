import sys


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


if __name__ == "__main__":
    rightleft = TreeNode(None, None)
    rightright = TreeNode(None, None)
    left = TreeNode(None, None)
    right = TreeNode(rightleft, rightright)
    root = TreeNode(left, right)
    print(max_depth(root))
