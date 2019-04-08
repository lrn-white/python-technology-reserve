from pyspark import SparkContext, SparkConf


if __name__ == '__main__':

    conf = SparkConf().setMaster("local").setAppName("wordcount")
    sc = SparkContext(conf=conf)
    lines = sc.textFile("word.txt")

    words = lines.flatMap(lambda line: line.split(" "))
    pairwords = words.map(lambda word: (word, 1))
    result = pairwords.reduceByKey(lambda v1, v2: v1 + v2)
    result.foreach(print)
    sc.stop()
