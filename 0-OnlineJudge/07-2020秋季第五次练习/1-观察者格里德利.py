# 【问题描述】格里德利很喜欢寻找事物间的相似处，请帮她找找字符串中最长的公共前缀
# 【输入形式】第一行输入一个数N，表示字符串个数，接下来N行每行输入一个字符串
# 【输出形式】匹配到的最长前缀，如果没有则输出No

# 【样例输入】
# 3
# car
# career
# cat

# 【样例输出】
# ca

# 【样例说明】何も言わない
# 【评分标准】無し

import sys
n = int(input())
lst = []
min_len = -1
for i in range(n):
    s = input()
    if len(s) == 0:     # 输入空字符串，直接停止
        print('No')
        sys.exit(0)
    if min_len == -1:
        min_len = len(s)
    if min_len > len(s):
        min_len = len(s)
    lst.append(s)
have = 0                        # 这些字符串有没有公共的前缀呢？默认没有
for i in range(min_len):     # 第i个字符
    p = lst[0][i]
    flag = 1                  # 默认是相同的
    for j in range(1, n):      # 遍历所有的字符串的 j 索引
        if p == lst[j][i]:
            pass
        else:
            flag = 0
            break
    if flag == 1:
        print(p, end='')
        have = 1
if have == 0:               # 这些字符串没有公共前缀
    print('No')
