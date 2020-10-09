# 请基于 list 实现一个栈，并根据用例输入，模拟出入栈过程，并输出对应的结果。
# 【输入形式】
# 第一行输入数n，接下来n行输入一些数，表示已经在栈里的数
# 接下来输入数m，接下来m行输入指令，A表示入栈，B表示出栈，具体看样例

# 【输出形式】
# 第一行输出弹出栈的数字们，用空格隔开
# 第二行弹出栈内剩余的数，并用空格隔开

# 【样例输入】
# 3
# 1
# 2
# 3
# 5
# A 5
# A 6
# B
# B
# B

# 【样例输出】
# 6 5 3
# 2 1

# 【样例说明】
# 如果出现异常，输出一行‘No’
# 【评分标准】

# 请用list实现

import sys
n = int(input())
stack = []
out = []
for i in range(n):
    stack.append(input())
m = int(input())
for i in range(m):
    ask = input().split()
    if ask[0] == 'A':
        stack.append(ask[1])
    elif ask[0] == 'B':
        if len(stack) == 0:
            print('No')
            sys.exit(0)
        else:
            out_num = stack.pop()
            out.append(out_num)

for i in out:
    print(i, end=' ')
print('')
stack.reverse()
for i in stack:
    print(i, end=' ')
