# 【问题描述】
#     Sklearn 也是科研数值计算中常用到的库之一，不仅集成了 SVM、决策树等多种模型供直接调用，还包含许多类似准确率、召回率计算等用于模型评估的函数。
# 本题需要使用sklearn计算一组数据的 F1值：F1值（F1-score）是分类问题的一种衡量指标，是精确率（precision）和召回率（recall）的调和平均数，最大为1，最小为0。


# 首先定义以下几个概念：
# TP（True Positive）：预测答案为正例，且实际也为正例的数量
# FP（False Positive）：错将其他类（负例）预测为正例的数量
# FN（False Negative）：正例预测为其他类标（负例）

# 则上述精确率和召回率的计算方式为：
# precision_{k}=\frac{TP}{TP+FP}
# recall_{k}=\frac{TP}{TP+FN}

# 因此精确率可以理解为预测为正例的结果中，真正是正例的比重；召回率为全部真正正例中，被预测为正例的比重。而只有precision和recall两指标都高时，才会提升F1-score。

# Sklearn 则节省了上述复杂的计算过程，提供了 sklearn.metrics.f1_score 函数，可以直接根据真实标签（y_true）和预测标签（y_pred）计算这批样本的 F1-score。
# 当然，如果只想计算 recall 或 precision，也可以使用 sklearn.metrics.precision_score 和 recall_score。

# 【输入形式】
# 输入有三行，第一行是一个浮点数，代表预测为正例的预测概率 threshold，概率大于等于threshold的样本被预测为正例。
# 接下来两行都由空格分隔。
# 第二行是一组样本的真实标签，0 或 1；
# 第三行是该组标签的预测概率，介于0 至 1 之间的浮点数，保留三位小数。

# 【输出形式】
# F1-score

# 【样例输入】
# 0.34373
# 0 0 1 1
# 0.49908166 0.5092066  0.59166291 0.38774589

# 【样例输出】
# 0.667

# 【样例说明】
# 根据第一行的threshold和第三行的预测概率，最终四个样本都被预测为正例，recall = 1, precision = 0.5。
# 因此 F1 = 0.667。

from sklearn.metrics import f1_score
p_thh = float(input())
y_true = [int(i) for i in input().split()]
y_pred = []
ps = [float(i) for i in input().split()]
for p in ps:
    if p > p_thh:
        y_pred.append(1)
    else:
        y_pred.append(0)
res = f1_score(y_true, y_pred)
print('%.3f' % res)
