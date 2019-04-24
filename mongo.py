"""
pymongo 模块操作示例
用于数据增删改查方法的参考
"""

from pymongo import MongoClient

#创建数据库链接
conn = MongoClient("localhost",27017)

#创建数据库对象和集合对象
db = conn.stu
myset = db.class5

#进行数据操作

#***************insert*******************
# myset.insert_one({"name":"张铁林","king":"乾隆"})
# myset.insert_many([{"name":"陈道明","king":"康熙"},
#                   {"naem":"张国立","king":"康熙"}])
# myset.insert({"name":"唐国强","king":"雍正"})
# myset.insert([{"name":"陈建斌","king":"雍正"},
#               {"name":"聂远","king":"乾隆"}])
# myset.save({"_id":1,"name":"郑少秋","king":"乾隆"})

# **************** find *****************
#所有的操作符加引号,作为字符窜的表达
cursor = myset.find({},{"_id":0})
# #循环遍历得到的每一个结果都是文档字典
# for i in cursor:
#     print(i)
# print(cursor.next()) #获取游标下一个结果

# for i in cursor.sort([("king",1)]):
#     print(i)
# r = myset.find_one({"king":"康熙"},{"_id":0})
# print(r)


#****************** update *************

# myset.update_many({"king":"康熙"},
#                  {"$set":{"king_name":"玄烨"}})

# myset.update_many({"king":"雍正"},
#                   {"$set":{"king_name":"胤禛"}})
# myset.update({"king":"乾隆"},
#              {"$set":{"king_name":"弘历"}},
#              multi = True)

# myset.update_one({"king":"光绪"},
#                  {"$set":{"name":"邓超"}},
#                  upsert=True)

# ****************** delete ***************
# myset.delete_one({"king":"乾隆"})
# myset.delete_many({"king_name":None})
# myset.remove({"king":"雍正"},multi = False)
# r = myset.find_one_and_delete({"king":"乾隆"})
# print(r)

# ***************** index ****************
# 参数 "name" =====>  [("name",1)]
# index1 = myset.create_index("name")
# index2 = myset.create_index([("name",-1)],name = "NAME")
# print("index1=",index1)
# print("index2=",index2)
# myset.drop_index("NAME")
# myset.drop_index([("name",1)])
# myset.drop_indexes()

# for i in myset.list_indexes():
#     print(i)

# ******************** aggregation ************
myset = db.class1  #更换操作集合

pipe = [{"$match":{"sex":{"$exists":True}}},{"$sort":{"age":1}},{"$project":{"_id":0}}]

cursor1 = myset.aggregate(pipe)
for i in cursor1:
    print(i)



#关闭链接
conn.close()