# 【问题描述】
# 小O的期末考试成绩出来了，他想要整理出自己考得最好的科目，向小L炫耀一番，你能帮帮他吗？

# 【输入形式】
# 一行若干个正整数，表示小W考试科目的成绩，中间用空格分隔。

# 【输出形式】
# 一行若干个正整数，中间用空格分隔，表示小W成绩最高的科目是哪几科（编号），若有多门科目成绩并列最高，那么从小到大输出这些科目（编号）。

# 【样例输入】
# 100 99 98 97 100

# 【样例输出】
# 1 5

res = input().split()
rec = []
for i in range(len(res)):
    rec.append(int(res[i]))
num = []
max = rec[0]
#print(rec)
for i in range(len(rec)):
    if rec[i] > max:
        num.clear()
        num.append(i+1)
        max = rec[i]
    elif rec[i] == max:
        num.append(i+1)
    else:
        pass
for i in num:
    print(i,end=' ')