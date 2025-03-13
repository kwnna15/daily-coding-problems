from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1

        def BFS(root):
            q = deque([root])
            maximum = []
            maximum.append(root.val)
            while q:
                l = len(q)
                value = 0
                for i in range(l):
                    temp_root = q.popleft()
                    if temp_root.left:
                        q.append(temp_root.left)
                        value += temp_root.left.val
                    if temp_root.right:
                        q.append(temp_root.right)
                        value += temp_root.right.val
                print(maximum)
                maximum.append(value)
            maximum.pop()
            return maximum.index(max(maximum)) + 1

        return BFS(root)
