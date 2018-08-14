# day9_4.py
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
    <ul id='linkBox'>
        <li><a href='http://naver.com'>Naver</a></li>
        <li class='nateClass'><a href='http://nate.com'>Nate</a></li>
        <li><a href='http://google.com'>Google</a></li>
        <li><a href='http://yahoo.com'>Yahoo</a></li>
        <li><a href='http://daum.com'>Daum</a></li>
    </ul>
    <div>
       <img src="images/naver.png" alt="naver">
       <img src="images/google.png" alt="google" class="g">
       <img src="images/coupang.png" alt="coupang">
       <img src="images/daum.png" alt="daum" class="g">
    </div>
    <div class='imgBox'>
       <img src="images/naver.png" alt="naver">
       <img src="images/google.png" alt="google">
       <img src="images/coupang.png" alt="coupang" class="g">
       <img src="images/daum.png" alt="daum" class="g">
    </div>
    </body>
</html>
"""
# 뷰디풀숲 객체 생성 
bs= BeautifulSoup(html,"html.parser")

# bs.select('css 셀렉터')
# 리스트 구조로 결과값이 리턴
li_list = bs.select('ul li')
print(li_list)
print('li 태그는 몇번 사용되었나요? ', len(li_list))

# linkBox 아이디가 적용된 ul 안의 li
li_list2 = bs.select('ul#linkBox li')
print(li_list2)
print('li 태그는 몇번 사용되었나요? ', len(li_list2))

# 모든 img 태그의 리스트 생성 
img_list = bs.select('img')
print('img 태그는 몇번 사용되었나요? ', len(img_list))

# imgBox 클래스가 적용된 태그 안의 img 리스트 생성 
img_list2 = bs.select('.imgBox img')
print('img 태그는 몇번 사용되었나요? ', len(img_list2))

# 퀴즈 
'''
# g 클래스가 적용된 태그 소스와 함께 숫자 카운팅 함께 출력

1 - <img src="images/google.png" alt="google" class="g">
2 - ..

전체 갯수 : ? 개 

'''

g_class_list = bs.select('.g')
cnt = 1
for i in g_class_list:
    print(cnt,' : ', i)
    cnt += 1
print('전체 갯수 : ', len(g_class_list) )    