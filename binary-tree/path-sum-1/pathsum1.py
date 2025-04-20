class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_sum(self, root: TreeNode, target_sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return target_sum == root.val
        left_sum = self.has_sum(root.left, target_sum - root.val)
        right_sum = self.has_sum(root.right, target_sum - root.val)
        return left_sum or right_sum
