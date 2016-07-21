# -*- coding: utf-8 -*-

import sqlite3

class SqliteManager:
    def __init__(self,dbName):
        self.dataBaseName = dbName
        self.conn = sqlite3.connect(self.dataBaseName)

    def save(self,sql):
        self.executeSql(sql)

    def delete(self,sql):
        self.executeSql(sql)

    def createTable(self,sql):
        self.executeSql(sql)

    def createIndex(self,sql):
        self.executeSql(sql)

    def executeSql(self,sql):
        self.conn.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()
