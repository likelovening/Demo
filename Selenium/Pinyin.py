#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from xpinyin import Pinyin
p=Pinyin()
tao="涛涛"
taotao=p.get_pinyin(tao, '')
print(taotao)


#将汉字转换成对应的拼音
p=Pinyin()
转换的字="转换的字"
tao1=p.get_pinyin(转换的字,'')

