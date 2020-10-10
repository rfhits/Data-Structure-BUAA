# 【问题描述】

# 保持良好的编程习惯是很重要的，这其中包括一点就是变量的命名风格。合适的变量命名风格能使代码可读性更高。
# 一种命名风格是将每个单词的首字母大写，例如DataBaseUser，由于大小写字母连在一起看起来特别像骆驼的驼峰，所以这种命名风格被称作驼峰命名法(CamelCase)。
# 另外一种下划线命名方法是保持单词小写，在单词之间用下划线连接，例如data_base_user。

# 请实现将驼峰命名法转变为下划线命名法。

# 【输入形式】输入数据包含一行，为一个用驼峰命名法命名的变量名。

# 【输出形式】输出数据包含一行，为转换后的用下划线命名法命名的变量名。

# 【样例输入】
# DataBaseUser

# 【样例输出】
# data_base_user

s = list(input())
for i in range(len(s)):
    if i == 0:
        print(s[i].lower(), end='')
    elif s[i].isupper():
        print('_'+s[i].lower(), end='')
    else:
        print(s[i], end='')
