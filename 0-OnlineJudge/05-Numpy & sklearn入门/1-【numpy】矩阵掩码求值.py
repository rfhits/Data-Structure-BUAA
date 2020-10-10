import numpy as np
tmp=[]
n=int(input())
for i in range(n):
    tmp.extend([int(i) for i in input().split()])
array_a=np.array(tmp)
tmp.clear()
mask=[]
for i in range(n):
    tmp.extend([int(i) for i in input().split()])
for i in tmp:
    if i==0:
        mask.append(False)
    else:
        mask.append(True)

print(array_a[mask].sum())