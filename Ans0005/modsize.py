#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0005: 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
from PIL import Image
import os

path = 'pics'
resultPath = 'result'

if not os.path.isdir(resultPath):
    os.mkdir(resultPath)

for picName in os.listdir(path):
    picPath = os.path.join(path, picName)
    with Image.open(picPath) as img:
        w, h = img.size
        # 判断是否需要缩放
        if h > 1136 or w > 640:
            # 确定缩放比例
            if w/1136 >= h/640:
                n = w/1136
            else:
                n = h/640
            img.thumbnail((w/n, h/n))
            img.save(resultPath + '/finish_' + picName.split('.')[0] + '.jpg', 'jpeg')
        else:
            print('There is no need to resize this pic')


