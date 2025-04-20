from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, curr_sum, target_sum, count):
    if not node:
        return 0

    curr_sum += node.val
    curr_count = count[curr_sum - target_sum]

    count[curr_sum] += 1

    curr_count += dfs(node.left, curr_sum, target_sum, count)
    curr_count += dfs(node.right, curr_sum, target_sum, count)

    count[curr_sum] -= 1
    if count[curr_sum] == 0:
        del count[curr_sum]

    return curr_count


def sum(root: TreeNode, target_sum: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    return dfs(root, 0, target_sum, count)
