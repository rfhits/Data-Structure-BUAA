import random

# 这里既可以使用class进行封装，
# 也可以使用dict进行封装
# dict会更方便

class movie():
    def __init__(self, lst):
        self.rank = lst[0]
        self.title = lst[1]
        self.rating = lst[2]
        self.cmnt = lst[3]
        self.link = lst[4]


movies = []
f = open("data.txt", "r", encoding="utf-8")
data = [str(line.strip()) for line in f]
for i in range(250):
    movie_lst = data[i*6:i*6+5]
    movies.append(movie(movie_lst))
    i += 1

# 随机生成数字，看看存储的movie类符不符合要求
x = random.randint(0, 250)
print(x+1)
print(movies[x].rank)
print(movies[x].title)
print(movies[x].rating)
print(movies[x].cmnt)
print(movies[x].link)
