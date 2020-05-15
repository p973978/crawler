# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:46:28 2020

@author: User
"""


from urllib import request


url = 'https://www.ptt.cc/bbs/joke/index.html'

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
headers = {'User-Agent':useragent}
# res = request.urlopen(url) # 沒有headers 會被拒絕
req = request.Request(url, headers=headers)
res = request.urlopen(req)


print(res.read().decode('utf-8'))

soup = 