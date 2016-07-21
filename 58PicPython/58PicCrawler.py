#--coding:utf-8--
#! /usr/bin/python
import math
import urllib
import urllib2
# import request
from SqliteManager import SqliteManager
from bs4 import BeautifulSoup;

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PictureObj:
    def __init__(self,title,url):
        self.picTitle = title
        self.picUrl = url
        self.tableName = "tb_picture"

    def getTableSql(self):
        sql = 'create table IF NOT EXISTS {0} (ID INTEGER PRIMARY KEY,picTitle text,picUrl text);'.format(
            self.tableName)
        return sql
    def getCreateIndexSql(self):
        sql = 'CREATE UNIQUE INDEX IF NOT EXISTS picUrl ON {0} (picUrl ASC);'.format(self.tableName)
        return sql

    def getInsertSql(self):

        sql = 'REPLACE INTO {0} (picTitle,picUrl) VALUES (\'{1}\',\'{2}\')'.format(self.tableName,self.picTitle,self.picUrl)
        print sql
        return sql

    def getSelectSql(self):
        sql = 'select * from ' + self.tableName
        return sql

    def getDeleteAll(self):
        sql = 'delete from ' + self.tableName
        return sql

    def getDeletePhone(self,phoneNum):
        sql = 'DELETE FROM {0} WHERE phoneNum = {1}'.format(self.tableName,phoneNum)
        return sql



manager = SqliteManager('58Pic.db')
globalPhone = PictureObj('', '')
manager.createTable(globalPhone.getTableSql())
manager.createIndex(globalPhone.getCreateIndexSql())

def getAllImageLink(start,end):


    i = start

    while (i < end):
        url = 'http://www.58pic.com/yuanchuang/%d.html' % i
        try:
            response=urllib2.urlopen(url,data=None,timeout=120)
        except urllib2.URLError as e:
            print ('%s : %s' % (url,e.reason))
            i += 1
            continue
        print (url)
        html = response.read()
        if html.strip()=='':
            print ('not exist URL: %s',url)
            continue
        soup = BeautifulSoup(html, "html.parser")
        liResult = soup.findAll('div',attrs={"class":"show-area-pic"})
        for li in liResult:
            imageEntityArray = li.findAll('img')
            for image in imageEntityArray:
                title = image.get('title')
                href = image.get('src')
                pic = PictureObj(title,href)

                manager.save(pic.getInsertSql())

        i = i + 1

if  __name__ == '__main__':

    start = 19840500
    getAllImageLink(start,start + 100)