import pandas as pd
import random as r

#1번 Series 데이터를 생성 후 정보를 출력해주세요
# -데이터 : 1~100사이 임의의 숫자 30개로 구성
a=[]

while True:
    l=r.randint(1,100)
    a.append(l)

    
    if len(a)==30:
        break

sr1=pd.Series(a)
print(sr1) 






print(f'--------------------------------------------------------------')
#2번 Series 데이터를 생성 후 정보를 출력해주세요
# -데이터 : 1~100 사이 임의의 숫자 30개로 구성
# -조 건 : 중복된 숫자 없음

print(f'방법1--------------------------------------------------------------')


a=set()

while True:
    l=r.randint(1,100)
    a.add(l)

    
    if len(a)==30:
        break
a=list(a)
sr1=pd.Series(a)
print(sr1) 




print(f'방법2--------------------------------------------------------------')

#방법2
a=[]

while True:
    l=r.randint(1,100)
    if l not in a:
        a.append(l)

    
    if len(a)==30:
        break

sr1=pd.Series(a)
print(sr1) 





#3번 Series 데이터를 생성 후 정보를 출력해주세요.
# 데이터 : 0.0 ~ 1.0 사이 실수 데이터 10개로 구성

import random as rm




# 지정된 범위는 1,10
a=[]



for _ in range(10):
    a.append(round(rm.random(), 1))
print(*a)
sr2=pd.Series(a)
print(sr2)



