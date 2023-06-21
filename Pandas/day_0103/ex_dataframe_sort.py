# -------------------------------------------------------------------
# 정렬(sort)
# - 인덱스 기준 정렬 => 오름차순(작->큰), 내림차순
# - 데이터 기준 정렬 => 오름차순, 내림차순
# -------------------------------------------------------------------
# 모듈/패키지 로딩 ---------------------------------------------------
import pandas as pd 

# DF 생성 -----------------------------------------------------------
df1=pd.DataFrame({'name':['마징가','배트맨','원더우먼'],
                'kor':[87,91,69],
                'eng':[99,73,89],
                'sci':[71,95,62]})

print(df1)
#      name    kor  eng  sci      오름차순
# 0   마징가    87   99   71
# 1   배트맨    91   73   95
# 2  원더우먼   69   89   62

# [1] 인덱스 기준 정렬 -----------------------------------------------

# 행기준 내림차순 (ascending=False)
desDF=df1.sort_index(ascending=False)
print(desDF.index,desDF,sep='\n',end='\n\n')
#      name   kor  eng  sci       내림차순
# 2  원더우먼  69   89   62
# 1   배트맨   91   73   95
# 0   마징가   87   99   71

# 열기준 내림차순
colDesDF=df1.sort_index(axis=1,ascending=False)
print(colDesDF.index,colDesDF,sep='\n',end='\n\n')
#     sci   name   kor  eng
# 0   71   마징가   87   99
# 1   95   배트맨   91   73
# 2   62  원더우먼   69   89

# 열기준 오름차순
colDesDF=df1.sort_index(axis=1,ascending=True)
print(colDesDF.index,colDesDF,sep='\n',end='\n\n')
#    eng   kor   name   sci
# 0   99   87   마징가   71
# 1   73   91   배트맨   95
# 2   89   69  원더우먼  62

# [2] 데이터 값 기준 정렬 -----------------------------------------------
# DataFrame.sort_values()

# name 기준 내림차순
valDesDF=df1.sort_values(by=['name'],ascending=False)
print(valDesDF.index,valDesDF,sep='\n',end='\n\n')
#      name   kor  eng  sci
# 2  원더우먼  69   89   62
# 1   배트맨   91   73   95
# 0   마징가   87   99   71

df2=df1.sort_values(by=['eng','kor'],ascending=False)
print(df2.index,df2,sep='\n',end='\n\n')
#      name   kor  eng  sci
# 0   마징가   87   99   71     => eng 순  -> kor 순
# 2  원더우먼  69   89   62       if eng값 같으면 kor큰게 위
# 1   배트맨   91   73   95

# 특정 컬럼에 값 넣기 ---------------------------------------------------
df2['name']=['Bm','Mg',"Ww"]
print(df2.name,'\n',type(df2.name)) # = df2['name']

print(df2.name[1],type(df2.name[1])) # 이름 바꾸기전의 sort 때문에 1번 idx WW 추출됨

print(df2.name[1].swapcase())

# ==> 활용해서 value 값들이 소문자, 대문자 섞여있으면 하나로 통일해서 정렬













