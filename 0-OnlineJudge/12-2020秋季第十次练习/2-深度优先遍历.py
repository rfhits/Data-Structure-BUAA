# 【问题描述】深度优先遍历
# 【输入形式】同上题
# 【输出形式】同上题
# 【样例输入】

# 4 A
# A: {B:1, C:1, D:1}
# B: {A:1, C:1, D:1}
# C: {A:1, B:1, D:1}
# D: {A:1, B:1, C:1}

# 【样例输出】
# A B C D

dic = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
       5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}

ans = []


def travelsal(mat, ver):
    global ans
    global n
    global mark
    ans.append(ver)
    for i in range(n):
        if(mat[ver][i] != 0) and (mark[i] == 0):
            mark[i] = 1
            travelsal(mat, i)


s = input().split()
n = int(s[0])
start = s[1]

mat = []
for i in range(n):      # init the matrix
    mat.append([])
    for j in range(n):
        mat[i].append(0)

for k in dic.keys():
    if dic[k] == start:
        start = k
        break

for i in range(n):          # fill the matrix
    s = input()
    for j in s:
        if j in dic.values():
            for k in dic.keys():
                if dic[k] == j:
                    mat[i][k] = 1
                    break
            


mark = [0]*n
mark[start] = 1

travelsal(mat, start)
# print(ans)
ans = [dic[k] for k in ans]
print(" ".join(ans))
