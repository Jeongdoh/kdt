#-----------------------------------------------------------------------------------------------
# csv file ==> dataframe 객체로 저장
# -pandas.read_csv(경로파일명)
#-----------------------------------------------------------------------------------------------
import pandas as pd

FILE=r'dataFiles-20230103T063936Z-001\dataFiles\banklist.csv' # or 'dataFiles-20230103T063936Z-001\\dataFiles\banklist.csv'

# DF객체 생성------------------------------------------------------------------------------------
bankDF=pd.read_csv(FILE)

print(f'bankDF==> \n{bankDF}')


# DF 데이터 확인용 메서드-----------------------------------------------------------------------------
# [1] 전체 요약 정보 제공 메서드 => info()메서드
bankDF.info()


# [2] 앞부분 5줄 (기본값) 실제 데이터 보기 => head(n)메서드
#     끝부분 5줄 (기본값) 실제 데이터 보기 => tail(n)메서드
print(bankDF.head(), bankDF.tail(3), sep='\n\n')


# [3]데이터의 기술통계를 적용한 결과 제공=> 데이터 분포 확인 => describe()메서드
#    수치 데이터만 가능(기본값)
#    모든 데이터 가능 (include='all')
# print(bankDF.describe())
print(bankDF.describe(include='all'))




# 데이터 가지고 놀기!
print(f'bankDF.columns=> {bankDF.columns}')

# (1) 4개 컬럼 => 'Bank Name','City' ,'Closing Date', 'Updated Date'
newDF=bankDF[['Bank Name','City' ,'Closing Date', 'Updated Date']]
print(newDF.info())
print(newDF.head(3))

# (2) 컬럼 중에서 인덱스로 설정 => set_index([])
newDF.set_index(['Bank Name','City'], inplace=True)
print(newDF.index, newDF.columns, sep='\n', end='\n\n')
print(newDF.head(3))

# (3) 'Updated Date' 기준으로 가장 최근 날짜부터 정렬해서 보여주세요.
# 가장 최근날짜 => 내림차순 (ascending=False)
# object ==> str ==============> datetime
newDF.sort_values(by=['Updated Date'], key=lambda col : pd.to_datetime(col), ascending=False, inplace=True)
print(newDF['Updated Date'].values)









# print('*'*50)

# #(1)
# bankCol=bankDF.columns[[0,1,5,6]]
# print(f'bankCol => \n{bankCol}')

# #(2)
# bankIdx=pd.DataFrame()
# # 'Bank Name'컬럼을 행 인덱스로 설정
# nameDF1=bankIdx.set_index('Bank Name')
# print(f'nameDF2===========>\n{nameDF1}')

# # #(3)
# # # 행기준 내림차순 (ascending=False)
# # desDF=nameDF1.sort_index(ascending=False)
# # print(desDF.index, desDF, sep='\n', end='\n\n')








