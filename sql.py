#!/usr/bin/env python
# coding: utf-8
import qrcode
import urllib
import urllib2
import cookielib
import requests
import xml.dom.minidom
import json
import time
import re
import sys
import os
import random
import multiprocessing
import platform
import logging
from collections import defaultdict
from urlparse import urlparse
from lxml import html
import MySQLdb

class MySql(object):

    # def __int__(self):
    #     self.name = "ddddddd"
        # self.mysqlConnection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='666666',db='weixin')
        # self.cursor = mysqlConnection.cursor()

    def select(self):
        com = "cdcdc'd"

        mysqlConnection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='666666',db='weixin')
        cursor = mysqlConnection.cursor()

        com = MySQLdb.escape_string(com)
        sql = "insert into user_msg_log (`user_id`,`user_name`,`msg_content`) values ('%s','%s','%s')"%('1','kaizhu',com)

        print sql

        try:
            cursor.execute(sql)
            mysqlConnection.commit()
        except Exception, e:
            print e
        

        # print self.name
        # sql = "select * from gxq_ttfund_prize limit 1"
        # self.cursor.execute(sql)
        # alldata = self.cursor.execute(sql).fetchall()
        # if alldata:
        #     for rec in alldata:
        #         print rec[0], rec[1]

        cursor.close()
        mysqlConnection.close()

    # def logWecharFriendMsg(self,uid,username,msgcontent):

    def insert(self,uid,username,msgcontent):
        mysqlConnection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='666666',db='weixin')
        cursor = mysqlConnection.cursor()
        sql = "insert into user_msg_log (`user_id`,`user_name`,`msg_content`) values ('%s','%s','%s')"%(uid,username,msgcontent)

        print sql

        try:
            cursor.execute(sql)
            mysqlConnection.commit()
        except Exception, e:
            print e



if __name__ == '__main__':
    sql = MySql()
    sql.select()

