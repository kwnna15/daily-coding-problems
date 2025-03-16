from bstdelete import TreeNode, Solution


def tree_to_list(root: TreeNode) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_tree(lst: list) -> TreeNode:
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


def test_example_1():
    root = list_to_tree([5, 3, 6, 2, 4, None, 7])
    key = 3
    sol = Solution()
    result = sol.delete(root, key)
    assert tree_to_list(result) in [
        [5, 4, 6, 2, None, None, 7],
        [5, 2, 6, None, 4, None, 7],
    ]


def test_example_2():
    root = list_to_tree([5, 3, 6, 2, 4, None, 7])
    key = 0
    sol = Solution()
    result = sol.delete(root, key)
    assert tree_to_list(result) == [5, 3, 6, 2, 4, None, 7]


def test_example_3():
    root = list_to_tree([])
    key = 0
    sol = Solution()
    result = sol.delete(root, key)
    assert tree_to_list(result) == []


def test_example_4():
    root = list_to_tree([1, None, 2])
    key = 1
    sol = Solution()
    result = sol.delete(root, key)
    assert tree_to_list(result) == [2]


def test_example_5():
    root = list_to_tree([1, None, 2])
    key = 2
    sol = Solution()
    result = sol.delete(root, key)
    assert tree_to_list(result) == [1]
