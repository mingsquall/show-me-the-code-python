#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0002: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""

import mysql.connector
import random
import string

poolOfRandom = string.ascii_letters + string.digits

def generate_code(total_code_num, code_len):
    codes = []
    for x in range(total_code_num):
        code = ""
        for y in range(code_len):
            code += random.choice(poolOfRandom)
        codes.append(code)
    return codes

def save_code2mysql():
    # 建立和数据库系统的连接
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '10111105', database = 'test')
    # 获取操作游标
    cursor = conn.cursor()
    # cursor.execute("CREATE DATABASE if not EXISTS test")
    cursor.execute("""CREATE TABLE if not EXISTS code
                    (
                    id   INT       NOT NULL,
                    code CHAR(25)  NOT NULL,
                    PRIMARY KEY (id)
                    )"""
    )
    codes = generate_code(200, 20)
    for index, code in enumerate(codes, 1):
        cursor.execute("""INSERT INTO code (id, code) VALUES (%s, %s)""", params=[index, code])
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    save_code2mysql()
