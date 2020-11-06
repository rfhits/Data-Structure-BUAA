# 【问题描述】
# 给定一棵二叉树，一条路径的数值指的是从根节点到叶子节点的十进制数字表示。保证节点的数值不会超过10。
# 例如1 -> 3 -> 5 -> 2 这条路径的数值则为1352。请求出该二叉树全部路径的数值之和。

# 【输入形式】
# 同上题，二叉树的完全二叉树式的层次遍历。

# 【输出形式】
# 一个整数，代表路径数值之和。

# 【样例输入】
# 1 2 3 4 None 6 7

# 【样例输出】
# 397

# 【样例说明】

#        1
#     2    3
#   4  N  6  7

# 124 + 136 + 137 = 397

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
    elif node.data == "None":
        return
    elif is_leaf(node):
            i = n*10 + int(node.data)
            global ans
            ans += i
            return
    else:
        i = n*10 + int(node.data)
        cnt(node.left, i)
        cnt(node.right, i)


def is_leaf(node):
    """"是不是叶子节点啊"""
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
