# 【问题描述】
# 给定一个10进制数，将其转换为任意的进制数（不会出现17进制或以上）
# 【输入形式】
# 输入两个数M,N，其中M表示需要被转换的10进制数，N表示给定的进制，中间用空格隔开
# 【输出形式】
# M的N进制表示，如遇到字母请使用大写

# 【样例输入】
# 16 2

# 【样例输出】
# 10000

# 【样例说明】这就不用我多说了8
# 【评分标准】这也不用我多说了8

s = [int(i) for i in input().split()]
num = s[0]
b = s[1]
bits = []
while(num != 0):
    bits.append(num % b)
    num = num // b
bits.reverse()
for i in bits:
    if i >= 10:
        print(chr(ord('A')+i-10),end='')
    else:
        print(i,end='')


# for i in bits:
#     if i == 10:
#         print('A', end='')
#     elif i == 11:
#         print('B', end='')
#     elif i == 12:
#         print('C', end='')
#     elif i == 13:
#         print('D', end='')
#     elif i == 14:
#         print('E', end='')
#     elif i == 15:
#         print('F', end='')
#     else:
#         print(i, end='')
