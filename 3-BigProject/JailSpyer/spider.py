import urllib.request

baseurl = "http://movie.douban.com/top250?start="

def getData(baseurl):
    datalist = []
    for i in range(10):
        url = baseurl + str(i*25)
        html = askURL(url)
    
        # 逐一解析

    return datalist

def saveData(savepath):
    """
    save data
    """
    print("sace...")


# 指定得到一个url的网页内容
def askURL(url):

    # 模拟头部信息
    # 告诉豆瓣我们是什么浏览器，可以接受什么样的信息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    request = urllib.request.Request(url, headers = head)
    html = ''
    try:
        reponse = urllib.request.urlopen()
        html = reponse.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasttr(e, "reason"):
            print(e,reason)
    return html
            
            


if __name__ == "__main__":

