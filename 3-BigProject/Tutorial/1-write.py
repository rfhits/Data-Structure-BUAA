# 介绍如何新建文件夹和文件，并向其中写入数据

import os
if(os.path.exists("Data")):
    pass
else:
    os.mkdir("Data")
f = open("Data/in.txt","w",encoding = "utf-8") # 如果不存在，会直接创建
print("你好，世界！", file = f)