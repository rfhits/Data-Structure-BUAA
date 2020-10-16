# 【问题描述】
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到 B ，就返回 True ；否则返回 False 。

# 【输入形式】
# 两行输入，分别为字符串A、B

# 【输出形式】
# True 或 False

# 【样例输入】
# aaaaaaabc
# aaaaaaacb

# 【样例输出】
# True

# 【样例说明】
# 交换后两个字符后 A 与 B 一致

# 【评分标准】
# 请注意 "ab" 和 "ab" 不是亲密字符串，因为交换 A 仅有的两个字符后与 B 并不一致

# 【分析】
# 这两个字符串不一样的字符数
# 情况一：>= 3个 --> GG
# 情况二：== 2个 --> 尝试互换再比较
# 情况三：== 1个 --> GG
# 情况四：== 0个 --> 具体分析

import collections as cs
import sys
p = 0   # 默认不匹配
a = list(input())
b = list(input())
m, n = len(a), len(b)
lst = []
if m != n:      # 两个字符串等长吗
    print("False")
    sys.exit(0)
for i in range(m):
    if a[i] == b[i]:
        pass
    else:
        lst.append(i)
if len(lst) == 0:   # a字符串 和 b字符串相等
    dic = dict(cs.Counter(a))
    for i in dic.values():
        if i >= 2:
            p = 1
elif len(lst) == 2:
    t = a[lst[0]]
    a[lst[0]] = a[lst[1]]
    a[lst[1]] = t
    p = (a==b)
else:
    pass
print(p==1)
