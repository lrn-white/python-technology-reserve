import sys
import time
import random

"""
模拟pvuv数据
"""


def mock(path):
    data = time.strftime('%Y-%m-%d')

    ip = '192.168.{}.{}'.format(str(random.randint(0, 255)), str(random.randint(0, 255)))

    userID = getUserId()

    locations = ['beijing', 'shanghai', 'guangzhou', 'shandong', 'shenzhen', 'chongqing']
    location = locations[random.randint(0, 5)]

    for j in range(0, random.randint(1, 10)):
        websites = ['www.baidu.com', 'www.xiaomi.com', 'www.jd.com', 'www,taobao.com', 'www.qq.com', 'www.360.com']
        website = websites[random.randint(0, 5)]

        operations = ['register', 'view', 'login', 'logout', 'buy', 'comment', 'jump']
        operation = operations[random.randint(0, 6)]

        oneInfo = data + "\t" + ip + '\t' + 'uid' + userID + "\t" + location + "\t" + website + "\t" + operation
        write_log_to_file(path, oneInfo)


def getUserId():
    id = str(random.randint(0, 100000))
    tmpstr = ""
    if len(id) < 5:
        for i in range(0, (5 - len(id))):
            tmpstr += "0"
    return tmpstr + id


def write_log_to_file(path, log):
    """
    'r'读,'w'写,'a'追加
    'r+'读+写
    'w+'读+写
    'a+'追加+写
    """
    with open(path, "a+") as f:
        f.writelines(log + "\n")


if __name__ == '__main__':
    output_path = 'data.txt'
    for i in range(1, 10000):
        mock(output_path)
