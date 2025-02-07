from leafsimilar import leaf_similar, TreeNode

def test_example_1():
    root1 = TreeNode(3, 
                     TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), 
                     TreeNode(1, TreeNode(9), TreeNode(8)))
    root2 = TreeNode(3, 
                     TreeNode(5, TreeNode(6), TreeNode(7)), 
                     TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    assert leaf_similar(root1, root2) == True

def test_example_2():
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(3), TreeNode(2))
    assert leaf_similar(root1, root2) == False

def test_example_3():
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert leaf_similar(root1, root2) == True

def test_example_4():
    root1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))
    assert leaf_similar(root1, root2) == False

def test_example_5():
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    assert leaf_similar(root1, root2) == True
