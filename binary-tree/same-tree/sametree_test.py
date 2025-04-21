from sametree import TreeNode, Solution


def test_example_1():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    assert sol.same(p, q) == True


def test_example_2():
    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(2)

    sol = Solution()
    assert sol.same(p, q) == False


def test_example_3():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    sol = Solution()
    assert sol.same(p, q) == False


def test_example_4():
    p = None
    q = None

    sol = Solution()
    assert sol.same(p, q) == True


def test_example_5():
    p = TreeNode(1)
    q = None

    sol = Solution()
    assert sol.same(p, q) == False
