# 【问题描述】
# One-hot 编码是一种最简单的词向量表示法，又称为一位有效编码，主要是采用长度为 N 的列表对 N 个单词进行编码：
# 首先对给定语料库（本题中只有一个句子）中单词的出现频率进行降序排序，对于出现次数次序为 k 的单词（从0开始记序），词向量 w 第 k 位为 1，即除了 w[k] = 1，其余均为 0。因此可以保证不同词语的词向量都是不同的（不同词语的次序 k不同）。

# 【输入形式】
#  第一行输入一行句子，第二行输入一个单词。
# 句子均为小写且不含标点符号，而且可以不考虑单词出现次数相同的情况。

# 【输出形式】
# 输出对应的 one-hot 编码，空格分隔每一位

# 【样例输入】
# the future is not ours to see que sera sera
# sera

# 【样例输出】
# 1 0 0 0 0 0 0 0 0

import collections
words = input().split()
word = input()
dic = collections.Counter(words)
dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
lst = list(dic.keys())
for i in lst:
    if i == word:
        print('1', end=' ')
    else:
        print('0', end=' ')
