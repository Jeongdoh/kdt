#%%
import pandas as pd

FILE='hollys_branches.csv'

hollysDF=pd.read_csv(FILE, encoding='utf-8')

hollysDF.info()


while True:
    where=input("지역을 선택하세요 : ")
    if where=='quit':
        break
    tmp=hollysDF[hollysDF['위치(시,구)'].str.contains(where)]
    print(f'검색된 매장 수 : {len(tmp)}')
    for i in range(len(tmp)):
        temp=list(tmp.iloc[i])
        print(f'[ {i+1}]: {temp[-2:]}')




