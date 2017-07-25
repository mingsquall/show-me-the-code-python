#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0000: 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
Problem 0000: Put your QQ avatar (or Weibo avatar) in the upper right corner with the red number, similar
to the amount of unread information WeChat prompted effect.
"""
from PIL import Image, ImageFont, ImageDraw
import random
from datetime import datetime

__author__ = 'YuanMingLiu'

# Print the Log information everytime you run this program
def log(func):
    def wrapper(*args, **kw):
        time = datetime.now()
        print('%s call %s(): %s' % (time, func.__name__, "1 image converted."))
        return func(*args, **kw)
    return wrapper

@log
def add_num2pic(img):
    num = str(random.randint(1, 99))
    draw = ImageDraw.Draw(img)
    font_size = int(min(img.size)/4)
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=font_size)
    fill = (256, 0, 0)

    draw.text((img.size[0] - font_size*1.2, 0), num, font=font, fill=fill)
    img.save('./new_img_'+str(num)+'.jpg', format='jpeg')


if __name__ == '__main__':
    path = input("Please input your image path: ")
    img = Image.open(path)
    add_num2pic(img)
