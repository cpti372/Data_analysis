# 아래 사이트 주소의 작품 부분만 데이터 추출하기 
# 윤동주 - 나무위키
# https://namu.wiki/w/윤동주 

# 필요한 모듈 불러오기  
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://namu.wiki/w/%EC%9C%A4%EB%8F%99%EC%A3%BC') 
bs= BeautifulSoup(html.read(),"html.parser")
# 전체 페이지 소스 확인하기 
# print(bs)

# 작품 부분의 선택자 : nth-child(), first-child(), last-child() 인식 못함
# body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > ul > li > ul > li > p > a
# body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > ul > li > ul > li > p > a

print(bs.select('div.content-wrapper > article > div.wiki-content.clearfix > div > div > ul > li > ul > li > p > a'))

result_list = \
  bs.select('div.content-wrapper > article > div.wiki-content.clearfix > div > div > ul > li > ul > li > p > a')

for i in result_list:
    # print(i) # a 소스 출력 
    # 제목만 출력 
    print(i.string)

'''
윤동주 추출하기 

body > div.content-wrapper > article > h1 > a > span

'''
# 리스트로 출력
print(bs.select('body > div.content-wrapper > article > h1 > a > span'))
list_title = bs.select('body > div.content-wrapper > article > h1 > a > span')
print(list_title[0].string)

'''
네이버 실시간 검색 순위 출력하기 
'''
