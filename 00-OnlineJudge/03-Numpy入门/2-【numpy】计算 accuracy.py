# 【问题描述】
# 龟龟写了一个性能很差的二分类模型，如果告诉你每个样本正确的标签以及模型预测的标签，你能帮他计算这批样本的正确率吗
# 请用numpy，用numpy，用numpy

# 【输入形式】
# 第一行包含N个整数，0或1，代表每个样本的真实标签，空格分隔
# 第二行也包含N个整数，0或1，代表模型预测每个样本的标签，空格分隔

# 【输出形式】
# 一个小数，代表这批样本的预测准确率，保留三位小数

# 【样例输入】
# 1 1 0 1 0
# 0 1 1 0 1

# 【样例输出】
# 0.200
import numpy as np
a = np.array([int(num) for num in input().split()])
b = np.array([int(num) for num in input().split()])
total = len(a)
c = a-b
n = 0
for i in c:
    if i == 0:
        n = n+1
print('%.3f' % (n/total))