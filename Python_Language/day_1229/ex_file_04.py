#---------------------------------------------------------------
#파일 읽기 살펴보기
#---------------------------------------------------------------
FILE_NAME='happy.txt'


#---------------------------------------------------------------
#파일안에 모든 내용 가져오기
#---------------------------------------------------------------
fp=open(FILE_NAME, mode='r', encoding='utf-8')
allData=fp.read()
fp.close()

print(f'allData type => {type(allData)}\n{allData}')




#---------------------------------------------------------------
#readlines() 파일 내용을 줄(Line)단위로 가져옴
#---------------------------------------------------------------
fp=open(FILE_NAME, mode='r', encoding='utf-8')
allLines=fp.readlines()
fp.close()

print(f'allLines type => {type(allLines)}, {len(allLines)}\n{allLines}')



#---------------------------------------------------------------
#readline() 파일 내용을 1줄 가져오기
#---------------------------------------------------------------
fp=open(FILE_NAME, mode='r', encoding='utf-8')
Line=fp.readline()
fp.close()

print(f'Line type => {type(Line)}, {len(Line)}\n{Line}')




#---------------------------------------------------------------
#readline() 파일 내용을 1줄 가져오기
#---------------------------------------------------------------
fp=open(FILE_NAME, mode='r', encoding='utf-8')
while True:
    line=fp.readline()
    print({line})
    if not line: break
fp.close()

print(f'Line type => {type(Line)}, {len(Line)}\n{Line}')