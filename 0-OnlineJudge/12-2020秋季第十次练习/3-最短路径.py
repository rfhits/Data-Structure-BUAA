# 【问题描述】给定一张图，一个起点和一个终点，寻找最短的路径
# 【输入形式】先输入一张图，然后输入起点和终点(大写字母表示，字典序)
# 【输出形式】最短路径长度
# 【样例输入】

# -1 2 3 4
# 2 -1 4 -1
# 3 4 -1 5
# 4 -1 5 -1
# B D

# 【样例输出】6



dic = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
       5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}


def fill(mat, dot, t):
    '''将dot接连的点，并且尚未被mark的点mark'''
    global n
    global mark
    for i in range(n):
        if(mat[dot][i] == 1) and (mark[i] == 0):
            mark[i] = t

s = input().split()
n = int(s[0])
start = s[1]

temp = 1
mat = []
mark = [0]*n

for i in range(n):      # init the matrix
    mat.append([])
    for j in range(n):
        mat[i].append(0)

for k in dic.keys():    # get start
    if dic[k] == start:
        start = k
        break

mark[k] = 1

for i in range(n):          # fill the matrix
    s = input()
    for j in s:
        if j in dic.values():
            for k in dic.keys():
                if dic[k] == j:
                    mat[i][k] = 1
                    break
            

