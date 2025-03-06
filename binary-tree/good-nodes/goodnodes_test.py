from goodnodes import TreeNode, count


def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    assert count(root) == 4


def test_example_2():
    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    assert count(root) == 3


def test_example_3():
    root = TreeNode(1)
    assert count(root) == 1


def test_example_4():
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert count(root) == 6


def test_example_5():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    assert count(root) == 5
