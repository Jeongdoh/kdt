#------------------------------------------------------------------------------------------
# 데이터 분석 => 기초 통계함수들, 고유값, 결측치
#------------------------------------------------------------------------------------------
import pandas as pd

FILE=r'dataFiles\dataFiles\auto-mpg.csv'

# 데이터 정보확인 함수----------------------------------------------------------------------
def printDataInfo(df):
    df.info()
    print(df.head(), df.tail(), sep='\n', end='\n\n')
    print(df.describe(), end='\n\n')
    print(f'Index=> {df.index}\nColumns => {df.columns}', end='\n\n')

# (1) FILE => Dataframe 읽기
mpgDF=pd.read_csv(FILE, header=None)

# (2)데이터 확인
printDataInfo(mpgDF)

# (3) 컬럼명 추가
# 'mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name'
mpgDF.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
print(mpgDF.head(3))


#(4) 실제 데이터와 맞지 않는 타입의 데이터를 타입 맞춰주기
# horsepower => 데이터 값 중에 '?'가 들어있엉서 에러남
# (4-1) 해당 컬럼에 데이터 종류 확인 => 고유값 확인 unique()
horseUnique=mpgDF.horsepower.unique()
print(f'horseUnique :{horseUnique}')

# (4-2) 해당 컬럼의 데이터 종류별 갯수 확인
horseValueCount=mpgDF.horsepower.value_counts()
print(f'horseValueCount :{horseValueCount, type(horseValueCount)}')
print(horseValueCount['?'])

# print('horsepower dtype : ', mpgDF.horsepower.dtype)
# mpgDF.horsepower.astype('float64')
# print('horsepower dtype : ', mpgDF.horsepower.dtype)
















