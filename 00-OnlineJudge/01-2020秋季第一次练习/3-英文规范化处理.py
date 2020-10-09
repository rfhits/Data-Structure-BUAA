# 【问题描述】给出一段不规范的英文，只包含字母、空格“ ”、逗号“,”、句号“.”，每个句子以句号“.”结尾。要求调整所有英文字母的大小写，使其满足规范：每个句子首字母大写，字母I单独写出时（两侧均为空格或标点）大写，其余字母全部小写。

# 【输入形式】输入数据共一行， 为待转换的英文，长度不超过 200 。

# 【输出形式】输出所输入的英文大小写规范化后的结果。

# 【样例输入】life Is short, i use python. let us use Python TOGETHER.

# 【样例输出】Life is short, I use python. Let us use python together.

# 【样例说明】句子首字母大写，I大写，其他小写。

ss = input()
s = ss.split('. ')
sens = []
for i in s:
    sens.append(i.capitalize())
# 分割句子并且首字母大写

outsens = ''
for sen in sens:
    sen_list = list(sen)
    l = len(sen_list)
    for i in range(l):
        if sen_list[i] == 'i':
            if i == 0 and (not sen_list[1].isalpha()):
                outsens = outsens+('I')
            elif i > 0 and (not sen_list[i+1].isalpha()) and (not sen_list[i-1].isalpha()):
                outsens = outsens+'I'
            else:
                outsens = outsens+'i'
        else:
            outsens = outsens+sen_list[i]
    if sens.index(sen) != len(sens)-1:
        outsens = outsens+'. '
print(outsens)
