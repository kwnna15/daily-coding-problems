class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delete(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key > root.val:
            root.right = self.delete(root.right, key)
        elif key < root.val:
            root.left = self.delete(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.delete(root.right, cur.val)
        return root
