# 利用本地的html，提取信息并存储到Data.txt里

# region 参考链接：

# https://www.bilibili.com/video/BV12E411A7ZQ?p=20
# https://www.bilibili.com/video/BV12E411A7ZQ?p=21
# https://www.bilibili.com/video/BV12E411A7ZQ?p=22
# https://www.bilibili.com/video/BV12E411A7ZQ?p=23
# https://www.bilibili.com/video/BV12E411A7ZQ?p=24

# endregion

from bs4 import BeautifulSoup
import re

base_filename = "Data/html-"

# region define所有的pattern
title_pat = re.compile(r'<span class="title">([^&].*)</span>')
rating_pat = re.compile(
    r'<span class="rating_num" property="v:average">(.*)</span>')
link_pat = re.compile(r'<a href="(.*)">')
cmnt_pat = re.compile(r'<span class="inq">(.*)</span>')
# endregion


# region 每找到一个movie，将内容分类存到list中
# 很遗憾，仅支持movie的标题(title)、评分(rating)、链接(link)、精选评论(comment)
title_lst = []
rating_lst = []
link_lst = []
cmnt_lst = []
# endregion


def elem(lst):
    ''' 当利用regex从item中查找时，可能啥也没找到，
    返回一个空列表，这时，添加到list中的元素就得是None'''
    if len(lst) == 0:
        return None
    else:
        return lst[0]


for i in range(10):  # 对10个html依次读取
    filename = base_filename + str(i) + ".html"
    f = open(filename, encoding="utf-8")
    html = f.read()

    bs = BeautifulSoup(html, "html.parser")
    item_lst = bs.find_all("div", class_="item")
    for item in item_lst:
        item = str(item)
        title_lst.append(re.findall(title_pat, item)[0])
        rating_lst.append(re.findall(rating_pat, item)[0])
        link_lst.append(re.findall(link_pat, item)[0])
        cmnt_lst.append(elem(re.findall(cmnt_pat, item)))
    f.close()

f = open("data.txt", "w", encoding="utf-8")
# 将电影的属性写入文件时，
# 如果要用strip处理， 
# 切记不能每行就包含一个电影的属性，可能有空格，此处导致了第一个bug
# 所以此处每行只有一个属性，一个movie有6行属性
# 详情请见Data.txt
for i in range(250):
    print(i+1, file=f)
    print(title_lst[i], file=f)
    print(rating_lst[i], file=f)
    print(cmnt_lst[i], file=f)
    print(link_lst[i], file=f)
    print('', file=f)
