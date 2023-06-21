#------------------------------------------------------------------------------------------------
#데이터 프레임 dataframe 요소 다루기
#------------------------------------------------------------------------------------------------
# 패키지, 모듈 로딩-------------------------------------------------------------------------------
import pandas as pd

#DF 생성 실습
# 데이터 => LIST데이터 사용
data=[[10,20,30],['F','M','M'],[11,22,33],[44,55,66],['A','B','C']]

df1=pd.DataFrame(data)
print(df1)
#ex)
#     0   1   2
# 0  10  20  30
# 1   F   M   M


#DF 요소/원소 다루기 열(columns)-------------------------------------------------------------------------------
# 열(column) 기준으로 요소
# 0번 컬럼 가져오기 => 변수명[컬럼]
print(f'columns => {df1.columns}')
one=df1[0]
print(f'one=> {one}')

print(f'one => {type(one)}\n{one}')

print('-----------------------------------------------')
for col in df1.columns:
    print(f'[{col}] => {type(df1[col])}\n{df1[col]}')

# 여러개 컬럼(열) 요소 가져오기 => 변수명[[컬럼1, 컬럼n]]   #인덱스로 빼오는 방법
# 0번, 2번 컬럼 가져오기
oneTwo=df1[[0,2]]
print(f'oneTwo => {type(oneTwo)}\n{oneTwo}')



print('-----------------------------------------------')

# 범위지정 후 요소 가져오기 => 변수명[[시작 : 끝+1]]    # 슬라이싱 방법이지만!!
# 0번, 1번 컬럼 가져오기
#실행해보면 범위지정 컬럼데이터 추출이 안됨!!
# oneZero=df1[0:2]        # 밑에 행만 추가, 빼기되는 방법
# print(f'oneZero => {type(oneZero)}\n{oneZero}')


# DF 요소/원소 다루기 열(columns)-------------------------------------------------------------------------------
# 데이터프레임의 컬럼속성변경하기 ==> 변수명.속성명=새로운값
df1.columns=['One','Two','Three']
print(f'변경확인 : {df1.columns}')



# 'One' 컬럼 가져오기 => 변수명[컬럼], 변수명.컬럼명
# 단, 컬럼이 문자열str인 경우
# 단, 1개 컬럼만 가능
print(f'[df1["One"]]=>{type(df1["One"])}\n{df1["One"]}')
print(f'[df1.One]=>{type(df1.One)}\n{df1.One}')

# 컬럼인덱스 변경 후 기본 인덱스 사용 불가
#print(f'[df1[0]]=>{type(df1[0])}\n{df1[0]}')




# DF 요소/원소 다루기 행(row)-------------------------------------------------------------------------------
# 변수명.iloc[인덱스] : 반드시 정수형 인덱스만 가능     # 행의 [순서]를 불러오는 방법
# 변수명.loc[인덱스] : 문자열 인덱스 가능           # 행의 [이름]을 가지고 불러오는 방법
# 0번 행 데이터 가져오기
print(f'----------------\n{df1}')
zeroRow=df1.iloc[0]
print(f'[zeroRow] => {type(zeroRow)}\n{zeroRow}')



# 2개 행 데이터 가져오기 ==> 변수명.iloc[[인덱스, 인덱스]]
zeroTwoRow=df1.iloc[[0,1]]
print(f'[zeroTwoRow] => {type(zeroTwoRow)}\n{zeroTwoRow}')


# 범위지정 데이터 가져오기 ==> 변수명.iloc[시작 : 끝+1]
#                             변수명[시작 : 끝+1]
oneThree=df1.iloc[1:4]
print(f'[oneThree] => {type(oneThree)}\n{oneThree}')


# 슬라이싱을 하면 row를 가져오는걸 알수있음
oneThree2=df1[1:4]
print(f'[oneThree2] => {type(oneThree2)}\n{oneThree2}')



# 행(row) 인덱스 속성 변경 후 행 추출----------------------------------------------------------------------
df1.index=['A','B','C','D','E']
print(f'행 인덱스 속성 변경 => {df1.index}')

zeroRow1=df1.loc['A']
zeroRow2=df1.iloc[0]

# 요소 / 원소 (element) 추출하기---------------------------------------------------------------------------

print(f'----------------------------------------------')
print(df1)
print(f'----------------------------------------------')

# 사용법 : 변수명.iloc[행인덱스, 열인덱스], 변수명.iloc[행인덱스] [열인덱스]    # 정수 숫자
# 사용법 : 변수명.loc[행인덱스, 열인덱스], 변수명.loc[행인덱스] [열인덱스]      # 추가 변경
# 요소값이 33인 데이터 추출, 22인 데이터 추출
v33=df1.loc['C', 'Three']
v22=df1.loc['C'] ['Two']

print(f'v33 => {v33}, v22 => {v22}')


# 요소값이 44, 66인 데이터 추출
v4466=df1.loc['D',['One','Three']]

print(f'v11 => {v4466}, v22 => {v4466}')

# 요소값이 20, 30, 22, 33인 데이터 추출
values=df1.loc[['A','C'],['Two','Three']]
print(f'values => \n{values}')

values1=df1.iloc[[0,2], [1,2]]
print(f'values1 => \n{values1}')


