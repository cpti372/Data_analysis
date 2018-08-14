from urllib.request import urlopen
from bs4 import BeautifulSoup
html="""
<html>
    <body>
    <h1 id='title'>hello</h1>
    <p id='body'>웹 페이지 분석 </p>
    <p>웹 스크래핑</p>
    <ul>
        <li class_='fruit'>사과</li>
        <li>양파</li>
        <li>고구마</li>
        <li class_='fruit'>바나나</li>
    </ul>
    <ul>
             
    </body>
</html>
"""

#하이퍼 링크 a 태그 안의 href 속성값 추출하기
#태그의 변수._atters[속성값]
bs=BeautifulSoup(html,'html.parser')
print(bs)
print(bs.p)
print(bs.p.string)
print('태그 소스= ',bs.p)
print(bs.find(id='title'))
print(bs.find(id='title').string)
result_list=bs.find_all(class_='fruit')
print(bs.find_all(class_=''))
for i in result_list:
    print(i)
print('-'*30,'\n\n')
#문서에 삽입된 태그 여러개 찾아가기-리스트 구조
bs.find_all('태그명')
li_list=bs.find_all('li')
print(li_list)
for i in li_list:
    print(i)# 단순하게 소스출력
    print(i.string)#텍스트를 출력 원할때

a_list=bs.find_all('a')
href_list=[]
print(a_list)
for i in a_list:
    print(i.attrs['href'])
    href_list.appdnd(h)
print(href_list)

img_list=[]
for i in img_list:
    print(i)
    h=i.attrs['src']#텍스트로 추출
    img_src_list.append(h)
print(img_src_list)