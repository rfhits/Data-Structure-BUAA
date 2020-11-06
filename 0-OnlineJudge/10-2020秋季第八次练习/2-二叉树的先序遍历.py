# 【问题描述】
# 如上题，按照完全二叉树的格式，依次输入一个二叉树每一层的节点。请先建树之后，按照先序遍历输出全部节点的value。
# 空结点None不用输出。

# 【输入形式】
# 同上题，按照层次遍历二叉树的全部节点，空格分隔。

# 【输出形式】
# 先序遍历的二叉树节点，空格分隔。

# 【样例输入】
# 1 None 3 None None 4 5 None None None None 6 7 8 9

# 【样例输出】
# 1 3 4 6 7 5 8 9

# 【样例说明】
# 这应该很简单吧，白送分

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
    DLR
    """
    if node == None:
        return
    elif node.data == "None":
        return
    else:
        print(node.data, end=' ')
    traversal(node.left)
    traversal(node.right)


node_list = []
input_tree(node_list)
traversal(node_list[0])
