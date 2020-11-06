s = input().split()
i = 0
while(1):
    a = i*2+1
    if a >= len(s):
        break
    if s[a] == "None":
        break
    else:
        i = a

print(s[i])
