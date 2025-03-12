from rightside import TreeNode, Solution


def test_example_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    sol = Solution()
    assert sol.view(root) == [1, 3, 4]


def test_example_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    sol = Solution()
    assert sol.view(root) == [1, 3, 5]


def test_example_3():
    root = TreeNode(1)
    root.right = TreeNode(3)
    sol = Solution()
    assert sol.view(root) == [1, 3]


def test_example_4():
    root = TreeNode(1)
    sol = Solution()
    assert sol.view(root) == [1]


def test_example_5():
    root = None
    sol = Solution()
    assert sol.view(root) == []
