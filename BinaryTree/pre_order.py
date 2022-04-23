from parase import parse_tuple
from ListOftrees import *

def pre_orderTraversal(root):
    if root is None:
        return []
    return [root.data]+pre_orderTraversal(root.left)+pre_orderTraversal(root.right)


if __name__=="__main__":
    root=parse_tuple(tree1)
    print(pre_orderTraversal(root))