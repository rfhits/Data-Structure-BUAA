# 【问题描述】
# 北航主要办公科研楼有新主楼、逸夫楼、如心楼、办公楼、图书馆、主楼、一号楼等等;
# 北航网络中心计划要给相关建筑物间铺设光缆进行网络连通，请给出用料最少的铺设方案。

# 编写程序输入一个办公区域分布图及建筑物之间的距离，计算出用料最少的铺设方案（只有一组最优解，不用考虑多组解)。


# 【输入形式】
# 办公区域分布图的顶点（即建筑物）按照自然数（0，1，2，n-1）进行编号，从标准输入中首先输入两个正整数，分别表示线路图的顶点的数目和边的数目，然后在接下的行中输入每条边的信息，每条边占一行，具体形式如下：

# <n> <e>

# <id> <vi> <vj> <weight>

# ...

# 即顶点vi和vj之间边的权重是weight，边的编号是id。

# 【输出形式】
# 输出铺设光缆的最小用料数，
# 然后另起一行输出需要铺设的边的id，并且输出的id值按照升序输出。

# 【样例输入】

#  6 10
# 1 0 1 600
# 2 0 2 100
# 3 0 3 500
# 4 1 2 500
# 5 2 3 500
# 6 1 4 300
# 7 2 4 600
# 8 2 5 400
# 9 3 5 200
# 10 4 5 600

# 【样例输出】

# 1500
# 2 4 6 8 9

# 【样例说明】
# 样例输入说明该分布图有6个顶点，10条边；顶点0和1之间有条边，边的编号为1，权重为600；顶点0和2之间有条边，权重为100，其它类推。

# 提示使用Kruscal算法 :(
# 依旧使用Prim算法 :)

s = input().split()
n = int(s[0])  # num of vertexes
e = int(s[1])  # num of edges
G = []

for i in range(e):
    s = input().split()
    s = [int(i) for i in s]

    # 每条边对应个tuple，所以append俩
    ss = (s[0], s[2], s[1], s[3])
    tp = tuple(s)
    G.append(tp)
    tp = tuple(ss)
    G.append(tp)


def get_edge(lst):
    edges = []
    global G
    for i in lst:
        for edge in G:
            if edge[1] == i:
                edges.append(edge)
    for edge in edges[:]:
        if (edge[1] in lst) and (edge[2] in lst):
            edges.remove(edge)

    # 挑出可接连的、权重最小的边
    edges.sort(key=lambda x: x[3])
    if(edges):
        return edges[0]
    else:
        return None


ans = 0
tree = [0, ]
nodes = []
edge = get_edge(tree)
while(edge):
    tree.append(edge[2])
    ans += edge[3]
    nodes.append(edge[0])
    edge = get_edge(tree)

print(ans)
nodes.sort()
nodes = [str(i) for i in nodes]
print(" ".join(nodes))
