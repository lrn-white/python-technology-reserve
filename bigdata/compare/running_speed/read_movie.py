import pandas as pd
from time import time

"""
统计每种类型的电影的数量
"""


def read_small_csv(path):
    data = pd.read_csv(path)
    genres = pd.DataFrame(data)['genres']
    movie_type = {}

    for i in range(genres.count()):
        for word in str(genres[i]).split('|'):
            if word in movie_type:
                movie_type[word] += 1
            else:
                movie_type[word] = 1
    print(movie_type)
    for key in movie_type:
        print(key + ":" + str(movie_type[key]))


def read_big_csv(path):
    data = pd.read_csv(path)
    genres = pd.DataFrame(data)['movieId']
    movie_type = {}

    for i in range(genres.count()):
        if genres[i] in movie_type:
            movie_type[genres[i]] += 1
        else:
            movie_type[genres[i]] = 1


if __name__ == '__main__':
    t1 = time()
    read_big_csv("genome-scores.csv")
    # read_small_csv("movies.csv")
    t2 = time()
    t = t2 - t1
    print(t)


# 结论：
# 小文件，比如1M时，python性能强于spark，大文件，比如10M，spark性能强于python，且数据量越大，性能差距越明显