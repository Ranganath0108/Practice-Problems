from ListOftrees import *
from parase import parse_tuple


def VerticalOrder_traversal(root):
    m = dict()
    hd = 0
    res = []
    getVerticalOrder(root, hd, m)

    for i in sorted(m):
        res.append({i: m[i]})
    return res


def getVerticalOrder(root, hd, m):
    if root is None:
        return
    try:
        m[hd].append(root.data)
    except:
        m[hd] = [root.data]
    getVerticalOrder(root.left, hd-1, m)
    getVerticalOrder(root.right, hd+1, m)


if __name__ == "__main__":
    root = parse_tuple(tree1)
    print(VerticalOrder_traversal(root))
    root2=parse_tuple(tree2)
    print(VerticalOrder_traversal(root2))
