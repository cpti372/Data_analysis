'''
네이버 영화 랭킹 
1~3위까지 출력하기 
https://movie.naver.com/movie/sdb/rank/rmovie.nhn
''' 

# 필요한 모듈 불러오기  
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn') 
bs= BeautifulSoup(html.read(),"html.parser")
# 전체 페이지 소스 확인하기 
# print(bs)
# 순위 소스 출력 
# print(bs.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'))
rank_list = bs.select('#old_content > table > tbody > tr > td.title > div > a')
# old_content > table > tbody > tr > td.title > div > a
for i in rank_list:
    print(i.string)    
# # 1 ~ 3위까지 출력하기 
# print('-'*5)
for i in range(0,3):
    print('{}위 {}'.format(i+1,rank_list[i].string)) 

   