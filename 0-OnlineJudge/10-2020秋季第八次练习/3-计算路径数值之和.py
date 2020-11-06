ans = 0


class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


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


def cnt(node, n):
    if node == None:
        return
    if node.data == "None":
        return
    if is_leaf(node):
        i = n*10 + int(node.data)
        global ans
        ans += i
        return
    i = n*10 + int(node.data)
    cnt(node.left, i)
    cnt(node.right, i)


def is_leaf(node):
    a1 = (node.left == None)
    if(node.left):
        a2=(node.left.data == "None")
        a1 = a1 or a2
    b1=(node.right == None)
    if(node.right):
        b2 = (node.right.data == "None")
        b1 = b1 or  b2
    return a1 and b1


node_list = []
input_tree(node_list)
cnt(node_list[0], 0)
print(ans)
