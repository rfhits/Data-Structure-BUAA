# 问题描述】
# 有几座互相连接的城市，现在需要在他们之间搭设交通网，请设计一种消耗最低的交通网。

# 【输入形式】
# 一张图，表示为城市之间的邻接矩阵，A[i][j]为城市 i 到城市 j 之间的距离， -1代表不可达。

# 【输出形式】
# 最低消耗

# 【样例输入】
# -1 2 3 4
# 2 -1 4 -1
# 3 4 -1 5
# 4 -1 5 -1

# 【样例输出】9


# 使用Prim算法
# 以三元组的形式，存储无向图的信息
# 每一个edge，对应两个三元组
# 这些三元组被放在G这个list里

G = []
s = input().split()
n = len(s)      # num of vert
s = [int(i) for i in s]

# 第一行
for i in range(1, n):
    if(s[i] > 0):
        t = (0, i, s[i])
        G.append(t)

# 每一行都存起来
for i in range(1, n):
    s = input().split()
    s = [int(i) for i in s]
    for j in range(n):
        if(s[j] > 0):
            t = (i, j, s[j])
            G.append(t)

# 给定使用过的vertexes
# 返回要连接的edge


def get_edge(lst):
    edges = []
    global G

    # 有接连，就添加
    for i in lst:
        for edge in G:
            if edge[0] == i:
                edges.append(edge)

    # 开始筛选，
    for edge in edges[:]:
        if (edge[0] in lst) and (edge[1] in lst):
            edges.remove(edge)

    # 选择可接连的边中，权重最小的那条
    edges.sort(key=lambda x: x[2])
    if(edges):
        return edges[0]
    else:
        return None


ans = 0
tree = [0, ]
e = get_edge(tree)
while(e):
    tree.append(e[1])
    ans += e[2]
    e = get_edge(tree)
print(ans)
