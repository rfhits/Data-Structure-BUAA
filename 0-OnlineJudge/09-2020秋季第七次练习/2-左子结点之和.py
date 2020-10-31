# 【问题描述】
# 计算给定二叉树的所有左子结点之和。

# 【输入形式】
# 一行，包含用空格分开的n个元素，每个元素为整数或者None（None表示空结点），依次表示按层次遍历的二叉树结点。

# 【输出形式】
# 一个整数，表示所有左子结点之和。

# 【样例输入】
# 1 2 3 4 5

# 【样例输出】
# 6

# 【样例说明】
# 左子结点为2和4

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_in(node_list):
    list_in = input().split()
    l = len(list_in)
    node_list.append(Node(list_in[0]))
    for i in range(1, l):
        if list_in[i] == "None":
            node_list.append(None)
        else:
            new_node = Node(list_in[i])
            node_list.append(new_node)
            if(i % 2 == 1):
                k = (i-1)//2
                while(node_list[k] == None):
                    k += 1
                node_list[k].left = new_node
            else:
                k = (i-2)//2
                while (node_list[k] == None):
                    k += 1
                node_list[k].right = new_node


node_list = []
tree_in(node_list)
ans = 0
for i in node_list:
    if(i == None):
        pass
    elif(i.left == None):
        pass
    else:
        ans += int(i.left.data)
print(ans)
