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
# 注：-1表示无连接

ans = []
temp = 0
dic = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
       5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}


def get_key(dic, val):
    for k in dic.keys():
        if dic[k] == val:
            return k


def tra(mat, ver, end):
    '''找到从ver到end的路径，并且走下去'''
    global ans
    global temp
    global tail
    global n
    global mark
    if ver == end:
        ans.append(temp)
        return
    else:
        for i in range(n):
            if(mark[i] == 0) and (mat[ver][i] >= 0):
                temp += mat[ver][i]
                mark[i] = 1
                tra(mat, i, tail)
                temp -= mat[ver][i]
                mark[i] = 0


s = input().split()
s = [int(i) for i in s]
n = len(s)
mat = []
mark = [0]*n
for i in range(n):      # init the matrix
    mat.append([])
    for j in range(n):
        mat[i].append(0)

for i in range(n):      # the first line of matrix
    mat[0][i] = s[i]
for i in range(1, n):   # the other lines of matrix
    s = input().split()
    s = [int(i) for i in s]
    for j in range(n):
        mat[i][j] = s[j]

s = input().split()
head = get_key(dic, s[0])
tail = get_key(dic, s[1])
mark[head] = 1
tra(mat, head, tail)
print(min(ans))
