# 【问题描述】
# 本题输入、输出以及链表构建代码已经在模板写好，只需补全功能函数 getLastKthNumber，返回对应数值即可。
# 给定一个链表的头节点head，以及一个整数k，请返回链表中倒数第k个元素的value。

# 【输入形式】
# 第一行是一串整数，空格分隔，代表链表元素
# 第二行是一个整数 k

# 【输出形式】
# 一个整数，代表倒数第 k 个元素。

# 【样例输入】
# 1 2 3 4 5
# 2

# 【样例输出】
# 4

# 【样例说明】
# 倒数第二个元素是4



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

# Don't modify code above.


def getLastKthNumber(head, k):

# your code here

    p1 = head
    p2 = head
    for i in range(k):
        p1 = p1.next
    while (p1):
        p1 = p1.next
        p2 = p2.next

    return p2.value

# Don't modify code below.


# Evaluate result returned from your function
k = int(input())
result = getLastKthNumber(head, k)
print(result)
