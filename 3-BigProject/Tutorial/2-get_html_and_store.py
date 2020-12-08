import urllib.request
import random
import os

# 确保Data文件夹存在
if(os.path.exists("Data")):
    pass
else:
    os.mkdir("Data")


headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',

    'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Language':' zh-CN,zh;q=0.9',

    'Cookie': 'bid=9s2YXaM8ddY; douban-fav-remind=1; __utmc=30149280; __utmc=223695111; __utmz=223695111.1607416754.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108288"; ap_v=0,6.0; _vwo_uuid_v2=D9EE8B759797EE3CBE0519CEDF2DE8D31|17632ef13dac6863480c757bcdf4009a; __extfc=1; dbcl2="208961468:/tjJXdq98hM"; ck=gZ4T; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1607436547%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; __utmt=1; __utmv=30149280.20896; __utmt_douban=1; __utma=223695111.599800690.1607416754.1607431176.1607436553.3; __utmb=223695111.0.10.1607436553; __utma=30149280.224390258.1607332982.1607436548.1607436575.5; __utmz=30149280.1607436575.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=683fa0044b20d677.1607416753.3.1607436650.1607431176.; __utmb=30149280.15.10.1607436575'
}




base_url = "https://movie.douban.com/top250?start="
base_filename = "html-"

for i in range(10):
    url = base_url + str(i*25)
    filename = base_filename + str(i) + ".html"

##### get html #####

    req = urllib.request.Request(url=url, headers=headers)  # 封装成一个Request Object
    response = urllib.request.urlopen(req)  # get返回一个file-like型的对象

##### store #####
    f = open("Data/"+filename, "w", encoding="utf-8")  # 如果路径不存在，会直接创建文件
    print(response.read().decode("utf-8"), file=f)
    f.close()
