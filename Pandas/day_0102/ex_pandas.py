import pandas as pd

#시리즈 (series) 데이터===================================
#pandas.Series(데이터)
#속성(Attribute): index, values, ndim, shape.....
#========================================================
#Series 객체 속성  출력 함수
#printSerises
def printSerises(srobj,srobjName):
    print(f'{srobjName} \n{srobj}')
    print('----------------------------')
    print(srobj.index)
    print(srobj.values)
    print(srobj.ndim)
    print(srobj.shape)
    print(srobj.dtype)



print('----------------------------')

#__name__:매직변수, 시스템에 값을 설정
#해당 파이썬 파일이 실행중 여부 확인
# 실행중 ==> __main__
# import될 경우 ==> 파일명

print(f'__name__ => {__name__}')
if __name__=='__main__':

    # (1)데이터 => 리스트 데이터

    sr=pd.Series([10,20,30])
    print(sr, 'sr')


    #시리즈 객체의 속성확인 => 변수명.속성명
    print(sr.index)
    print(sr.values)
    print(sr.ndim)
    print(sr.shape)

    # (2) 데이터 => 딕셔너리 형태 데이터
    sr2=pd.Series({'name':'Hong', 'age':12, 'loc':'daegu'})
    print(f'====> \n{sr2}')
    print('----------------------------')
    print(sr2.index)
    print(sr2.values)
    print(sr2.ndim)
    print(sr2.shape)

    # (3) 데이터 => 튜플 형태 데이터
    sr3=pd.Series((11,22))
    print(f'====> \n{sr3}')
    print('----------------------------')
    print(sr3.index)
    print(sr3.values)
    print(sr3.ndim)
    print(sr3.shape)


