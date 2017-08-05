#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问题 0006: 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
import os
import re

def findWord(path):
    if not os.path.isdir(path):
        return 'not path'
    fileList = os.listdir(path)
    reObj = re.compile('\b?(\w+)\b?')
    for file in fileList:
        filePath = os.path.join(path, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt':
            with open(filePath) as f:
                data = f.read()
                words = reObj.findall(data)
                wordDict = dict()
                for word in words:
                    word = word.lower()
                    if word in ['a', 'the', 'of', 'to', 'and']:
                        continue
                    if word in wordDict:
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
            ansList = sorted(wordDict.items(), key=lambda t:t[1], reverse=True)
            print('file: %s->the most word: %s' % (file, ansList[1]))

if __name__ == '__main__':
    findWord('txt')
