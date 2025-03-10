from zigzag import TreeNode, Solution


def test_example_1():
    root = TreeNode(TreeNode(None, TreeNode(TreeNode(None, TreeNode()))), TreeNode())
    sol = Solution()
    assert sol.longest(root) == 4


def test_example_2():
    root = TreeNode(TreeNode(TreeNode(TreeNode(TreeNode(TreeNode())))))
    sol = Solution()
    assert sol.longest(root) == 1


def test_example_3():
    root = TreeNode(
        TreeNode(TreeNode(TreeNode(TreeNode(TreeNode())))),
        TreeNode(TreeNode(TreeNode(TreeNode(TreeNode(TreeNode()))))),
    )
    sol = Solution()
    assert sol.longest(root) == 2


def test_example_4():
    root = TreeNode(
        TreeNode(TreeNode(TreeNode(TreeNode(TreeNode())))),
        TreeNode(TreeNode(TreeNode(TreeNode(TreeNode(TreeNode()))))),
    )
    sol = Solution()
    assert sol.longest(root) == 2


def test_example_5():
    root = TreeNode(
        TreeNode(TreeNode(TreeNode(TreeNode(TreeNode())))),
        TreeNode(TreeNode(TreeNode(TreeNode(TreeNode(TreeNode()))))),
    )
    sol = Solution()
    assert sol.longest(root) == 2
