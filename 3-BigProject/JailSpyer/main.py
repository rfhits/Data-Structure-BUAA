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

#  region 一个电影元素的内容：rank、title、 rating、cmnt、link
# 1
# 肖申克的救赎
# 9.7
# 希望让人自由。
# https://movie.douban.com/subject/1292052/
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
    return movie

def movie_to_str(movie):
    out = ''
    out += '排名：' + str(movie['rank']) + '\n'
    out += '名称：' + movie['title'] + '\n'
    out += '评分：' + str(movie['rating']) + '\n'
    out += '精选评论：\n' + movie['cmnt'] + '\n'
    out += '链接：\n' + movie['link'] + '\n'
    return out

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # search
        self.pushButton_search.clicked.connect(self.search)

        # feeling lucky, give a random to user
        self.pushButton_luck.clicked.connect(self.luck)
    
    def J_show(self, Jstr):
        self.textBrowser_GuideJ.setText(Jstr)

    def search(self):
        global movies
        word_in = self.lineEdit_input.text()
        if self.comboBox.currentText()== "全名搜索":
            Jstr = "很抱歉，没有找到！"
            res = ''
            for movie in movies:
                if movie["title"] == word_in:
                    res = movie_to_str(movie)
                    Jstr = "找到了！"
                    break
                else:
                    pass
            self.textBrowser_res.setText(res)
            res = ''
            mywindow.J_show(self, Jstr)
        elif self.comboBox.currentText() == "正则匹配":
            self.textBrowser_res.setText("anti 全名")

        elif self.comboBox.currentText()== "排名搜索":
            pass
        elif self.comboBox.currentText()== "排名范围":
            pass
        elif self.comboBox.currentText()== "评分检索":
            pass
        elif self.comboBox.currentText()== "评分范围":
            pass
        elif self.comboBox.currentText()== "年份检索":
            pass
        elif self.comboBox.currentText()== "年份范围":
            pass
        else:
            self.textBrowser_GuideJ.setText("comboBox Error")
 
    def luck(self):
        ran = random.randint(1, num+1)
        print(ran)
        movie = tree.search(ran).value
        res = movie_to_str(movie)
        self.textBrowser_luck.setText(res)

        Jstr = "哦，你找到了《"+ movie['title'] + "》\n"
        Jstr += "不知道你看过没有，真的很不错哦"
        mywindow.J_show(self, Jstr)




    # region 写入B+树
    f = open("data.txt", "r", encoding="utf-8")
    data = [str(line.strip()) for line in f]
    for i in range(250):
        movie_lst = data[i*6:i*6+5]
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
    # for movie in movies:
    #     print(movie['title'])
    sys.exit(app.exec_())
