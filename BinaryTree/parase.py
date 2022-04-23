
from Node import Node


def parse_tuple(data):
    if(isinstance(data, tuple) and len(data) == 3):
        node = Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    return node
