
import pandas as pd
from urllib.request import	urlopen
from bs4 import BeautifulSoup

hollys_info=[]
for n in range(1,54):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={n}&sido=&gugun=&store=')
    bs = BeautifulSoup(html.read(), 'html.parser')

    all=bs.select('tbody > tr')

    for idx in range(len(all)):
        store=all[idx].select('td')
        h=[]
        h.append(store[1].text)
        h.append(store[0].text)
        h.append(store[3].text)
        h.append(store[5].text)
        hollys_info.append(h)


hollys_table = pd.DataFrame(hollys_info, columns=('매장이름', '위치(시,구)', '주소', '전화번호'))
hollys_table.to_csv('./hollys_branches.csv', encoding='utf-8', mode='w', index=True)

