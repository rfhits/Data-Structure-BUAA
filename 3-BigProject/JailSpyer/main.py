import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from functools import partial
from PyQt5.QtGui import QIcon

from JailSpyder import Ui_MainWindow
from BplusTree import Bptree, KeyValue

import re
import random

movies = []     # 每一个movie被封装成了dict，存在movies这个list中
num = 250
tree = Bptree(4, 4)
cnt = 0

#  region 一个电影元素的内容：rank、title、 rating、cmnt、link、year
# 1
# 肖申克的救赎
# 9.7
# 希望让人自由。
# https://movie.douban.com/subject/1292052/
# 1994
# endregion


def lst_to_dct(lst):
    """
    把列表变成字典
    """
    movie = {}
    movie["rank"] = int(lst[0])
    movie["title"] = lst[1]
    movie["rating"] = float(lst[2])
    movie["cmnt"] = lst[3]
    movie["link"] = lst[4]
    movie["year"] = int(lst[5])
    return movie


def movie_to_str(movie):
    out = ''
    out += '名称：' + movie['title'] + '\n'
    out += '上映年份：' + str(movie['year']) + '\n'
    out += '排名：' + str(movie['rank']) + '\n'
    out += '评分：' + str(movie['rating']) + '\n'
    out += '精选评论：\n' + movie['cmnt'] + '\n'
    out += '链接：\n' + movie['link'] + '\n\n\n'
    return out


