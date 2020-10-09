# 【问题描述】
# 小 f 听说莎士比亚的总词汇量在 15000 个至 21000个之间，在佩服之余，她也想要知道自己的词汇量如何。小 f 认为，对常用词汇的掌握相对来说更为重要，因此她想请你帮她统计一下，她平时最常使用的词汇是哪些。

# 【输入形式】
# 第一行一个正整数 n，表示输入的行数。
# 接下来 n行，每行一个字符串，只包含空格和大小写字母，一行内多个单词之间用空格分割。

# 【输出形式】
# 第一行一个正整数，表示出现最多次单词的次数。对于一个单词，不论其中字母的大小写如何变化，都视为同一个单词。如 python, PYTHON, PyThOn 只算作一个单词。
# 接下来若干行字符串，表示出现最多次的单词。如果出现最多次的单词不止一个，则需要根据输入时第一次出现的先后顺序逐行输出。请注意，输出的单词必须全为小写字母（即使输入中为大写）。

# 【样例输入】
# 3
# use THAT two two
# and THAT we should
# hear and we speak

# 【样例输出】
# 2
# that
# two
# and
# we

import collections as cs
s = int(input())
words = []
# split the sentence to get the words
for i in range(s):
    senten = input().lower()
    words.extend(senten.split())
dic = dict(cs.Counter(words))
lst = list((sorted(dic.items(), key=lambda item: item[1], reverse=True)))
max=lst[0][1]
print(max)
for i in lst:
    if i[1]==max:
        print(i[0])
