res = []
stack =[]
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def isN(node):
    if node == None:
        return True
    elif node.data == 'None':
        return True
    else:
        return False


def input_tree(node_list):
    ''' input the data by the layer, make a tree, the root is stored in node_list[0]'''

    input_list = input().split()
    l = len(input_list)
    node_list.append(Node(input_list[0]))
    for i in range(1, l):
        node = Node(input_list[i])
        node_list.append(node)
        if i % 2 == 1:
            k = (i-1)//2
            node_list[k].left = node
        else:
            k = (i-2)//2
            node_list[k].right = node

def tra(node):
    t = node
    while  (not isN(t) ) or stack:
        if not isN(t):
            stack.append(t)
            t =t.left
        else:
            t = stack[-1]
            stack.pop()
            res.append(t.data)
            t =t.right

node_list = []
input_tree(node_list)
tra(node_list[0])
print(' '.join(res))