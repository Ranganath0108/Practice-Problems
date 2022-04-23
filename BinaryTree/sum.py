from parase import parse_tuple
from ListOftrees import *


def sum(root):
    if root is None:
        return 0
    return root.data+sum(root.left)+sum(root.right)

if __name__=="__main__":
    root=parse_tuple(tree1)
    print(sum(root))