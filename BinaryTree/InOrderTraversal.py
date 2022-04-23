import imp
from parase import parse_tuple
from ListOftrees import *
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left)+[root.data]+inorder_traversal(root.right)


if __name__=="__main__":
    root=parse_tuple(tree1)
    print(inorder_traversal(root))