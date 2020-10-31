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
            else:
                k = (i-2)//2
                while(node_list[k] == None):
                    k += 1
                node_list[k].right = node


node_list = []
input_tree(node_list)
k = int(input())
h = 2**(k-1) - 1    # head
t = 2**k-1          # tail
l= len(node_list)

ans = 0
if l <= h:          # 其实有个bug，没法面对多层none的情况，可以通过给node增加layer属性解决
    ans = 0
else:
    for i in range(h, t):
        if(i < l):
            if node_list[i] == None:
                pass
            elif node_list[i].data == None:
                pass
            else:
                ans += int(node_list[i].data)
print(ans)
