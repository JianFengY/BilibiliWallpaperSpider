# -*- coding: utf-8 -*-
'''
Created on 2017年10月20日

@author: Jeff Yang
'''
import requests
from urllib.request import urlretrieve
# import json

url = "http://h.bilibili.com/wallpaperApi?action=getOptions&page=1"
html = requests.get(url)
# print(type(html))
# content = json.loads(html.text)
content = html.json()

path = 'D:/Wallpaper/'
i = 1
while i <= len(content) - 1:
    src = content[i]['detail'][0]['il_file']
    print('Downloading ' + content[i]['detail'][0]['title'] + ' ……')
    urlretrieve(src, path + str(i) + src[-4:])
    i = i + 1
print('Done!')
