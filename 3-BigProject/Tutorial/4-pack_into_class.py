import random

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
for line in f:
    data = line.split()
    movies.append(movie(data))
print(x+1)
print(movies[x].title)