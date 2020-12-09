# Tutorial

直接看视频，讲得比我好。  
我的代码提供参考。

## 新建文件夹写文件

见 [1-write.py](/1-write.py)

有要求：

1. 利用路径判断某个文件夹是否存在，不存在直接创建

2. 写到的文件用相对路径来表示

3. utf-8为文件打开格式（Windows默认是GBK）

代码：

    import os
    if(os.path.exists("Data")): # Data文件夹是否存在
        pass
    else:
        os.mkdir("Data")    # 不存在的话，创建改文件夹
    f = open("Data/in.txt","w",encoding = "utf-8") # 如果不存在in.txt，会直接创建
    print("你好，世界！", file = f)

重要的是，判断有没有文件夹和文件的打开方式

## urllib得到html

一个可以解析网页的库，我们用里面的request模块

### 封装和伪装

request模块下的Request函数，  
接受url和headers，封装成一个request对象  
这个request就要发送给服务器。

对于headers
带上了User-Agent和cookie进行伪装。  
cookie的查找可以百度。  
带上cookie可以anti-anti-spider : )

### 响应和存储

request模块有urlopen函数，接受request对象，  
返回一个网页的对象。

可以read再decode("utf-8")，写到本地的html文件中。

## BeautifulSoup和Re

BeautifulSoup是一个第三方解析网页的库，所以要自行安装；  
Re库，大家在学习正则表达式时，已经和它打过招呼了。

打开本地的html，使用read函数，得到string-stream。  
将此string-stream，配合html.parser  
用bs模块的BeautifulSoup函数进行解析。

### 找到item

利用find_all，找到25个item。  
将此item标签，强转为str，  
用regex获取内容。

值得注意的是，有的item中，没有评论(cmnt)。  
此刻应做判断，返回None。

## 参考链接

[urllib的使用](https://www.bilibili.com/video/BV12E411A7ZQ?p=18)  
[获取html](https://www.bilibili.com/video/BV12E411A7ZQ?p=19)  
[BeautifulSoup教程-1](https://www.bilibili.com/video/BV12E411A7ZQ?p=20)  
[BeautifulSoup教程-2](https://www.bilibili.com/video/BV12E411A7ZQ?p=21)  
[正则表达式教程-1](https://www.bilibili.com/video/BV12E411A7ZQ?p=22)
[利用正则表达式提取内容](https://www.bilibili.com/video/BV12E411A7ZQ?p=23)  
[解析标签并提取](https://www.bilibili.com/video/BV12E411A7ZQ?p=24)  

## 错误解决

[打开文件，报gbk相关错误](https://www.jb51.net/article/64816.htm)
