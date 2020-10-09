# 排序方法

word=input().split()
flag=input()
dict={}
for i in word:
    if i not in dict.keys():
        dict[i]=word.count(i)
f=zip(dict.values(),dict.keys())
c=sorted(f,reverse=True)
print(c)
l=int(len(dict))
d=[i for j in c for i in j ]
print(d)
for i in d:
    for j in range(0,l):
        if i == j:
            d.remove(i)
for i in d:
    if i == flag:
        print('1 ',end='')
    else:
        print('0 ',end='')