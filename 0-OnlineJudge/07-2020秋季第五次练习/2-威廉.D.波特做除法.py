# 【问题描述】威廉.D.波特正在学习做除法，请使用正则表达式，帮帮她吧

# 【输入形式】字符串形如dividend = ?, divisor = ?
# 【输出形式】一个数，如果出现异常情况则输出No

# 【样例输入】
# dividend = 10, divisor = 3

# 【样例输出】
# 3

# 【样例说明】嗯？
# 【评分标准】嗯。


import re
s = input()
pat = r"-?\d+"      # 负号一次或没有； 十进制数至少一个
nums = [int(i) for i in list(re.findall(pat, s))]
if len(nums) != 2 or nums[1] == 0:     # 输入数字的个数错误 或 除数是0
    print("No")
else:
    print(nums[0]//nums[1])
