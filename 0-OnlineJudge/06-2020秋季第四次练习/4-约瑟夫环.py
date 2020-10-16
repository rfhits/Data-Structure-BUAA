# 【问题描述】
# n个人围成一个圈，按顺时针方向一次编号1、2、3、……、n，从第一个人开始顺时针方向依次报数1、2、3、……，报数m的人被淘汰，然后下一个人再从1开始报数，一直重复该过程。由于人数是有限的，因此最后一定只会剩下一个人，求这个人的编号。

#【输入形式】
# 第一行，一个整数n，表示约瑟夫环的总人数。
# 第二行，一个整数m，表示报到m的人被淘汰。

#【输出形式】
# 一行，一个整数，约瑟夫环最终剩下的人的编号。

#【样例输入】
# 5
# 2

#【样例输出】
# 3

#【样例说明】
# 5个人围成一圈，编号1，2，3，4，5；
# 第一轮，2号淘汰，剩下1，3，4，5；
# 第二轮，从3开始报数，4号淘汰，剩下1，3，5；
# 第三轮，从5开始报数，1号淘汰，剩下3，5；
# 第四轮，从3开始报数，5号淘汰，剩下3。

#【评分标准】
# 通过所有数据

n = int(input())
m = int(input())
nums = [i+1 for i in range(n)]
cur = 0         # who is counting now? "cur" means "current"
i = 1           # which number is the guy counting?
while (len(nums) != 1):
    if(i == m):
        nums.remove(nums[cur])
        i = 1
        if cur == len(nums)+1:
            cur = 0
        else:
            pass
    else:
        i += 1
        cur = (cur+1) % len(nums)
print(nums[0])
