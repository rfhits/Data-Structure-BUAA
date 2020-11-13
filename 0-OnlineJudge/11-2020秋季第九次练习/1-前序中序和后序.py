# 【问题描述】你现在知道一个二叉树的前序遍历和中序遍历，请输出它的后序遍历。无相同元素。
# 【输入形式】前序遍历和中序遍历
# 【输出形式】后序遍历
# 【样例输入】
# 1 2 3
# 1 3 2

# 【样例输出】
# 3 2 1

# 【样例说明】无
# 【评分标准】无


# head tail
def LRD(a_h, a_t, b_h, b_t):
    for i in range(b_h, b_t+1):
        if(a[a_h] == b[i]):
            LRD(a_h+1, a_h+i-b_h, b_h, i-1)
            LRD(a_h+i-b_h+1, a_t, i+1, b_t)
            print(b[i], end=' ')
            break


a = input().split()
b = input().split()
n = len(a)
LRD(0, n-1, 0, n-1)


# 解析：
# DLR: C A B G H E D F
# LDR: G H B A C D E F

# DLR中的第一个是root
# LDR中root的左边就是左树的节点，root的右边就是右树的节点
# 先找到root，是C

# DLR: C | A B G H | E D F
# LDR: G H B A | C | D E F

# C左边是 G H B A
# C右边是 D E F
# 这个左片段的“长度”，就是 i-b_h
# 通过“长度”，来确定要传入的参数


# 递归，把
# DLR中的 A B G H 和
# LDR中的 G H B A 传入

# A | B G H |
# G H B | A |


# 递归，把
# DLR中的 E D F 和
# LDR中的 D E F 传入


# 核心思想就是 分割-传入-最后print
#　如果还是看不懂，，无能为力聊
# 附上博客一篇：
# https://blog.csdn.net/Greek_to_me/article/details/81951057
