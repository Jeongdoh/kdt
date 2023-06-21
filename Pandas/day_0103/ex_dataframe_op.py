#-----------------------------------------------------------------------------------------------
# Series 데이터 연산 수행
# 브로드캐스트(Broadcast) : 연산 수행되는 SR/DF에 동일 크기로 확장해서 연산수행
#-----------------------------------------------------------------------------------------------
import pandas as pd

# SR객체 생성------------------------------------------------------------------------------------
sr1=pd.Series([11,12,13,14,15])

print(sr1)

# 연산 수행 - (1) Series 연산자 숫자==============================================================
sr2=sr1+10
print(f'sr1+10==> \n{sr2}', end='\n\n')

sr2=sr1-10
print(f'sr1-10==> \n{sr2}', end='\n\n')

sr2=sr1*10
print(f'sr1*10==> \n{sr2}', end='\n\n')

sr2=sr1/10
print(f'sr1/10==> \n{sr2}', end='\n\n')

sr2=sr1//10
print(f'sr1//10==> \n{sr2}', end='\n\n')

sr2=sr1%10
print(f'sr1%10==> \n{sr2}', end='\n\n')

# 비교연산 => True/False


sr2=sr1>13
print(f'sr1>13==> \n{sr2}', end='\n\n')


sr2=sr1!=13
print(f'sr1!=13==> \n{sr2}', end='\n\n')


# 연산수행 - (2) Series 연산자 Seires==============================================================
sr3=pd.Series([7,7,7])


sr4=sr1+sr3
print(f'sr1+sr3 => \n{sr4}', end='\n\n')

sr4=sr1-sr3
print(f'sr1-sr3 => \n{sr4}', end='\n\n')


# 결측치 비교 불가
# sr4=sr1>=sr3
# print(f'sr1>=sr3 => \n{sr4}', end='\n\n')



# 연산수행 - (3) Series.연산메서드(Series)==============================================================
# 빈데이터를 값을 채운 (fill_value 매개변수) 후 연산가능
sr3=pd.Series([7,7,7])


sr4=sr1.add(sr3, fill_value=0)
print(f'sr1.add(sr3) => \n{sr4}', end='\n\n')

sr4=sr1.divmod(sr3,fill_value=0)
print(f'sr1.divmod(sr3) => \n{sr4}', end='\n\n')








