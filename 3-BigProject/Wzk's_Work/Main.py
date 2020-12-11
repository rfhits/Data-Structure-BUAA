import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from PyQt5.QtGui import QIcon

from UI import Ui_Dialog

from BplusTree import Bptree, KeyValue

import re

data=[]
mybptree=Bptree(4,4)
title_dict={}   # {"paper_title-1": key-1, "paper_title-2": key-2}
tree_dict={}

path=r"data\data ".strip()
title_path=r"title_dict51405.txt"
author_path=r"author_51405.txt"
subject_path=r"subject_51405.txt"
data_range=51405    # 总共有五万余条数据

def initial(ui):
    def generate_data_from_file(data,f,count):  # 把一组组数据插入到data里
        # count 只是一个index，从1到 data_range
        paper = f.read()    # a file string
        length=len(paper)
        data.append( {"Count":count} )
        # data里面全是set，相当于用集合表示了类

        for i in range(length):
            if paper[i:i+13] == "arxiv number:":
                for j in range(i+13,length):
                    if paper[j]=="\n":
                        break
                data[count]["Key"]=int(paper[i+13:j])
                # arxiv number 就是key
            elif paper[i:i+10] == "\nTitle:\n  ":
                for j in range(i+10,length):
                    if paper[j]=="\n":
                        break
                data[count]["Title"]=paper[i+10:j]
            elif paper[i:i+13] == "\nSubjects:\n  ":
                for j in range(i+13,length):
                    if paper[j]=="\n":
                        break
                data[count]["Subjects"]=paper[i+13:j]
            elif paper[i:i+12] == "\nAuthors:\n  ":
                for j in range(i+12,length):
                    if paper[j]=="\n":
                        break
                data[count]["Authors"]=paper[i+12:j].split(", ")
                try:
                    data[count]["Authors"].remove("")
                except:
                    pass
        return data
    def generate_title_dict(data):  # 把data里的数据都分类写到文件里、存到title里
        title_dict = {}
        f_title=open(title_path,"w")
        for paper in data:
            title_dict[paper["Title"]]=paper["Key"]
            write=paper["Title"]+" : "+str(paper["Key"])+"\n"
            f_title.write(write)
        print("Generate Title_Dict Completed.")
        return title_dict


    def generate_author_rank(data):
        author_dict={}
        f_author=open(author_path,"w")
        for i in data:
            if 'Authors' not in i.keys():
                continue
            for author in i['Authors']:
                if author in author_dict:
                    author_dict[author] += 1
                else:
                    author_dict[author] = 1
        author_dict_sort=sorted(author_dict.items(),key=lambda item:item[1],reverse=True)
        for author in author_dict_sort:
            if author!='':
                print(author[0]+" : "+str(author[1]),file=f_author)
    
    def generate_subject_rank(data):
        subject_dict={}
        f_subject=open(subject_path,"w")
        for i in data:
            if 'Subjects' not in i.keys():
                continue
            subject=i['Subjects']
            if subject in subject_dict:
                subject_dict[subject] += 1
            else:
                subject_dict[subject] = 1
        subject_dict_sort=sorted(subject_dict.items(),key=lambda item:item[1],reverse=True)
        for subject in subject_dict_sort:
            if subject!='':
                print(subject[0]+" : "+str(subject[1]),file=f_subject)

    
    global data,mybptree,title_dict,tree_dict,path,f_title,f_author,f_subject,data_range
    testlist=[]
    print("Data Processing")
    for count in range(data_range): ########
        f_source = open(path+str(count+1)+".txt","r")
        generate_data_from_file(data,f_source,count)
        testlist.append(KeyValue(data[count]["Key"],path+str(count+1)+".txt"))
    print("Generate Data Completed.")
    
    for kv in testlist:
        mybptree.insert(kv)
    print("Build B+Tree Completed")
    
    for i in data:
        try:
            key=re.search("\((.*)\)",i['Subjects']).group(1)
        except:
            pass
        if key not in tree_dict:
            subtree=Bptree(4,4)
            tree_dict[key]=subtree
        tree_dict[key].insert(KeyValue(i["Key"],path+str(i["Count"]+1)+".txt"))
    print("Build B+Trees With Subjects Completed.")
    print("Initialization Completed.")
    
    title_dict=generate_title_dict(data)
    generate_author_rank(data)
    generate_subject_rank(data)


class UI(Ui_Dialog):    # setup UI
    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        initial(self)
                
    
    
def tree_search_ui(mybptree,key):   # use Arxiv number directly
    result = mybptree.search(key)
    if result!=None:
        f=open(result.value,"r")
        return f.read()+"PDF download:\n" + r"http://arxiv.org/pdf/"+str(result.key)[0:4]+"."+str(result.key)[4:9]+"\n"
    return None

def search(ui):
    if ui.line_input_2.text()=="":
        target_tree = mybptree
    else:
        try:
            target_tree = tree_dict[ui.line_input_2.text()]
        except:
                ui.textBrowser.setText("Wrong subject name.")
                target_tree = mybptree

    if ui.comboBox.currentText()=='Arxiv Number':
        try:
            key=int(ui.line_input.text())
            result=tree_search_ui(target_tree,key)
            if result!=None:
                ui.textBrowser.setText(result)
            else:
                ui.textBrowser.setText("No results.")
        except:
            ui.textBrowser.setText("Wrong Behavior.")
    elif ui.comboBox.currentText()=='Title (precise)':
        try:
            key=title_dict[ui.line_input.text()]
            result=tree_search_ui(target_tree,key)
            ui.textBrowser.setText(result)
        except:
            ui.textBrowser.setText("No results.")
        
    elif ui.comboBox.currentText()=='Title (regular expression)':
        key_results=[]
        output_results=[]
        pattern=ui.line_input.text()
        for string in title_dict.keys():
            if re.search(pattern,string)!=None:
                key_results.append(string)
        if len(key_results)==0:
            ui.textBrowser.setText("No results.")
        else:
            for key_result in key_results:
                key=title_dict[key_result]
                result=tree_search_ui(target_tree,key)
                if result!=None:
                    output_results.append(result)
            if len(output_results)!=0:
                ui.textBrowser.setText(str(len(output_results))+" results.\n\n"+"\n".join(output_results))
            else:
                ui.textBrowser.setText("No results.")
    
def author_rank(ui):
    f_author=open(author_path,"r")
    ui.textBrowser.setText(f_author.read())
    
def subject_rank(ui):
    f_subject=open(subject_path,"r")
    ui.textBrowser.setText(f_subject.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    MainWindow.setWindowIcon(QIcon('icon.jpg')) 

    ui.button_number.clicked.connect(partial(search,ui))
    #

    ui.button_author_rank.clicked.connect(partial(author_rank,ui))
    #

    ui.button_subject_rank.clicked.connect(partial(subject_rank,ui))
    #
    
    
    sys.exit(app.exec_())
    