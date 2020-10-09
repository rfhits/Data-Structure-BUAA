# 现在请你打印一个n阶单位矩阵。

# 【输入形式】
# 一行整数n (0 < n <= 10)

# 【输出形式】
# 输出该n阶单位矩阵，每个元素之间用空格分隔

# 【样例输入】
# 3

# 【样例输出】
# 1 0 0
# 0 1 0
# 0 0 1

s = int(input())


def prilin(s, j):
    for i in range(s):
        if i == j:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print('')
    return


for i in range(s):
    prilin(s, i)
