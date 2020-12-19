# 利用本地的10个html，
# 提取全部信息存储到data.txt里，这将用于检索
# 对250部电影，单独提取每一部信息，存储到Movies目录下
# 针对图片链接爬取图片，存储到Covers目录下

# region 参考链接：

# https://www.bilibili.com/video/BV12E411A7ZQ?p=20
# https://www.bilibili.com/video/BV12E411A7ZQ?p=21
# https://www.bilibili.com/video/BV12E411A7ZQ?p=22
# https://www.bilibili.com/video/BV12E411A7ZQ?p=23
# https://www.bilibili.com/video/BV12E411A7ZQ?p=24

# endregion
from bs4 import BeautifulSoup
import re
import os
import urllib.request

if(os.path.exists("Movies")):
    pass
else:
    os.mkdir("Movies")

if(os.path.exists("Covers")):
    pass
else:
    os.mkdir("Covers")

read_filename = "Selenium_Html/html-"
write_base_filename = "Movies/movie-"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',

    'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Language': ' zh-CN,zh;q=0.9'
}


# region define所有的pattern
title_pat = re.compile(r'<span class="title">([^&].*)</span>')  # 电影标题
tag_pat = re.compile(r'[\s][0-9]{4}.*[\xa0]/[\xa0](.*)[\s]')    # 类别
dir_pat = re.compile(r'导演: (.*?)[<\xa0]')                       # 导演
star_pat = re.compile(r'主演: (.*?)<br/>')                     # 主演
rgn_pat = re.compile(r'[0-9]{4}.*/[\xa0](.*?)[\xa0]/')          # 国家或地区
rating_pat = re.compile(
    r'<span class="rating_num" property="v:average">(.*)</span>')   # 评分
year_pat = re.compile(r'[\s]{2}([0-9]{4})')                     # 上映年份
cmnt_pat = re.compile(r'<span class="inq">(.*)</span>')         # 精选评论
link_pat = re.compile(r'<a href="(.*)">')                       # 链接
img_pat = re.compile(r'<img.*?src="(.*?)"')                     # 图片链接
# endregion


# region 每找到一个movie，将内容分类存到list中
# 支持movie的标题(title)、类别（tag）、
# 导演（director）、主演（star）、国家或地区（region）、
# 评分(rating)、上映年份（year）、精选评论(comment)、链接(link)

title_lst = []
tag_lst = []    # [1st movie's tags, , ]

dir_lst = []
star_lst = []
rgn_lst = []

rating_lst = []
year_lst = []
cmnt_lst = []

link_lst = []
img_lst = []
# endregion


def elem(lst):
    ''' 当利用regex从item中查找时，可能啥也没找到，
    返回一个空列表，这时，添加到list中的元素就得是None'''
    if len(lst) == 0:
        return "电影暂无此属性"
    else:
        return lst[0]

# read html files and store
for i in range(10):
    filename = read_filename + str(i) + '.html'
    f = open(filename, encoding="utf-8")
    html = f.read()

    bs = BeautifulSoup(html, "html.parser")     # receive a string stream
    item_lst = bs.find_all("div", class_="item")
    for item in item_lst:
        item = str(item)
        # print(item)

        title_lst.append(re.findall(title_pat, item)[0])
        tag_lst.append(re.findall(tag_pat, item)[0])

        dir_lst.append(elem(re.findall(dir_pat, item)))
        star_lst.append(elem(re.findall(star_pat, item)))
        rgn_lst.append(elem(re.findall(rgn_pat, item)))

        rating_lst.append(re.findall(rating_pat, item)[0])
        year_lst.append(re.findall(year_pat, item)[0])

        cmnt_lst.append(elem(re.findall(cmnt_pat, item)))
        link_lst.append(re.findall(link_pat, item)[0])
        img_lst.append(elem(re.findall(img_pat, item)))
    f.close()


# 将电影的属性写入文件时，
# 如果要用strip处理，
# 切记不能每行就包含一个电影的所有属性，可能有空格，此处导致了我的第一个bug
# 所以此处每行只有一个属性，一个movie有10行属性
# 详情请见data.txt
f = open("data.txt", "w", encoding="utf-8")
for i in range(250):
    print(i+1, file=f)
    print(title_lst[i], file=f)
    print(tag_lst[i], file=f)

    print(dir_lst[i], file=f)
    print(star_lst[i], file=f)
    print(rgn_lst[i], file=f)

    print(rating_lst[i], file=f)
    print(year_lst[i], file=f)

    print(cmnt_lst[i], file=f)
    print(link_lst[i], file=f)

    print('', file=f)
f.close()

for i in range(250):
    file_name = write_base_filename + str(i + 1) + ".txt"
    f = open(file_name, "w", encoding='utf-8')

    print("排名：" + str(i+1), file=f)

    print("电影名称：" + title_lst[i], file=f)
    print("类别：" + tag_lst[i], file=f)

    print("导演：" + dir_lst[i], file=f)
    print("主演：" + star_lst[i], file=f)
    print("国家或地区：" + rgn_lst[i], file=f)

    print("评分：" + str(rating_lst[i]), file=f)
    print("上映年份：" + str(year_lst[i]), file=f)

    print("精选评论：" + cmnt_lst[i], file=f)
    print("链接：" + link_lst[i], file=f)
f.close()

# 利用src_link拿图片
for i in range(250):
    img_name = "Covers/" + str(i + 1) + "-" + title_lst[i] + ".jpg"
    req = urllib.request.Request(url=img_lst[i], headers=headers)
    img_reponse = urllib.request.urlopen(req)
    img_content = img_reponse.read()
    imgf = open(img_name, 'wb')
    imgf.write(img_content)
    imgf.close()
