from pyspark.conf import SparkConf
from pyspark.context import SparkContext


def pv(lines):
    pair_site = lines.map(lambda line: (line.split("\t")[4], 1))
    reduce_result = pair_site.reduceByKey(lambda v1, v2: v1 + v2)
    result = reduce_result.sortBy(lambda tp: tp[1], ascending=False)
    result.foreach(print)


def uv(lines):
    distinct = lines.map(lambda line: line.split("\t")[1] + "_" + line.split("\t")[4]).distinct()
    reduce_result = distinct.map(lambda distinct: (distinct.split("_")[1], 1)).reduceByKey(lambda v1, v2: v1 + v2)
    result = reduce_result.sortBy(lambda tp: tp[1], ascending=False)
    result.foreach(print)


def uvExceptBJ(lines):
    distinct = lines.filter(lambda line: line.split("\t")[3] != 'beijing').map(
        lambda line: line.split("\t")[1] + "_" + line.split("\t")[4]).distinct()
    reduce_result = distinct.map(lambda distinct: (distinct.split("_")[1], 1)).reduceByKey(lambda v1, v2: v1 + v2)
    result = reduce_result.sortBy(lambda tp: tp[1], ascending=False)
    result.foreach(print)


def getCurrSiteTop2Location(one):
    site = one[0]
    locations = one[1]
    location_dict = {}
    for location in locations:
        if location in location_dict:
            location_dict[location] += 1
        else:
            location_dict[location] = 1
    result_list = []
    sorted_list = sorted(location_dict.items(), key=lambda kv: kv[1], reverse=True)
    if len(sorted_list) < 2:
        result_list = sorted_list
    else:
        for i in range(2):
            result_list.append(sorted_list[i])
    return site, result_list


def getTop2Location(lines):
    site_locations = lines.map(lambda line: (line.split("\t")[4], line.split("\t")[3])).groupByKey()
    result = site_locations.map(lambda one: getCurrSiteTop2Location(one)).collect()
    for elem in result:
        print(elem)


def getSiteInfo(one):
    userid = one[0]
    sites = one[1]
    dic = {}
    for site in sites:
        if site in dic:
            dic[site] += 1
        else:
            dic[site] = 1
    result_list = []
    for site, count in dic.items():
        result_list.append((site, (userid, count)))
    return result_list


def getCurSiteTop3User(one):
    site = one[0]
    userid_count_iterable = one[1]
    top3List = ["", "", ""]
    for userid_count in userid_count_iterable:
        for i in range(0, len(top3List)):
            if top3List[i] == "":
                top3List[i] = userid_count
                break
            else:
                if userid_count[1] > top3List[i][1]:
                    for j in range(2, i, -1):
                        top3List[j] = top3List[j - 1]
                    top3List[i] = userid_count
                break
    return site, top3List


def getTop3User(lines):
    site_uid_count = lines.map(lambda line: (line.split("\t")[2], line.split("\t")[4])).groupByKey().flatMap(lambda one: getSiteInfo(one))
    result = site_uid_count.groupByKey().map(lambda one: getCurSiteTop3User(one)).collect()
    for elem in result:
        print(elem)


if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("test")
    sc = SparkContext(conf=conf)
    lines = sc.textFile("data.txt")
    # pv(lines)
    # uv(lines)
    # uvExceptBJ(lines)
    # getTop2Location(lines)
    # getTop3User(lines)
