#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0001: 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）。
"""
import random
import string

poolOfRandom = string.ascii_letters + string.digits

def generate_code(total_code_num, code_len):
    for x in range(total_code_num):
        code = ""
        for y in range(code_len):
            # choice(sequence)可以在一个有序的类型(比如list,tuple,string)中，随机选取一个元素
            code += random.choice(poolOfRandom)
        print(code)

if __name__ == '__main__':
    generate_code(200, 20)
