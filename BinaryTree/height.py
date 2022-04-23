from parase import parse_tuple

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))

root=parse_tuple(((4,2,5),1,(None,3,None)))

if __name__=="__main__":
    print(height(root))







