# 【问题描述】
# 给定一个二叉树，请输出其中序遍历。

# 【输入形式】
# 二叉树的层序遍历，每一层之前的None不省略。

# 【输出形式】
# 二叉树的中序遍历。

# 【样例输入】
# 1 2 3 4 5 6 7

# 【样例输出】
# 4 2 5 1 6 3 7


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


def traversal(node):
    """
    LDR
    """
    if node == None:
        return
    elif node.data == "None":
        return
    else:
        traversal(node.left)
    print(node.data, end=' ')
    traversal(node.right)


node_list = []
input_tree(node_list)
traversal(node_list[0])
