from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()
result = urlopen('http://pythonscraping.com/pages/warandpeace.html'
    , context=context)
bs = BeautifulSoup(result.read(), "html.parser")
#전체 출력
print(bs)
#특정 태그 출력 
print(bs.h1.string)
#p 태그만 리스트로 생성하고 10번째 위한 p태그 소스 추출하기 
p_list=bs.find_all('p')
print(bs.select_one('.red').string)
