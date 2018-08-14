#css 셀렉터 찾기
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
    <ul id='linkBox'>
        <li class='linkBox2'><a href='http://naver.com'>Naver</a></li>
    <div><img src=".png" alt="naver"></div>
             
    </body>
</html>
"""
bs=BeautifulSoup(html,'html.parser')
#print(bs.select_one('css셀렉터'))#1개 
#문서에서 ul태그 있는 첫번째 li 추출
print(bs.select_one('ul li'))
#문서에서 div태그 아래에 있는 첫번째 img추출
print(bs.select_one('div img'))
print(bs.select_one('#linkBox li a'))
#linkBox아이디 갑을 가진 ul태그안에 있는 nateclass 값을 가진 li 태그 안에 있는 a 태그
#li태그에서 다시 아래에 있는 첫번째 a 추출
print(bs.select_one('#linkBox .nateClass a'))
print(bs.select_one('div#linkBox li.nateClass a'))


#