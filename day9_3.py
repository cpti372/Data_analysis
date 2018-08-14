# 필요한 모듈 불러오기  
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 웹상에 있는 페이지 이용
# 웹상의 페이지를 변수로 저장 
html = urlopen('http://pythonscraping.com/pages/warandpeace.html') 
# print(html.read())
# 뷰티풀숲 변수로 웹상의 태그 소스와 연결 
bs= BeautifulSoup(html.read(),"html.parser")
print(bs)
print('\n'*10)

# 웹페이지에서 [Copy selector]기능으로 선택자 복사 
#   #text > span
print('#text > span 소스 확인하기')
print(bs.select_one('#text > span'))


# 뷰티풀숲 사용시 주의 사항 
# nth-child(), first-child, last-child
# #text > p:nth-child(2) > span:nth-child(1)
# #text p span.green
# text 아이디를 가진 태그에서 
# green 클래스가 적용된 태그 
print(bs.select_one('#text .green'))
print('*'*30)
print(bs.select_one('#text > span').string)

'''
퀴즈 - 
1. h1 태그안의 텍스트 추출
2. p 태그만 리스트로 생성하고 10번째 위한 p태그 소스 추출하기 
3. 첫번째 red 클래스가 적용된 텍스트 추출하기  
'''