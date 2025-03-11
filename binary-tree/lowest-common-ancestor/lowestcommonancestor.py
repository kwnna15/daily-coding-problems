import sys


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class Solution:
    def lca(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        left_lca = self.lca(root.left, p, q)
        right_lca = self.lca(root.right, p, q)

        if left_lca and right_lca:
            return root
        if left_lca:
            return left_lca
        
        return right_lca
