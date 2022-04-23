from parase import parse_tuple
from ListOftrees import *
from height import height
from LevelOrderTraversal import CurrentLevel


def zigZagTravesal(root):
    h=height(root)
    for i in range(1,h+1):
        CurrentLevel(root,i,i%2)


if __name__ == "__main__":
    root = parse_tuple(tree1)
    print(zigZagTravesal(root))
    root2=parse_tuple(tree2)
    print(zigZagTravesal(root2))
