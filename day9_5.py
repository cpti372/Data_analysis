#아래 사이트 주소의 작품 부분만 데이터 추출하기 
#https://namu.wiki/w/%EC%9C%A4%EB%8F%99%EC%A3%BC
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()
html=urlopen('https://namu.wiki/w/%EC%9C%A4%EB%8F%99%EC%A3%BC',context=context)
bs= BeautifulSoup(html,"html.parser")
#print(bs)

result_list= bs.select('body > div.content-wrapper > article > h1 > a > span')
print(result_list)
for i in result_list:
    print(i.string)#i만 찍으면 하이퍼링크 소스가 나옴

                   