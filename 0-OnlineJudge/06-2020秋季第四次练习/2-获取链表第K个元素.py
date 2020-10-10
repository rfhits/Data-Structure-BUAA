# 【问题描述】
# 本题输入、输出以及链表构建代码已经在模板写好，只需补全功能函数 getKthNumber，返回对应数值即可。
# 给定一个链表的头节点head，以及一个整数k，请返回链表中第k个元素的value。

# 【输入形式】
# 第一行是一串整数，空格分隔，代表链表元素
# 第二行是一个整数 k

# 【输出形式】
# 一个整数，代表第 k 个元素。

# 【样例输入】
# 1 2 3 4 5
# 2

# 【样例输出】
# 2

# 【样例说明】
# 第二个元素是2


# A simple definition of linked Node.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = None

# Read list of data and construct linked list
raw_values = input()
last = None
for value in [int(x) for x in raw_values.split()]:
    node = Node(value)
    if head is None:
        head = node
    else:
        last.next = node
    last = node

def getKthNumber(head, k):
    ''' Please complete this function below,
    and return a value as answer.'''
    cur = head          # cur means current node
    for i in range(k-1):
        cur = cur.next
    return cur.value


k = int(input())
result = getKthNumber(head, k)
print(result)
