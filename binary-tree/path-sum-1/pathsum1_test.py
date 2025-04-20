from pathsum1 import TreeNode, Solution


def test_example_1():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    sol = Solution()
    assert sol.has_sum(root, 22) == True


def test_example_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution()
    assert sol.has_sum(root, 5) == False


def test_example_3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    sol = Solution()
    assert sol.has_sum(root, 0) == False


def test_example_4():
    root = TreeNode(1)
    sol = Solution()
    assert sol.has_sum(root, 1) == True


def test_example_5():
    root = None
    sol = Solution()
    assert sol.has_sum(root, 0) == False
