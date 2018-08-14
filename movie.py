#영화 순위 출력하기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()
html=urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn',context=context)
bs= BeautifulSoup(html.read(),"html.parser")
ranklist=bs.select('#old_content > table > tbody > tr > td.title > div')
print(ranklist)
for i in ranklist:
    print(i.string)
for i in range(0,4):
    print('{}위{}'.format(i+1,ranklist[i].string))
