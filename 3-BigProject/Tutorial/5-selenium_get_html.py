import os
if(os.path.exists("Selenium_Html")):
    pass
else:
    os.mkdir("Selenium_Html")


from selenium import webdriver
import time
import random
base_filename = "Selenium_Html/html-"
base_url = 'https://movie.douban.com/top250?start='
browser = webdriver.Chrome(
    "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

for i in range(10):
    filename = base_filename + str(i) + ".html"
    url = base_url + str(i*25)
    f = open(filename, "wb")
    browser.get(url)
    time.sleep(2)
    f.write(browser.page_source.encode("utf-8"))
    # 写入文件
    print(str(i) + '文件写入成功')
    # 关闭文件
    f.close()
    sleep_time = random.randint(3, 7)
    time.sleep(sleep_time)
browser.quit()
