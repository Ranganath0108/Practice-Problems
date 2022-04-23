
from ListOftrees import *
from parase import parse_tuple


def isSumProperty(root):
    if root is None or root.left is None and root.right is None:
        return True
    else:
        if(root.left != None):
            leftData = root.left.data
        if(root.right != None):
            rightData = root.right.data
        if(root.data == leftData+rightData and isSumProperty(root.left) and isSumProperty(root.right)):
            return True
    return False


if __name__ == "__main__":
    root = parse_tuple(tree1)
    print(isSumProperty(root))
    root2 = parse_tuple(tree2)
    print(isSumProperty(root2))
