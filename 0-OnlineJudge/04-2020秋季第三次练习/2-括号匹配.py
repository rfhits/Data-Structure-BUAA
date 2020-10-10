# 【问题描述】
# 判断包含有4种括号{，[，<（，），>，]，}的字符串是否是合法匹配。

# 例如以下是合法的括号匹配：
# (),   [ ],  (()),   ([ ]), ()[ ],   ()[()]

# 以下是不合法的括号匹配：
# (,   [,  ],   )(,   ([ ]},  ([()，{( })

# 【输入形式】
# 一行字符串（长度范围为1～200）

# 【输出形式】
# 如果字符串中括号匹配是合法的，则输出“Yes”；不合法则输出“No”。

# 【样例输入】
# ([)

# 【样例输出】
# No
# 【样例说明】
# 括号[没有匹配

# 【评分标准】
# 要求使用填空题中补全的Stack类完成程序设计，全部通过为满分

brs = list(input())
l = len(brs)
stack = []
# stack.append(brs[0])
for i in range(0, l):
    if len(stack) == 0:
        stack.append(brs[i])
    elif brs[i] == '[' or brs[i] == '{' or brs[i] == '<' or brs[i] == '(':
        stack.append(brs[i])
    elif brs[i] == ']':
        if stack[-1] == '[':
            stack.pop()
        else:
            break
    elif brs[i] == '}':
        if stack[-1] == '{':
            stack.pop()
        else:
            break
    elif brs[i] == '>':
        if stack[-1] == '<':
            stack.pop()
        else:
            break
    elif brs[i] == ')':
        if stack[-1] == '(':
            stack.pop()
        else:
            break
if (len(stack) == 0):
    print("Yes")
else:
    print("No")
