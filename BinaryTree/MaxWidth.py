from parase import parse_tuple
from height import height
from ListOftrees import *


def maxWidth(root):
    maxW = 0
    h = height(root)
    for i in range(1, h+1):
        width = getWidth(root, i)
        maxW = max(width, maxW)
    return maxW


def getWidth(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return getWidth(root.left, level-1)+getWidth(root.right, level-1)


if __name__ == "__main__":
    root = parse_tuple(tree1)
    print(maxWidth(root))
    root2 = parse_tuple(tree2)
    print(maxWidth(root2))
