# encoding: utf-8
import jieba
words=jieba.posseg.cut("我爱北京天安门")
for w in words:
    if w.flag == 'ns':
        print w
