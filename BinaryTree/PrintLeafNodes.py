from parase import parse_tuple
from ListOftrees import *


def printleafNodes(root):
    if root is None:
        return
    if(root.left is None and root.right is None):
        print(root.data, end=" ")
        return
    if(root.left != None):
        printleafNodes(root.left)
    if(root.right != None):
        printleafNodes(root.right)


if __name__ == "__main__":
    root = parse_tuple(tree1)
    print(printleafNodes(root))
    root2 = parse_tuple(tree2)
    print(printleafNodes(root2))
