import random

# 随机生成数字，检查合法性
x = random.randint(0,250)

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
print(x+1)
print(movies[x].title)