from parase import parse_tuple
from ListOftrees import *
from height import height


def LevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        CurrentLevel(root, i)


def CurrentLevel(root, level,flag=1):
    if root is None:
        return 
    if level == 1:
        print(root.data, end=" ")
        return 
    elif level > 1 and flag==1:
        CurrentLevel(root.left, level-1)
        CurrentLevel(root.right, level-1)
    elif level > 1 and flag==0:
        CurrentLevel(root.right, level-1,0)
        CurrentLevel(root.left, level-1,0)
        


if __name__ == "__main__":
    root = parse_tuple(tree1)
    print(LevelOrder(root))
    root2=parse_tuple(tree2)
    print(LevelOrder(root2))
