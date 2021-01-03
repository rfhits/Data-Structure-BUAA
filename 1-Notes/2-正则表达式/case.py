# https://www.bilibili.com/video/BV1xs411x71b?from=search&seid=4293577164504280220
# this video will show u a simple case on how to use regex in python :)
import re
text = ''
file = open('poem.txt')
for line in file:
    text = text + line
file.close()

# 找的以 a 开头的、长度为3单词
# res = re.findall(' (a[a-z]{2}) ', text)
# res = re.findall(' (a[a-z][a-z]) ', text)
# res = re.findall(' (a[a-z]{2}) |(A[a-z][a-z]) ', text)
res= re.findall(r'\d{2,3}',text) # 贪心，会匹配3个长度
res = set(res)
print(res)
print(len(res))
# print(text)
