
from parase import parse_tuple
from ListOftrees import *


def post_order(root):
    if root is None:
        return  []
    return post_order(root.left)+post_order(root.right)+[root.data]

if __name__=="__main__":
    root=parse_tuple(tree1)
    print(post_order(root))