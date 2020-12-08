from bs4 import BeautifulSoup
import re

base_filename = "Data/html-"

##### regex #####
title_pat = re.compile(r'<span class="title">([^&].*)</span>')
rating_pat = re.compile(
    r'<span class="rating_num" property="v:average">(.*)</span>')
link_pat = re.compile(r'<a href="(.*)">')
cmnt_pat = re.compile(r'<span class="inq">(.*)</span>')

##### lst #####
title_lst = []
rating_lst = []
link_lst = []
cmnt_lst = []


def elem(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[0]


for i in range(10):
    filename = base_filename + str(i) + ".html"
    f = open(filename, encoding="utf-8")
    html = f.read()

    bs = BeautifulSoup(html, "html.parser")
    items_lst = bs.find_all("div", class_="item")
    for item in items_lst:
        item = str(item)
        title_lst.append(re.findall(title_pat, item)[0])
        rating_lst.append(re.findall(rating_pat, item)[0])
        link_lst.append(re.findall(link_pat, item)[0])
        cmnt_lst.append(elem(re.findall(cmnt_pat, item)))
    f.close()

f = open("data.txt", "w", encoding="utf-8")
for i in range(250):
    print(i+1, end=" ", file=f)
    print(title_lst[i], end=' ', file=f)
    print(rating_lst[i], end=' ', file=f)
    print(cmnt_lst[i], end=' ', file=f)
    print(link_lst[i], end=' ', file=f)
    print('', file=f)
