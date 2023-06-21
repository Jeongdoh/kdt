from urllib.request import	urlopen
from bs4 import BeautifulSoup
import requests

html = requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
bs = BeautifulSoup(html.text, 'html.parser')
all=bs.select('a.tltle')

n=[]

naver_info=[]
for idx in range(10):
    naver_info.append(all[idx]['href'])
    n.append(all[idx].text)




while True:
    

    print('[ 네이버 코스피 상위 10대 기업 목록 ]')
    for i in range(len(n)):
        print(f'[{i+1:2}] {n[i]}')
    user=int(input("알고싶은 기업 : "))

    if user==-1:
        break
    
    if user in [1,2,3,4,5,6,7,8,9,10]:
        html = requests.get(f'https://finance.naver.com{naver_info[user-1]}')
        bs = BeautifulSoup(html.text, 'html.parser')
        all=bs.select('div#middle > dl > dd')
        print(f'https://finance.naver.com{naver_info[user-1]}')
        print(*all[1].text.split(' ')[0:2],sep=': ')
        print(*all[2].text.split(' ')[0:2],sep=': ')
        print(*all[3].text.split(' ')[0:2],sep=': ')
        print(*all[4].text.split(' ')[0:2],sep=': ')
        print(*all[5].text.split(' ')[0:2],sep=': ')
        print(*all[6].text.split(' ')[0:2],sep=': ')
        print(*all[8].text.split(' ')[0:2],sep=': ')

#