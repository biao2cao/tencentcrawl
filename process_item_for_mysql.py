#!/usr/bin/python
# -*- coding:utf-8 -*-

import redis
import MySQLdb
#import pymysql
import json

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", port = 6379, db = 0)

    # 创建mysql数据库连接
    #mysqlcli = MySQLdb.connect(host = "127.0.0.1", port = 3306, \
    #    user = "root", passwd = "sg186", db = "tencent")
    mysqlcli = MySQLdb.connect(host = "127.0.0.1", port = 3306, \
        user = "root", passwd = "sg186", db = "tencent" ,charset = "utf8")
    #mysqlcli = pymysql.connect(host = "127.0.0.1", port = 3306, \
    #    user = "root", password = "sg186", database = "tencent")

    offset = 0

    while True:
        # 将数据从redis里pop出来
        source, data = rediscli.blpop("tencentcrawlposition:items")
        item = json.loads(data)
        try:
            # 创建mysql 操作游标对象，可以执行mysql语句
            cursor = mysqlcli.cursor()

            cursor.execute("insert into position  (pName,pLink,pType,peopleNum,workArea,publishTime,time,spidername) values (%s, %s, %s, %s, %s, %s, %s, %s)", [item['pName'], item['pLink'],item['pType'],item['peopleNum'],item['workArea'],item['publishTime'],item['time'],item['spidername']])
            #cursor.execute("insert into position  (pName) values (%s)", [item['pName']])
        #cursor.execute("insert into position  (pName) values (item['pName'])")
            # 提交事务
            mysqlcli.commit()
            # 关闭游标
            cursor.close()
            offset += 1
            print offset
        except:
            pass

if __name__ == "__main__":
    process_item()
