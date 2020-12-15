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


Jwelcome = "欢迎来到豆瓣电影Top250检索系统！"
luck_int = "不知道要看哪部电影？\n试试“手气不错”！"
tags = "犯罪 剧情 爱情 同性 动作 灾难 喜剧  战争 动画 奇幻 历史 科幻 悬疑 冒险  音乐 歌舞 古装 传记 家庭 惊悚 运动  西部 情色 儿童 纪录片 武侠 恐怖"

def lst_to_dct(lst):
    """
    把列表变成字典
    """
    movie = {}
    movie["rank"] = int(lst[0])
    movie["title"] = lst[1]
    movie["tag"] = lst[2]

    movie["dir"] = lst[3]
    movie["star"] = lst[4]
    movie["rgn"] = lst[5]

    movie["rating"] = float(lst[6])
    movie["year"] = int(lst[7])

    movie["cmnt"] = lst[8]
    movie["link"] = lst[9]

    movie["path"] = "Movies/movie-" + str(movie["rank"]) + ".txt"
    return movie


def movie_to_str(movie, fuzzy_lst=None):
    out = ''
    if fuzzy_lst != None:
        out += "关键词："
        for i in fuzzy_lst:
            out += str(i)
        out += "\n\n"

    out += '排名：' + str(movie['rank']) + '\n'
    out += '名称：' + movie['title'] + '\n'
    out += '类别：' + movie['tag'] + '\n\n'

    out += '导演：' + movie['dir'] + '\n'
    out += '主演：' + movie['star'] + '\n'
    out += '国家或地区：' + movie['rgn'] + '\n\n'

    out += '评分：' + str(movie['rating']) + '\n'
    out += '上映年份：' + str(movie['year']) + '\n'

    out += '精选评论：\n' + movie['cmnt'] + '\n\n'
    out += '链接：\n' + movie['link'] + '\n'
    out += '本地路径：\n' + 'Movies/movie-' + str(movie['rank']) + '.txt\n'
    out += '----------\n\n\n'

    return out


def fuzzy_value(movie, keywords):
    value = 0
    fuzzy_lst = []
    for kw in keywords:
        flag = 0
        if kw in movie["title"]:
            value += 1
            flag = 1
        else:
            pass
        if kw in movie['cmnt']:
            value += 1
            flag = 1
        else:
            pass
        if kw in movie["tag"]:
            value += 1
            flag = 1
        else:
            pass
        if flag == 1:
            fuzzy_lst.append(kw)
    return (value, fuzzy_lst)


def tag_value(movie, tag_lst):
    value = 0
    for tag in tag_lst:
        if tag in movie["tag"]:
            value += 1
        else:
            pass
    return value


def star_value(movie, star_lst):
    value = 0
    for star in star_lst:
        if star in movie["star"]:
            value += 1
        else:
            pass
    return value


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('img/douban.ico'))

        # search
        self.pushButton_search.clicked.connect(self.search)

        # feeling lucky, give a random to user
        self.pushButton_luck.clicked.connect(self.luck)

        # init UI
        self.textBrowser_GuideJ.setText(Jwelcome)
        self.textBrowser_luck.setText(luck_int)

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
                          for movie in movies if (fuzzy_value(movie, keywords)[0] > 0)]
            # search_res: [(movie, (value, fuzzy_lst)), ]
            if len(search_res) == 0:
                Jstr = "很抱歉，没有找到。\n"
                Jstr += "要不换个关键词试试？ : )"
            else:
                search_res.sort(key=lambda tp: tp[1][0], reverse=True)
                Jstr = "共找到了" + str(len(search_res)) + "条结果！"
                for tp in search_res:
                    res += movie_to_str(tp[0], fuzzy_lst=tp[1][1])

        elif self.comboBox.currentText() == "类别搜索":
            Jstr = ''
            res = ''
            tag_lst = word_in.split()
            search_res = [(movie, tag_value(movie, tag_lst))
                          for movie in movies if (tag_value(movie, tag_lst)) > 0]
            if len(search_res) == 0:
                Jstr = "很抱歉，没有找到。\n"
                Jstr += "支持的类的关键字有：\n"
                Jstr += tags + "\n"
                Jstr += "要不换个类别试试？ : )"
            else:
                search_res.sort(key=lambda tp: tp[1], reverse=True)
                Jstr = "共有" + str(len(search_res)) + "部电影的类别和您的输入相关 (*^_^*)"
                for tp in search_res:
                    res += movie_to_str(tp[0])

        elif self.comboBox.currentText() == "导演搜索":
            Jstr = ''
            res = ''
            cnt = 0
            for movie in movies:
                if word_in in movie["dir"]:
                    res += movie_to_str(movie)
                    cnt += 1
                else:
                    pass
            if cnt == 0:
                Jstr += "抱歉，好像没有导演的名字能匹配上您的输入呢/(ㄒoㄒ)/~~\n"
                Jstr += "要不，换个关键字（词）试试"
            else:
                Jstr += "共有" + str(cnt) + "位导演的名字匹配上了您的输入！O(∩_∩)O"

        elif self.comboBox.currentText() == "主演搜索":
            Jstr = ''
            res = ''
            star_lst = word_in.split()
            search_res = [(movie, star_value(movie, star_lst))
                          for movie in movies if (star_value(movie, star_lst)) > 0]
            if len(search_res) == 0:
                Jstr = "很抱歉，什么也没有找到。,,ԾㅂԾ,,\n"
                Jstr += "要不换个主演的名字试试？"
            else:
                search_res.sort(key=lambda tp: tp[1], reverse=True)
                Jstr = "共有" + str(len(search_res)) + "部电影和您的输入的主演信息相关 (*^_^*)"
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
            Jstr = "请输入两个1到250之间的数，空格隔开。\n谢谢 :)"
            try:
                rank_range = [int(i) for i in word_in.split()]
            except:
                pass
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
            Jstr = "请输入两个0到10之间的实数，空格隔开。\n谢谢 :)"
            try:
                rating_range = [float(i) for i in word_in.split()]
            except:
                pass
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
            Jstr = "世界上第一部电影上映年份是1985年哦\n请输入两个合法的年份，空格隔开。\n谢谢 :)"
            try:
                year_range = [int(i) for i in word_in.split()]
            except:
                Jstr = "世界上第一部电影上映年份是1985年哦\n请输入两个合法的年份，空格隔开。\n谢谢 :)"
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
                    Jstr = "世界上第一部电影上映年份是1985年哦\n请输入两个合法的年份，空格隔开。\n谢谢 :)"
        else:
            self.textBrowser_GuideJ.setText("comboBox Error")

        self.textBrowser_res.setText(res)
        self.textBrowser_GuideJ.setText(Jstr)
        res = ''
        Jstr = ''

    def luck(self):
        ran = random.randint(1, num+1)
        # print(ran)
        try:
            movie = tree.search(ran).value
            res = movie_to_str(movie)
            Jstr = "哦，你找到了《" + movie['title'] + "》\n"
            Jstr += "不知道你看过没有，真的很不错哦！"

        except:
            Jstr = "第" + str(ran) + "部电影出了点问题 ,,ԾㅂԾ,,"

        self.textBrowser_GuideJ.setText(Jstr)
        self.textBrowser_luck.setText(res)
    # region 写入B+树
    f = open("data.txt", "r", encoding="utf-8")
    data = [str(line.strip()) for line in f]
    for i in range(250):

        movie_lst = data[i*11: i*11+10]

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
