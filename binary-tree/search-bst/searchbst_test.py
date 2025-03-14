from searchbst import TreeNode, Solution


def test_example_1():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    sol = Solution()
    result = sol.search(root, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3


def test_example_2():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    sol = Solution()
    result = sol.search(root, 5)
    assert result is None


def test_example_3():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    sol = Solution()
    result = sol.search(root, 7)
    assert result.val == 7
    assert result.left is None
    assert result.right is None


def test_example_4():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    sol = Solution()
    result = sol.search(root, 1)
    assert result.val == 1
    assert result.left is None
    assert result.right is None


def test_example_5():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    sol = Solution()
    result = sol.search(root, 4)
    assert result.val == 4
    assert result.left.val == 2
    assert result.right.val == 7
