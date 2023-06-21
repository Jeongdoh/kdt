from urllib.request import	urlopen
from bs4 import BeautifulSoup

#find_all(tag,	attrs,	recursive,	text,	limit,	keywords)


html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DigkHP07c')


def scraping_use_find(html):
    html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DigkHP07c')
    bs	= BeautifulSoup(html.read(), 'html.parser')

    print(bs.find('a',{'id':'header-nws'}).find('img')['alt'],'Scraping')
    tombstone_container=bs.find_all('li',{'class':'forecast-tombstone'})
    print('-'*40)
    print('[find 함수 사용]')
    print('총 tomestone_container 검색 수 : ', len(tombstone_container))
    print('-'*80)

    for idx in tombstone_container:
        print('[Period]:',idx.find('p',{'class':'period-name'}).text)
        print('[Short desc]:',idx.find('p',{'class':'short-desc'}).text)
        print('[Temperature]:',idx.find('p',{'class':'temp'}).text)
        print('[Image desc]: ',idx.find('img')['title'])
        print('-'*80)

scraping_use_find(html)




def scraping_use_select(html):
    html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DigkHP07c')
    bs	= BeautifulSoup(html.read(), 'html.parser')

    print(bs.find('a',{'id':'header-nws'}).find('img')['alt'],'Scraping')
    forecast_tombstone=bs.select('li.forecast-tombstone')
    print('-'*40)
    print('[select 함수 사용]')
    print('총 forecast_tombstone 검색 수 : ', len(forecast_tombstone))
    print('-'*80)

    for idx in forecast_tombstone:
        print('[Period]:',idx.select_one('p.period-name').text)
        print('[Short desc]:',idx.select_one('p.short-desc').text)
        print('[Temperature]:',idx.select_one('p.temp').text)
        print('[Image desc]:' ,idx.select_one('img')['title'])
        print('-'*80)

scraping_use_select(html)