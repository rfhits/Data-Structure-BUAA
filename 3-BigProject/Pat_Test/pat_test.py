import re

f = open('html-0.html', 'r', encoding= 'utf-8')
s = f.read()

# star_pat = re.compile(r'主演: (.*?[.]{3})')                     # 主演
star_pat = re.compile(r'主演: (.*?)<br>')                     # 主演

dir_lst = re.findall(star_pat,s)
for i in dir_lst:
    print(i)
print(len(dir_lst))