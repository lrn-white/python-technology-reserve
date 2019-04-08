from time import time

from pyspark import SparkContext, SparkConf
import pandas as pd

"""
统计每种类型的电影的数量
"""


def read_small_csv(path):
    conf = SparkConf().setMaster("local").setAppName("wordcount")
    sc = SparkContext(conf=conf)

    # dataframe读取csv
    data = pd.read_csv(path)
    lines = pd.DataFrame(data)['genres']
    # 将list转换为rdd
    new_lines = sc.parallelize(lines)

    words = new_lines.flatMap(lambda line: line.split("|"))
    pairwords = words.map(lambda word: (word, 1))
    result = pairwords.reduceByKey(lambda v1, v2: v1 + v2)
    result.foreach(print)
    sc.stop()


def read_big_csv(path):
    conf = SparkConf().setMaster("local").setAppName("wordcount")
    sc = SparkContext(conf=conf)

    # dataframe读取csv
    data = pd.read_csv(path)
    lines = pd.DataFrame(data)['movieId']
    # 将list转换为rdd
    new_lines = sc.parallelize(lines)

    pairwords = new_lines.map(lambda word: (word, 1))
    result = pairwords.reduceByKey(lambda v1, v2: v1 + v2)
    result.foreach(print)
    sc.stop()


if __name__ == '__main__':
    t1 = time()
    read_big_csv("ratings.csv")
    # read_small_csv("movies.csv")
    t2 = time()
    t = t2 - t1
    print(t)
