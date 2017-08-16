#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0007: 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os

def count_code(path):

    files = os.listdir(path)
    for file in files:

        blankLine = 0
        codeLine = 0
        noteLine = 0
        allLine = 0

        filePath = os.path.join(path, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.py':
            with open(filePath) as f:
                for line in f.readlines():
                    allLine += 1
                    # 去掉字符串头和尾的空格，删掉位于头尾的\n \t等
                    if line.strip() == '':
                        blankLine += 1

                    elif line.startswith('#'):
                        noteLine += 1

                    else:
                        codeLine += 1

                print('File: %s————Total Line: %s' % (file, allLine))
                print('CodeLine:%s\nNoteLine:%s\nBlankLine:%s' % (codeLine, noteLine, blankLine))
                print('———————————————————————')

# Input your code file directory
count_code('/Users/patientman/PycharmProjects/class_test')
