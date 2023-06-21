#----------------------------------------------------------------------
# 인덱스와 인덱스 라벨(네임) 살펴보기
# -인덱스 : 판다스 시스템에 지정하는 RangeIndex 정수형 (0-base)
# -인덱스 라벨(네임): 시리즈 객체 생성시 지정하는 인덱스
#----------------------------------------------------------------------
import pandas as pd

# Series 객체 생성------------------------------------------------------
# 데이터 :  1~20사이의 3의 배수
# 인덱스 : 문자 'a' ~ 'f'
#----------------------------------------------------------------------
data=list(range(3,21,3))
idx=['a','b','c','d','e','f']
idx2=[11,22,33,44,55,66]
mySR=pd.Series(data, index=idx2, name='Jumsu', dtype='float32')

print(mySR)


# 요소 1개 읽기 => 변수명[인덱스]
#print( mySR['a'] , mySR[0])
print(mySR[11], mySR[0])

#for idx in mySR.index: print(  mySR[idx])


#요소 여러개 읽기 => 변수명[인덱스1, 인덱스2,...]
#print( mySR[['a','b','f']] , mySR[[0,3,5]])
print( mySR[mySR.index[::2]])


# 범위지정 요소 읽기 => 변수명[시작:끝인덱스+1]
# 인덱스가 문자열인경우 [시작인덱스명 : 끝인덱스명]
#print( mySR['a':'d'] , mySR[0:3])
