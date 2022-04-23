from parase import parse_tuple
from ListOftrees import *


def size(node):
    if node is None:
        return 0
    return 1+size(node.left)+size(node.right)

if __name__=="__main__":
    root=parse_tuple(tree1)
    print(size(root))


