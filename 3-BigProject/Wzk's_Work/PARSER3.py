from html.parser import HTMLParser
import random
import requests
import re

USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]

ip_list = [
        "39.137.69.8:8080",
        "182.34.33.119:9999",
        "101.95.115.196:8080",
        "180.153.144.138:8800",
        "117.57.91.208:9999",
        "39.137.69.7:8080",
        "219.239.142.253:3128",
        "117.69.201.13:9999"
        ]

proxy_list = [ {"http" : ip} for ip in ip_list]

class DataParser1(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data ={'number':"", 'title':"", 'authors':[], 'subjects':""}
    
    def handle_starttag(self,tag,attrs): 
        def _attr(attrlist,attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return
        if tag=='a' and _attr(attrs,'title')=='Abstract':   #tag：处理开始标签
            self.data['number'] = _attr(attrs,'href')[5:9]+_attr(attrs,'href')[10:15]

class DataParser2(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = None

    def handle_data(self, getdata):
        self.data = getdata

def get_data(html):
    global title_dict
    global f_title
    data={"number":"", "title":"", "subjects":"", "authors":[] }
    myparser1=DataParser1()
    myparser1.feed(html)
    data['number']=myparser1.data['number']
    
    re_title=r'<div class="list-title mathjax">\n<span class="descriptor">Title:</span> (.*)\n</div>'
    html_title=re.findall(re_title,html)[0]
    data['title']=html_title
    
    re_subjects=r'<div class="list-subjects">\n<span class="descriptor">Subjects:</span> <span class="primary-subject">(.*)</span>'
    html_subjects=re.findall(re_subjects,html)[0]
    data['subjects']=html_subjects
    
    re_authors=r'<a href="/search/cs\?searchtype=author\&query=(.*)</a>'
    myparser2=DataParser2()
    html_authors_list=re.findall(re_authors,html)
    for html_authors in html_authors_list:
        html_authors = html_authors.split(">")[1]
        data['authors'].append(html_authors)
    
    title = data['title']
    title_dict[title] = data['number']
    print(title+" : "+str(title_dict[title])+"\n",file=f_title)
    return data

def parser(url):
    datalist=[]
    heads = { 'User-Agent' : random.choice(USER_AGENTS) }
    req = requests.get(url, headers=heads,proxies=random.choice(proxy_list))
    htmlreturn = req.text
    htmllist = htmlreturn.split("</dd>")
    for html in htmllist:
        try:
            datalist.append(get_data(html))
        except:
            pass
    return datalist

title_dict = {}
write_path = r"D:\OneDrive - buaa.edu.cn\Curriculums\二秋-必修-数据结构\2019-WZK's_Work\Big Project"################change here########
f_title = open(write_path+"title.txt","w")
print("Arxiv Paper Parser:\n")
count = 1
start = 0############
    
for i in range(start,84):  ######################
    url="https://arxiv.org/list/cs/18?skip="+str(500*i)+"&show=500"
    datalist=parser(url)
    for data in datalist:
        f = open(write_path+str(start*500+count)+".txt","w")
        print("Paper"+str(count)+", arxiv number:"+data['number'],file=f)
        print("Title:",file=f)
        print("  " + data['title'],file=f)
        print("Subjects:",file=f)
        print("  " + data['subjects'],file=f)
        print("Authors:",file=f)
        try:
            print("  " + ", ".join(data['authors']),file=f)
        except:
            print("---unsupported character for utf-8 ---",file=f)
        print("",file=f)
        print("Paper"+str(start*500+count)+"done.")
        count += 1
        f.close()
f_title.close()
