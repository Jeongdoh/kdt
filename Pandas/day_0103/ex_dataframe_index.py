#--------------------------------------------------------------------------------------------------
# 인덱스(Index) 다루기
#--------------------------------------------------------------------------------------------------
# 모듈/패키지 로딩----------------------------------------------------------------------------------
import pandas as pd

# DF 생성-------------------------------------------------------------------------------------------

df1=pd.DataFrame({'name':['마징가','베트맨','원더우먼'],
                'kor':[87,91,69],
                'eng':[99,73,89],
                'sci':[71,95,62]})

#df 데이터 확인하기
print(f'df1========================>\n{df1}')
print(f'df1.index=>{df1.index}')
print(f'df1.columns=>{df1.columns}')


# [1] 특정 컬럼을 행 인덱스 설정=====================================================================
# DataFrame.set_index()메서드
# 'name'컬럼을 행 인덱스로 설정
nameDF2=df1.set_index('name')
print(f'df1========>\n{df1}')
print(f'nameDF2===========>\n{nameDF2}')


# 모든 행에 대한 값을 출력 => DF.loc[행인덱스]
for rIDX in nameDF2.index:
    print(rIDX, nameDF2.loc[rIDX], sep='\n', end='\n\n')

print('-'*50)
sr1=nameDF2.loc['마징가']
print(type(sr1), sr1, sep='\n')


# [2]인덱스 부분 변경================================================================================================
# 전체 변경 => DF.index=[새로운 인덱스], DF.columns=[새로운 인덱스]
# DataFrame.rename()메서드

# 행 인덱스: '마징가' '베트맨' '원더우먼' ==> '베트맨' ----->'홍길동'
copyDF=df1.rename(index={'베트맨':'홍길동'})
print(copyDF, end='\n\n')


df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df)


# 열(columns) 인덱스 변경
df.rename(columns={'B':'BB'}, inplace=True)
print(df)

# 행(row) 인덱스 변경 => 10, 20, 30 변경
df.rename(index={0: 10, 1:20, 2:30}, inplace=True)
print(df)


# 행(row) 인덱스 변경 => 10, 20, 30 => '10', '20', '30' 변경
df.rename(index=str, inplace=True)
print(df.index)


# [3] 새로운 인덱스 지정 설정=============================================================
# DaraFrame.reindex([새로운 인덱스])
# 기존 인덱스랑 갯수나 이름 다를 수 있음
# => 기존 인덱스가 아닌 인덱스의 값은 존재 하지 않음 => NaN : not a number 의 약자
newDF=df.reindex(['10','15','20','25'])
print('원본      DF => ', df, end='\n\n')
print('변경된 인덱스 => ',newDF,end='\n\n')


newDF=df.reindex(['10','15','20','25'], method='ffill')
print('원본      DF => ', df, end='\n\n')
print('변경된 인덱스 => ',newDF,end='\n\n')



# NaN값을 내가 원하는 값으로 채우기 -> fill_value=값
newDF=df.reindex(['10','15','20','25'], fill_value='nothing')
print('원본      DF => ', df, end='\n\n')
print('변경된 인덱스 => ',newDF,end='\n\n')



# [4] 판다스에서 지정하는 기본 인덱스로 초기화 설정=============================================================
# DaraFrame.reset_index()
# 기존 인덱스==> 컬럼으로 추가 [기본값]
newDF2=newDF.reset_index()


print(newDF2)

newDF2=newDF.reset_index(drop=True)


print(newDF2)













