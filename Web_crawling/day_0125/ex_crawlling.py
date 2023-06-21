from urllib.request import urlopen

# html = urlopen('https://www.daangn.com/hot_articles')
# print(type(html))
#print(html.read())


from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(),	'html.parser')
print(bs)
print(bs.h1)
print(bs.title)





from urllib.error import HTTPError
from bs4	import BeautifulSoup

def getTitle(url,tag):
    try:
        html =	urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj =	BeautifulSoup(html.read(),	'html.parser')
        value =	bsObj.body.find(tag)
    except AttributeError as e:
        return None
    return value
tag =	'h2'
value =	getTitle('http://www.pythonscraping.com/pages/page1.html',	tag)
if value ==	None:
    print(f'{tag} could not be found')
else:
    print(value)



# 2장
html_example =	'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's	first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>

            <p id="second">class1's second	paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's	third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example	page
        <p>g</p>
    </div>
    <h1	id="footer">Footer</h1>
</body>
</html>
'''


from bs4	import BeautifulSoup
soup	=	BeautifulSoup(html_example,	'html.parser')
print(soup.title)	#	<title>	태그 전체를 가져옴
print(soup.title.text)	#	<title>태그의 텍스트만 리턴
print(soup.title.get_text())	#	.text와 동일한 기능


print(soup.title.parent)


print(soup.body)


print(soup.h1)
print(soup.h1.text)


print(soup.a)
print(soup.a.text) # <a>	태그 내부의 텍스트 추출 (google)
print(soup.a['href']) #	<a>	태그 내부의 href 속성의 url을 추출
print(soup.a.get('href')) #	a['href']와 동일 기능


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
print(soup.find('div'))

#find() 함수 사용
#여러 <div> 태그 중 특정 속성을 가지는 항목 추출
print(soup.find('div',	{'id':'text_id2'}))


#text 또는 get_text()
#추출된 요소에서 텍스트만 가져옴
div_text =	soup.find('div', {'id':'text_id2'})
print(div_text.get_text())


# <a> 태그 및 <a> 태그의 href 속성 추출
href_link =	soup.find('a', {'class':'internal_link'}) # 딕셔너리 형태
href_link =	soup.find('a',	class_	='internal_link') # class는 파이썬 예약어
print(href_link) # <a class=”internal_link”	…>	태그 전체를 추출
print(href_link['href'])# <a> 태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href')) # ['href']와 동일 기능
print(href_link.text) # <a>	Page1 </a>태그 내부의 텍스트(Page1) 추출



#<a> 태그 내부의 모든 속성(attrs)	가져오기
print('href_link.attrs:', href_link.attrs)# <a>태그 내부의 모든 속성 출력

#<a> 태그 내부의 속성의 값 가져오기: dict의 values() 호출
print('values():', href_link.attrs.values()) # 모든 속성들의 값 출력

values = list(href_link.attrs.values())	#	dictionary	값들을 리스트로 변경
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))

#class속성
#class 속성은 여러 개의 값을 가질 수 있음 (multi-valued	attribute)
#따라서 list 형태로 리턴함
print('class 속성값: ', href_link['class'])





from bs4	import BeautifulSoup
tr =	'''
<table>
<tr	class="passed	a	b	c"	id="row1	example"><td>t1</td></tr>
<tr	class="failed"	id="row2"><td>t2</td></tr>
</table>
'''
table =	BeautifulSoup(tr,	'html.parser')
for row in table.find_all('tr'):
    print(row.attrs)

#href 속성의 값이 ‘www.google.com’인 항목 검색
href_value = soup.find(attrs={'href' : 'www.google.com'})
print(href_value)
print(href_value['href'])
print(href_value.text)


#find()	함수
#span 태그의 속성 가져오기
span_tag = soup.find('span')
print('span	tag:', span_tag)
print('attrs:',	span_tag.attrs)	# attribute 속성 추출
print('value:',	span_tag.attrs['class']) # class 속성의 값 추출
print('text:', span_tag.text)



#모든 div 태그 검색
from bs4 import BeautifulSoup
html_example =	'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's	first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>

            <p id="second">class1's second	paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's	third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
    Example	page
    <p>g</p>
    </div>
    <h1	id="footer">Footer</h1>
</body>
</html>
'''
soup =	BeautifulSoup(html_example,	'html.parser')


# 전체 div 태그를 모두 검색 (리스트 형태로 반환)
div_tags =	soup.find_all('div')	
print('div_tags length:', len(div_tags))
for div in div_tags:
    print('-----------------------------------------------')
    print(div.text.replace('\n',' '))


# 모든 <a>	태그 검색 및 속성 보기
links=soup.find_all('a')

for	alink in links:
    print(alink)
    print('url:{0},	text:{1}'.format(alink['href'],	alink.get_text()))
    print()

# 특정 태그 중 여러 속성값을 한 번에 검색
# • 여러 <a>태그에서 2개의 class	속성값 검색:	
# ‘external_link’,	‘internal_link’만 검색
# – 검색할 속성값을 리스트 형태로 추가
# – {'class':['external_link',	'internal_link’]}
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)

#<p>태그의 id값이 ‘first’,	‘third’인 항목 검색

p_tags = soup.find_all('p', {'id': ['first', 'third']})

for	p in p_tags:
    print(p)


#  select_one()	예제
# • <head>태그 검색


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
head =	soup.select_one('head')
print(head.text.strip())




#첫 번째 <h1>태그 검색
h1 = soup.select_one('h1')	#	첫 번째 <h1>태그 선택
print(h1)

#select_one() 함수 예제
#<h1>태그의 id 검색: #id
#<h1>태그의 id가 "footer＂인 항목 추출
footer = soup.select_one('h1#footer')
print(footer)


# 클래스 이름 검색: 태그.클래스이름
# – <a class=“internal_link”	herf=“/pages/page1.html>Page1</a> 검색
class_link = soup.select_one('a.internal_link')
print(class_link)

print(class_link.text)
print(class_link['href'])


# 계층적 하위 태그 접근 #1
# • (상위태그 > 하위태그) 형식으로 접근:	태그가 단계적으로 존재할 때
link1 = soup.select_one('div#link > a.external_link')
print(link1)

#계층적 하위 태그 접근 #2
#(상위태그 하위태그) 형식으로 접근:	자손 관계의 하위태그
link2 = soup.select_one('div#class1	p#second')
print(link2)
print(link2.text)


# select()	함수
# 모든 <h1>	태그 검색
h1_all = soup.select('h1')
print(h1_all)

#모든 url 링크 검색
#	html문서의 모든 <a>	태그의 href 값 추출
url_links = soup.select('a')
for	link in url_links:
    print(link['href']) 


#<div id=“class1”> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')
print(div_urls)

print(div_urls[0]['href'])



#  여러 항목 검색하기
# select()함수
# • <h1>태그의 id가 ”heading”과 “footer”를 모두 검색
# – 쉼표(,)로 나열함
h1 = soup.select('#heading,	#footer')
print(h1)

#<a>태그의 class이름이 “external_link”와 ”internal_link”	모두 검색
url_links =	soup.select('a.external_link,a.internal_link')
print(url_links)


#select()함수
national_anthem = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            남산 위에
            저 소나무 철갑을 두른
            듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
    </div>
</body>
</html>
'''

#제목과 가사 내용 추출
soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').text)

contents = soup.select('p.content')
for	content	in contents:
    print(content.text)








