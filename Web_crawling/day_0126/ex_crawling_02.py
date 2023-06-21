# CSS	속성을 이용한 태그 검색 (등장 인물 검색)
from urllib.request import	urlopen
from bs4 import	BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, "html.parser")
# 등장인물의 이름: 녹색
nameList = soup.find_all('span', {'class': 'green'})
for	name in nameList:
    print(name.get_text())

# find_all(text=“검색어”)
# • 대소문자 구분
# • 검색어:
# ‘the	prince’
from	urllib.request import	urlopen
from	bs4	import	BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')
princeList = soup.find_all(text='the prince')
print(princeList)
print('the prince count:',	len(princeList))

# 트리 이동
# • 문서 내부에서 특정 위치를 기준으로 태그를 찾을 때
# • 단방향으로 트리 이동
# 자식: children
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,	'html.parser')
table_tag =	soup.find('table', {'id':'giftList'})
for	child in table_tag.children:
    print(child)

# 트리 이동
# • 문서 내부에서 특정 위치를 기준으로 태그를 찾을 때
# • 단방향으로 트리 이동
# 자손: descendants
desc = soup.find('table', {'id':'giftList'}).descendants
print('descendants 개수: ', len(list(desc)))

for	child in soup.find('table', {'id':'giftList'}).descendants:
    print(child)

# 형제: next_siblings 속성
# • 임의의 행을 선택하고 next_siblings을 선택하면,
# – 테이블의 다음 행들을 모두 선택 (모든 형제를 선택)
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
for	sibling	in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

# previous_siblings 속성
# • 선택된 행 이전의 항목들을 선택
for	sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)

# next_sibling,	previous_sibling
# • 태그 하나만 반환
# • 문자열 마지막에 whitespace(‘\n’, ‘\r’등)가 있는 경우
# – 해당 whitespace를 next_sibling으로 반환
sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print(ord(sibling1)) # ord(문자): 문자의 Unicode 정수를 리턴
sibling1

#next_sibling.next_sibling 이용
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)

#parent 사용
style_tag = soup.style
print(style_tag.parent)

#  .parent 사용
# • parent:	부모 tag를 먼저 검색(<td>)
# • previous_sibling:	부모 태그이 이전 형제 태그 검색
# • get_text():	태그 내부의 문자열 반환
img1 = soup.find('img',	{'src':	'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)



# 정규 표현식 객체 사용:	
# • 정규식 객체를 생성: compile(pattern)
# – 동일 패턴을 여러 번 검색하는 경우, 편리하게 사용
# – re모듈 함수들은 pattern 파라미터 없이 호출이 가능
# Ø search(string,	pos),	match(string,	pos) 등

import	re

# compile()	사용 안함
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))


# compile() 사용
p = re.compile('[a-z]+') # 알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

# findall() 함수
# • 일치하는 모든 문자열을 리스트로 리턴
p = re.compile('[a-z]+') # 알파벳 소문자
print(p.findall('life is too short'))

# search()	함수
# • 일치하는 첫 번째 문자열만 리턴
result = p.search('I like apple 123')
print(result)
print(result.group()) # group(): 일치하는 전체 문자열 리턴
result = p.findall('I like apple 123')
print(result)


# § 전화번호 분석
# • 전화번호:
# ‘지역번호-국번-전화번호’
# – 전화번호: (2, 3자리)-(3, 4자리)-(4자리)
# – 예: 02-123-4567, 053-123-1234

import	re
#	^	..	$	을 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
print(tel_checker.match('02-123-4567'))
print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))

m = tel_checker.match('02-123-4567')
print(m.groups())

# • group()
# – 매칭된 전체 문자열 반환
# • group(index)
# – 해당 인덱스에 매칭된 문자열 반환
# – index=0:	전체 리턴
m = tel_checker.match('02-123-4567')
print('group():', m.group())
print('group(1):', m.group(1))
print('group(2,3)', m.group(2,3))
print('start():', m.start())	#	매칭된 전체 문자열의 시작 인덱스
print('end():',	m.end())	#	마지막 인덱스 +	1

# § 휴대전화번호
# • 휴대전화번호 구성:
# ‘사업자번호(3자리)-국번(3,4자리)-전화번호(4자리)’
# – 사업자 번호: 010,	011,	016,	017,	018,	019
# – 예: 010-123-4567,	011-1234-5678,	019-111-2222
# • (?:0|1|[6-9])	의미
# – ?:	뒤에 따라 나오는 숫자(0|1|6|7|8|9)를 하나의 그룹으로 합침
cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')
print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))


# § 전방 긍정 탐색 (?=패턴)
# • 패턴과 일치하는 문자열을 만나면 패턴 앞의 문자열 반환
# § 전방 부정 탐색 (?!패턴)
# • 패턴과 일치하지 않는 문자열을 만나면 해당 문자열 반환

import	re
#	전방 긍정 탐색:	(문자열이 won을 포함하고 있으면 won	앞의 문자열 리턴)
lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')

lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2)

#	전방 부정 탐색 (?!): 4자리 숫자 다음에 '-'를 포함하지 않으면 앞의 문자열 리턴
lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)


# BeautifulSoup의 문자열을 받는 함수들
# • 정규 표현식을 매개 변수로 받을 수 있음
# § 제품 이미지 검색:
# • <img src=“...”> 태그의 속성[‘src’] 사용

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup =	BeautifulSoup(html,	'html.parser')

#	정규식:	('img.*\.jpg'):	img 다음에 임의의 한 문자가 0회 이상:		img.jpg,	img1.jpg,	imga.jpg 등
img_tag = re.compile('/img/gifts/img.*.jpg')

#	find_all()에서 img의 src 속성값에 정규식 사용
images = soup.find_all('img', {'src': img_tag})

for image in images:	
    print(image, end=" -> ['src'] 속성: ")
    print(image['src'])




