# 【问题描述】
# 给定一棵二叉树，求树中全部第k层的节点之和。

# 【输入形式】
#  第一行，包含用空格分开的n个元素，每个元素为整数或者None（None表示空结点），依次表示按自顶向下层次遍历的二叉树结点。
# 第二行，一个整数 k。

# 【输出形式】
# 一个整数代表对应节点之和。如果树中最大深度依然小于k，则返回0。

# 【样例输入】
# 1 2 3 None None 4 5 6
# 2

# 【样例输出】
# 5

# 【样例说明】
# 如图所示，第二层只有两个节点2和3。

class Node():
    def __init__(self, data=None, left=None, right=None, layer=None):
        self.data = int(data)
        self.left = left
        self.right = right
        self.layer = layer  # 在原来的基础上，增加了layer这一属性


def input_tree(node_list):
    ''' input the data layer by layer, make a tree, the root is stored in node_list[0]'''

    input_list = input().split()
    l = len(input_list)
    node_list.append(Node(input_list[0]))
    node_list[0].layer = 1
    for i in range(1, l):
        if input_list[i] == "None":
            node_list.append(None)
        else:
            node = Node(input_list[i])
            node_list.append(node)
            if i % 2 == 1:
                k = (i-1)//2
                while(node_list[k] == None):
                    k += 1
                node_list[k].left = node
                node_list[i].layer = node_list[k].layer+1   # 补上layer
            else:
                k = (i-2)//2
                while(node_list[k] == None):
                    k += 1
                node_list[k].right = node
                node_list[i].layer = node_list[k].layer+1   # 补上layer


node_list = []
input_tree(node_list)
k = int(input())
ans = 0
for i in node_list: # 对node_list进行遍历，选出其中layer符合要求的node
    if i == None:
        continue
    else:
        if i.layer == k:
            ans += i.data
print(ans)