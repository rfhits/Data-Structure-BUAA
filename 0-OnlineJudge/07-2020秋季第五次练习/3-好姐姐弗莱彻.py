# 【问题描述】弗莱彻有174个妹妹，但她的妹妹们不太喜欢看说明，弗莱彻姐姐只好把要去的地方着重标出
# 【输入形式】
# 分两列输入，第一列输入一句用空格隔开的话，第二行输入每个字标记，标记分为O(什么都不是)，B-LOC(地点首字)，I-LOC（地点其余字）

# 【输出形式】一句带标记的话

# 【样例输入】
# 记 者 们 在 香 港 必 须 要 跑 得 快
# O O O O B-LOC I-LOC O O O O O O

# 【样例输出】
# 记者们在<LOC>香港</LOC>必须要跑得快

# 【样例说明】这就不用我多说了吧
# 【评分标准】这也不用我多说多了吧

# 注意：
# 单汉字，单个地名
# 多汉字，多地名

s = input().split()     # 汉字
mark = input().split()    # 标记
doing = 0               # 是否正在进行一个地名的输出
j = 0                   # 汉字的输出索引
for i in mark:
    if i == "O":         # 检查上一个地名输出是否结束
        if doing == 1:
            print("</LOC>", end='')
            doing = 0
        print(s[j], end='')
    elif i == "B-LOC":
        if doing == 1:      # 检查上一个地名输出是否结束
            print("</LOC>", end='')
            doing = 0
        print("<LOC>", end='')
        doing = 1
        print(s[j], end='')
    else:                   # 地名其他字符，顺序输出
        print(s[j], end='')
    j += 1
if doing == 1:          # 封尾
    print("</LOC>", end='')
