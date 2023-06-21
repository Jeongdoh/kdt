#------------------------------------------------------------------------------------------
# 연산실습
#------------------------------------------------------------------------------------------
# 모듈 로딩--------------------------------------------------------------------------------
import pandas as pd

FILE = 'dataFiles\\dataFiles\\stock price.xlsx'


# [1] 가격에 대한 주식ID, 이름, 가격만 사용하도록 데이터 추출
# df객체 생성
stockPrice=pd.read_excel(FILE)

# 데이터 확인 => info(), head(), tail(), describe()
stockPrice.info()
print('-'*50)
print(stockPrice.head())
print('-'*50)
print(stockPrice.tail())
print('-'*50)
print(stockPrice.describe())
print('-'*50)


newSP=stockPrice[['id','stock_name' ,'price']]
print('-'*50)
print(newSP.head())
print('-'*50)
print(newSP.tail())
print('-'*50)
print(newSP.describe())
print('-'*50)




# [2] 가격에 대한 *100 결과를 추가

print(newSP.price * 100)

# 방법1
newSP['price100']=newSP.price*100
# 방법2
newSP['price100']=newSP.price.mul(100,fill_value=0)

# 내가한거
newSP2=newSP[['price']]*100
print(f'newSP2*10==> \n{newSP2}', end='\n\n')



#=============================================================================================================
# id 컬럼을 인덱스 설정하세요. => DataFrame.set_index(컬럼)
# 데이터 파일 읽어들일때 설정 => 매개변수(파라미터) index_col
print('='*50)
print(stockPrice.index, newSP.index, sep='\n' )


#특정컬럼 인덱스로 지정 => index_col매개변수
#로딩할 특정컬럼 지정 => usecols=''
#skipfooter:3 밑에3줄 빼고 다 가져오는것    skiprows:3 위에 3줄빼고 다 가져오는 것  \
# header:스킵로우 부르면 위에 3줄 사라지고나면 4번째 열이 헤드가 되는데 이를 방지하기위해  None 숫자 열이 들어가줌


#stockDF=pd.read_excel(FILE, usecols='B,D')
stockDF=pd.read_excel(FILE, skiprows=3, header=None)
stockDF.info()
print(stockDF.index, stockDF.columns, sep='\n', end='\n\n')
print(stockDF)

# parse_dates 매개변수 => 컬럼 지정하면 해당 컬럼의 타입이 datetime64로 변경
# dayfirst 매개변수 : 일/월 순서로 설정하겠다는 뜻
# inter_datetime_format 매개변수 : 날짜시간 포맷을 추정해서 파싱
# date_parser 매개변수 : 직접 날짜 시간 포맷설정 function
from datetime import datetime   # 날짜시간관련 모듈
print('='*50)
FILE2='dataFiles\\dataFiles\\banklist.csv'

# bankDF=pd.read_csv(FILE2, parse_dates=['Updated Date'], dayfirst=True, infer_datetime_format=True)
_date_parser=lambda x: datetime.strptime(x,"%d/%b/%y %H:%M:%S")        # 위처럼 해도되고 이렇게 해도 됨
bankDF=pd.read_csv(FILE2, parse_dates=['Updated Date'], date_parser=_date_parser)   # 위처럼 해도되고 이렇게 해도 됨
bankDF.info()
print(bankDF.head())













