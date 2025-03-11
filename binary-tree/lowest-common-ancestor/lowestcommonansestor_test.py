from lowestcommonancestor import TreeNode, Solution


def test_example_1():
    root = TreeNode(TreeNode(TreeNode(), TreeNode()), TreeNode(TreeNode(), TreeNode()))
    p = root.left
    q = root.right
    sol = Solution()
    assert sol.lca(root, p, q) == root


def test_example_2():
    root = TreeNode(TreeNode(TreeNode(), TreeNode()), TreeNode(TreeNode(), TreeNode()))
    p = root.left.left
    q = root.left.right
    sol = Solution()
    assert sol.lca(root, p, q) == root.left


def test_example_3():
    root = TreeNode(TreeNode(TreeNode(), TreeNode()), TreeNode(TreeNode(), TreeNode()))
    p = root.left.left
    q = root.right.right
    sol = Solution()
    assert sol.lca(root, p, q) == root


def test_example_4():
    root = TreeNode(TreeNode(TreeNode(), TreeNode()), TreeNode(TreeNode(), TreeNode()))
    p = root.left.left
    q = root.left
    sol = Solution()
    assert sol.lca(root, p, q) == root.left


def test_example_5():
    root = TreeNode(TreeNode(TreeNode(), TreeNode()), TreeNode(TreeNode(), TreeNode()))
    p = root.left.left
    q = root.left.left
    sol = Solution()
    assert sol.lca(root, p, q) == root.left.left
