import pytest
from maxdepth import max_depth, TreeNode


def test_example_1():
    root = TreeNode(TreeNode(), TreeNode(TreeNode(), TreeNode()))
    assert max_depth(root) == 3


def test_example_2():
    root = TreeNode(None, TreeNode())
    assert max_depth(root) == 2


def test_example_3():
    root = None
    assert max_depth(root) == 0


def test_example_4():
    root = TreeNode()
    assert max_depth(root) == 1


def test_example_5():
    root = TreeNode(TreeNode(TreeNode(TreeNode(TreeNode()))))
    assert max_depth(root) == 5
