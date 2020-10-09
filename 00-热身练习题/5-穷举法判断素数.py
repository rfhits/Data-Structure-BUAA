# 穷举法判断素数
# 【问题描述】
# 如何判断一个数是否为素数？当输入数据小于等于2的时候，可以直接给出答案，当输入大于2的时候，其实可以用穷举法试出来的哦。依次用n除以2、3、4……直到n的一半（可直接取整），判断是否可以整除。如果期间的任意一个数可以整除n，则说明n不是素数，如果都不能整除，则n是素数。

# 【输入形式】每次输入一个自然数n，0≤n≤1000

# 【输出形式】一行，如果n是素数，则输出“Y”，否则输出“N”（注意不包含引号）

# 【样例输入】13
# 【样例输出】Y
# 【样例说明】13是素数，输出Y
# 【评分标准】全部通过得满分

n = int(input())
# 默认是质数
p = 1
if n <= 1:
    p = 0
elif n == 2:
    pass
else:
    lst = list(range(2, int(n/2)+1))
    for i in lst:
        if n % i == 0:
            p = 0
            break
        else:
            continue
if p == 1:
    print('Y')
else:
    print('N')