def fuzzy_value(movie, keywords):
    value = 0
    for kw in keywords:
        if kw in movie["title"]:
            value += 1
        else:
            pass
        if kw in movie['cmnt']:
            value += 1
        else:
            pass
    return value


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # search
        self.pushButton_search.clicked.connect(self.search)

        # feeling lucky, give a random to user
        self.pushButton_luck.clicked.connect(self.luck)

    def search(self):
        global movies
        res = ''
        Jstr = ''
        word_in = self.lineEdit_input.text()
        if self.comboBox.currentText() == "全名搜索":
            Jstr = "很抱歉，没有找到！"
            for movie in movies:
                if movie["title"] == word_in:
                    res = movie_to_str(movie)
                    Jstr = "找到了！"
                    break
                else:
                    pass
        elif self.comboBox.currentText() == "模糊搜索":
            search_res = []
            res = ''
            Jstr = ''
            keywords = word_in.split(' ')
            # print(keywords)
            search_res = [(movie, fuzzy_value(movie, keywords))
                          for movie in movies if (fuzzy_value(movie, keywords) > 0)]
            if len(search_res) == 0:
                Jstr = "很抱歉，没有找到。\n"
                Jstr += "要不换个关键词试试？ : )"
            else:
                search_res.sort(key=lambda tp: tp[1], reverse=True)
                Jstr = "共找到了" + str(len(search_res)) + "条结果！"
                for tp in search_res:
                    res += movie_to_str(tp[0])
        elif self.comboBox.currentText() == "排名搜索":
            try:
                rank = int(word_in)
            except:
                Jstr = "请输入一个整数"
                res = ""
            else:
                if rank in range(1, 251):
                    movie = tree.search(rank).value
                    res = movie_to_str(movie)
                else:
                    Jstr = "请输入一个1到250之间的整数！"
                    res = ""
        elif self.comboBox.currentText() == "排名范围":
            try:
                rank_range = [int(i) for i in word_in.split()]
            except:
                Jstr = "请输入两个1到250之间的数，空格隔开。\n谢谢 :)"
            else:
                if len(rank_range) != 2:
                    Jstr = Jstr = "请输入两个1到250之间的数，空格隔开。\n谢谢 :)"
                elif rank_range[0] in range(1, 251) and rank_range[1] in range(1, 251):
                    rank_range.sort()
                    for i in range(rank_range[0], rank_range[1]+1):
                        movie = tree.search(i).value
                        res += movie_to_str(movie)
                else:
                    Jstr = "请输入两个1到250之间的数，空格隔开。\n谢谢 : )"
        elif self.comboBox.currentText() == "评分搜索":
            try:
                rating = float(word_in)
                search_num = 0
                for movie in movies:
                    if movie['rating'] == rating:
                        res += movie_to_str(movie)
                        search_num += 1
                    else:
                        pass
                if res == '':
                    Jstr = "抱歉，看来没有电影是这个评分 😓"
                else:
                    Jstr = "一共有" + str(search_num) + \
                        "部电影评分为" + str(rating) + "!"
            except:
                Jstr = "请输入一个1到10之间的数 :)"
        elif self.comboBox.currentText() == "评分范围":
            try:
                rating_range = [float(i) for i in word_in.split()]
            except:
                Jstr = "请输入两个0到10之间的实数，空格隔开。\n谢谢 :)"
            else:
                if len(rating_range) != 2:
                    Jstr = Jstr = "请输入两个0到10之间的实数，空格隔开。\n谢谢 :)"
                elif (0 <= rating_range[0] <= 10) and (0 <= rating_range[1] <= 10):
                    search_num = 0
                    rating_range.sort()
                    for movie in movies:
                        if rating_range[0] <= movie["rating"] <= rating_range[1]:
                            search_num += 1
                            res += movie_to_str(movie)
                        else:
                            pass
                    Jstr = "有" + str(search_num) + "部电影的评分落在" + "[" + str(
                        rating_range[0])+", " + str(rating_range[1]) + "]" + "内！"
                else:
                    Jstr = "请输入两个0到10之间的实数，空格隔开。\n谢谢 : )"
        elif self.comboBox.currentText() == "年份搜索":
            try:
                year = int(word_in)
            except:
                Jstr = "请输入一个年份 : )"
            else:
                search_num = 0
                for movie in movies:
                    if movie['year'] == year:
                        search_num += 1
                        res += movie_to_str(movie)
                    else:
                        pass
                Jstr = "共有" + str(search_num) + "部电影在" + str(year) + "年上映。"
        elif self.comboBox.currentText() == "年份范围":
            try:
                year_range = [int(i) for i in word_in.split()]
            except:
                Jstr = "世界上第一部电影上映年份是1985年哦\n所以请输入两个合法的年份，空格隔开。\n谢谢 :)"
            else:
                if len(year_range) != 2:
                    pass
                elif (1895 <= year_range[0] <= 2020) and (1895 <= year_range[1] <= 2020):
                    search_num = 0
                    year_range.sort()
                    for movie in movies:
                        if year_range[0] <= movie["year"] <= year_range[1]:
                            search_num += 1
                            res += movie_to_str(movie)
                        else:
                            pass
                    Jstr = "有" + str(search_num) + "部电影在" + \
                        str(year_range[0])+"年到" + str(year_range[1]) + "年内上映！"
                else:
                    Jstr = "世界上第一部电影上映年份是1985年哦\n所以请输入两个合法的年份，空格隔开。\n谢谢 :)"
        else:
            self.textBrowser_GuideJ.setText("comboBox Error")

        self.textBrowser_res.setText(res)
        self.textBrowser_GuideJ.setText(Jstr)
        res = ''
        Jstr = ''

    def luck(self):
        ran = random.randint(1, num+1)
        # print(ran)
        movie = tree.search(ran).value
        res = movie_to_str(movie)
        Jstr = "哦，你找到了《" + movie['title'] + "》\n"
        Jstr += "不知道你看过没有，真的很不错哦！"
        self.textBrowser_GuideJ.setText(Jstr)
        self.textBrowser_luck.setText(res)

    # region 写入B+树
    f = open("data.txt", "r", encoding="utf-8")
    data = [str(line.strip()) for line in f]
    for i in range(250):
        movie_lst = data[i*7:i*7+6]
        movies.append(lst_to_dct(movie_lst))
        i += 1
    # region test movies
    # x = random.randint(0, 250)
    # print(x+1)
    # print(movies[x])
    # endregion

    for i in range(250):
        tree.insert(KeyValue(movies[i]["rank"], movies[i]))
    # endregion


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
