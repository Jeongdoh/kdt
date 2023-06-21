#<div id=“class1”> 내부의 모든 url 검색
# div_urls = soup.select('div#class1 > a')
# print(div_urls)

# print(div_urls[0]['href'])


from urllib.request import	urlopen
from bs4 import BeautifulSoup

html = urlopen('https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')

def D_weather(html):
    html = urlopen('https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')
    bs	= BeautifulSoup(html.read(), 'html.parser')

    print('현재 위치: ',bs.select_one('div._area_panel').select_one('h2.title').text)
    print('현재 온도: ',bs.select_one('div.temperature_text').text)
    print('날씨 상태: ',bs.select_one('div.temperature_info').select_one('p.summary').select_one('span.before_slash').text)
    print('공기 상태: ')
    li_today=bs.select('li.item_today')
    for i in range(0,4):
        print(li_today[i].text)
    print('-'*35)    
    print('시간대별 날씨 및 온도')
    print('-'*35)
    h_weather=bs.select('div._hourly_weather > ul > li._li')
    for i in h_weather:
        print(i.text.strip())
D_weather(html)