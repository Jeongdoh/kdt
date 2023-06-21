# urllib.request 라이브러리
# • urlretrieve() 함수 원형
# – url로 표시된 네트워크 객체를 로컬 파일로 복사
# – filename:	복사할 파일 위치 및 이름 지정
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import	BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
home_image = bs.find('img', {'class':'pagelayer-img'})
image_location = home_image['src'] # <img>	태그의 ‘src’ 속성값을 가져옴

print(image_location)
urlretrieve(image_location,	'logo.jpg')




















