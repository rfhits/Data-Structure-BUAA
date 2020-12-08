# 笔记

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

## urllib

一个可以解析网页的库，我们用里面的request模块

request有urlopen函数，返回一个网页的对象。

可以read再decode("utf-8")

### 超时处理

timeout和try-catch

### 伪装和封装

headers和request中的Request

## 错误解决

[UnicodeEncodeError: 'gbk' codec can't encode character '\xee' in position 21804: illegal multibyte sequence](https://www.jb51.net/article/64816.htm)
