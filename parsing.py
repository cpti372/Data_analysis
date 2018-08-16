#데이터 분석가 기초 공부 
#parcing
print("hello,world!\t\t\n".strip())
#lsstrip-> 왼쪽 공백 제거 
#rstrip->오른쪽 공백 제거
#split->기준으로 나누기
print("-".join(['010','3398','3614']))
print("https://www.youtube.com/watch?v=L9bgo6W1DAE".find(".com"))

#set->회원 명단 조회 및 중복 항목 삭제 

mylist=list(set(mylist))#회원명단에서 중복된거 없애고 나서 리스트화 

biglist=[str(i)for i in range(1000000)]
"abc" in biglist # 리스트에서 분석할때

bigSet=set(biglist) #set 형태로 바꿈

#리스트 내포로 리스트 이해하기
[x for in mylist]
[x for in mylist if x>=0]
[x**2 for x in mylist]

#카운터로 세기 : 딕셔너리에서 자주 쓰임->pandas기반
from collections import Counter
phrase="a man a plan a canal panama"
cntr=Counter(phrase.split())
print(cntr.most_common())


#pickle 사용시 바이너리 모드에서 읽는거 
f.read()#바이너리 형태로 읽기
f.read(n)#첫번째 n개의 바이트를 문자열이나 바이너리 형태로 읽는다
f.readlind()#다음줄을 문자열로 읽는다
f.readlines()#모든줄을 문자열 리스트로 읽는다

#웹에 접근하기 
import urllib.request
try:
    with urllib.request.urlopen(https://www.youtube.com/watch?v=D6k39YULxRg)as doc:
        html=doc.read()
except:
    print("could not open")

#웹 페이지 파싱하기
import urllib.parse
URL="https://www.google.co.kr/"
urllib.parse.urlparse(URL)

#ParseResult(scheme='https', netloc='www.google.co.kr', path='/', params='', query='', fragment='')



