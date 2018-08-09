# 필요한 모듈 불러오기  
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = """
<html>
    <body>
    <h1 id='title'>Hello Python</h1>
    <p id='body'>웹페이지 분석</p>
    <p>웹스크래핑</p>
    <ul>
        <li class='fruit'>사과</li>
        <li>양파</li>
        <li>고구마</li>
        <li class='fruit'>바나나</li>
    </ul>
    <ul>
        <li><a href='http://naver.com'>Naver</a></li>
        <li><a href='http://nate.com'>Nate</a></li>
        <li><a href='http://google.com'>Google</a></li>
        <li><a href='http://yahoo.com'>Yahoo</a></li>
        <li><a href='http://daum.com'>Daum</a></li>
    </ul>
    <div>
       <img src="images/naver.png" alt="naver">
       <img src="images/google.png" alt="google">
       <img src="images/coupang.png" alt="coupang">
       <img src="images/daum.png" alt="daum">
    </div>
    </body>
</html>
"""
# 뷰디풀숲 객체 생성 
bs= BeautifulSoup(html,"html.parser")
# 전체 소스 출력
print(bs)
# 도트(.)로 태그 찾아가기 
# bs.태그명.태그명2... : 첫번째 태그 소스 찾기 
print('태그소스 = ', bs.p)
print('태그 소스안의 텍스트',bs.p.string)
# 아이디로 찾아가기 
# bs.find(id='아이디이름')
print('아이디가 title인 태그 소스 : ', bs.find(id='title'))
print('아이디가 title인 태그의 텍스트 : ', bs.find(id='title').string)
# 클래스로 찾아가기 - 리스트 구조
# bs.find_all(class_='클래스명')
result_list=bs.find_all(class_='fruit')
print(result_list)
for i in result_list:
    print(i)
print('-'*30,'\n\n')    
# 문서에 삽입된 태그 여러개 찾아가기 - 리스트구조 
# bs.find_all('태그명')
li_list = bs.find_all('li')
print(li_list)
for i in li_list:
    print('태그소스',i)   
    print('태그안의 텍스트',i.string) 
# 하이퍼링크 a 태그안의 href 속성값 추출하기 
# 태그의리스트변수.attrs['속성값']
a_list = bs.find_all('a') 
href_list = []
print('하이퍼링크 태그 리스트', a_list)   
for i in a_list:
    print(i.attrs['href'])
    h = i.attrs['href'] # 텍스트로 추출 
    href_list.append(h)
print('하이퍼링크 url 리스트',href_list)    

'''
img 태그의 src 속성값을 추출해서 리스트로 만든다. 

출력형태 :
   img태그소스 - src 속성값
   <img src="images/naver.png" alt="naver">  : images/naver.png
   ...

'''