#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0004: 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re
import collections
# from collections import Counter


# 方法一
# 匹配出所有英文字符
words = re.findall(r'\w+', open('yellow.txt').read().lower())
# counter计数器统计字符出现的次数
count_dict = dict(collections.Counter(words))
for k, v in count_dict.items():
    print('%s: %s' % (k, v))

# 方法二
# ctn = Counter()
# words = re.findall(r'\w+', open('yellow.txt').read().lower())
# for word in words:
#     ctn[word] = ctn[word] + 1
# print(ctn)
