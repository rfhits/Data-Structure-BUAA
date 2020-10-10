# 【问题描述】
# 给定两个形状相同的N阶方阵，A和B，请输出A中多少元素比B中对应位置的元素大，即A[i][j] > B[i][j]。
# 要求：请用 numpy 库实现，请用 numpy 库实现，请用 numpy 库实现
# 通过一个simple的二重循环可以很容易实现算法，但是你可以用更方便的numpy来操作矩阵吗？

# 【输入形式】
# 第一行一个整数N
# 接下来的2~N+1行，每行有N个整数，代表方阵A每一行的元素
# 接下来的N+2~2N+1行，每行有N个整数，代表方阵B每一行的元素

# 【输出形式】
# 一个整数，表示一共有多少位置(i, j)满足A[i][j] > B[i][j]。

# 【样例输入】
# 3
# 6 8 3
# 1 4 7
# 5 8 4
# 7 8 7
# 4 7 8
# 0 9 6

# 【样例输出】
# 1

import numpy as np
n = int(input())
temp = []
for i in range(n):
    temp.extend(input().split())
a = [int(num) for num in temp]
temp.clear()
for i in range(n):
    temp.extend(input().split())
b = [int(num) for num in temp]
array_a = np.array(a)
array_b = np.array(b)
array_c = array_a-array_b
low = 0
for i in array_c:
    if i > 0:
        low = low+1
print(low)
