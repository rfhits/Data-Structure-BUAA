# 【问题描述】在一个网络里有若干节点，假设每两个节点间通信需要的时间为1，现在给某个节点发送信号，多长时间后，网络里所有节点都能收到该信号
# 【输入形式】第一行输入节点个数和开始初始节点
# 【输出形式】一个数
# 【样例输入】

# 7 C
# A: {B:1, C:1, D:1, G:1}
# B: {A:1, C:1, D:1}
# C: {A:1, B:1, F:1}
# D: {A:1, B:1}
# E: {F:1}
# F: {C:1, E:1, G:1}
# G: {A:1, F:1}

# 【样例输出】2

# 可以看成一种“传播方式”，
# 比如A被“激发”，下一次激发的就是A接连的点
# 将所有点激发要几次，相当于画圈圈

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
            

t = 1
lst = []

while(0 in mark):
    lst = [i for i in list(range(n)) if mark[i] != 0]       # 要激发的点
    for i in lst:
        fill(mat, i, t)
    t += 1
    lst = []

t -= 1
print(t)
