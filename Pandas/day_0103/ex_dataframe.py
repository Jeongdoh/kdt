#------------------------------------------------------------------------------------------------
#데이터 프레임 dataframe
# - 판다스 구조화 데이터 타입
# - 구성 : 행과 열
# - 요소 : 행인덱스, 열이름
#------------------------------------------------------------------------------------------------
# 패키지, 모듈 로딩
import pandas as pd

#DF 생성 실습
# 데이터 => LIST데이터 사용
data=[[10,20,30],['F','M','M']]

df1=pd.DataFrame(data)

# 데이터 확인 출력
print(f'df1 => \n{df1}')

print(f'df1.index => {df1.index}')
print(f'df1.columns => {df1.columns}')
print(f'df1.shape => {df1.shape}')
print(f'df1.ndim => {df1.ndim}')
print(f'df1.dtypes => {df1.dtypes}')
print(f'df1.values => \n{df1.values}\n{type(df1.values)}')



# 데이터 => Dict데이터 사용
data={'name':['홍','이','박'], 'job':['학생','학생','주부']}
df2=pd.DataFrame(data)

# 데이터 확인 출력
print(f'df2 => \n{df2}')

print(f'df2.index   => {df2.index}')
print(f'df2.columns => {df2.columns}')
print(f'df2.shape   => {df2.shape}')
print(f'df2.ndim    => {df2.ndim}')
print(f'df2.dtypes  => {df2.dtypes}')
print(f'df2.values  => \n{df2.values}\n{type(df2.values)}')
