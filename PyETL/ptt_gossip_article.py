# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:01:20 2020

@author: User
"""


import requests
from bs4 import BeautifulSoup
import os




headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ss = requests.session()
ss.cookies['over18'] = '1'

if not os.path.exists('ptt_gossiping'):
    os.mkdir('ptt_gossiping')
    
    

for f in range(0,5):
    #按入內文
    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    title_list = soup.select('div.title')
   
    
    for title_soup in title_list:
        try:
            #get article title
            title_name = title_soup.select('a')[0].text
            
            # Extract article content
            
            article_url = 'https://www.ptt.cc'+title_soup.select('a')[0]['href']
            
            res_article = ss.get(article_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, 'html.parser')
                                                  
            author = soup_article.select('span.article-meta-value')[0].text
            title = soup_article.select('span.article-meta-value')[2].text
            datetime = soup_article.select('span.article-meta-value')[3].text
            
            push = 0
            down = 0
            score = 0
            push_info_list = soup_article.select('div.push')
            
            for info in push_info_list:
                if '推' in info.text:
                    push += 1
                if '推' in info.text:
                    down += 1
            
            score = push - down
            
            article_cont = soup_article.select('div#main-content')[0].text.split('※ 發信站')[0]
            
            article_cont += '\n---split---\n'
            article_cont += '推: {}\n'.format(push)
            article_cont += '噓: {}\n'.format(down)
            article_cont += '分數: {}\n'.format(score)
            article_cont += '作者: {}\n'.format(author)
            article_cont += '標題: {}\n'.format(title)
            article_cont += '時間: {}\n'.format(datetime)
            
            n_article_title = title_name.replace('/','').replace('?','').replace(':','')
            
            with open('./ptt_gossiping/{}.txt'.format(n_article_title),'w',encoding = 'utf-8') as w:
                w.write(article_cont)
        
        except IndexError as e:
            print('============')
            print(title_name)
            print(article_url)
            print(e.args)
            print('============')
            
             
        #上一頁url
    url = 'https://www.ptt.cc' + soup.select('a.btn.wide')[1]['href']
        