# 【问题描述】新的学期到了，小学老师 W 老师接下了 4 年 3 班班主任的活。除了要每次给小明带麻麻送的旺仔牛奶之外，他还必须要按照身高给小盆友排序，以便于之后的座位安排。

# 【输入形式】
# 第一个一个正整数 n，表示小朋友的人数。
# 接下来 2n行，每两行表示一个小朋友的姓名和身高。保证不会有两个小朋友身高或名字相同。

# 【输出形式】
# 将小朋友们按身高由高到矮排序，按顺序输出 n 个小朋友的名字和身高，身高保留两位小数。输出的形式见输出样例。

# 【样例输入】
# 2
# a
# 1.023453
# b
# 2.133453

# 【样例输出】
# b, 2.13
# a, 1.02

# 共10行 →_→ ^_^ ←_←
n = int(input())
dic = {}
for i in range(n):
    name = input()
    height = float(input())
    dic[name] = height
dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
# how to sort?? haha, nice
for k, v in dic.items():
    print(k, end=', ')
    print('%.2f' % v)
