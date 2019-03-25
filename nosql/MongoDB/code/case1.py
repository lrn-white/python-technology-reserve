import pymongo

"""
mongoDB基础操作
"""

# 连接数据库
client = pymongo.MongoClient("localhost", 27017)
# 选择数据库
db = client.test
# 获取集合
collection = db.student
# 添加数据
m1 = {"sname": "Tom", "age": 18}
m2 = {"sname": "Jack", "age": 24}
m3 = {"sname": "Tony", "age": 24}
# 添加一条数据
m1_id = collection.insert_one(m1)
# 添加多条数据
mids = collection.insert_many([m2, m3])
# 查找数据
# 返回一个生成器对象,包含所有数据
result1 = collection.find()
# 返回一条数据
result2 = collection.find_one({'sname': 'Tom'})
for r in result1:
    print(r)
print(result2)
