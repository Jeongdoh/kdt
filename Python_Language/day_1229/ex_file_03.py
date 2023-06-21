#--------------------------------------------------------
#파일 입출력 (i/o)
#--------------------------------------------------------
# 쓰기모드 (mode)
# mode='w' : 파일이 존재하면 내용을 지우기, 그리고 쓰기
#            파일이 없으면 파일 생성하고 쓰기

# mode='a' : 파일이 존재하면 끝 부분에 내용 쓰기
#            파일이 없으면 파일 생성하고 쓰기
#--------------------------------------------------------

#모드 'w'로 파일쓰기
# mode='w' : 파일이 존재하면 내용을 지우기, 그리고 쓰기
#            파일이 없으면 파일 생성하고 쓰기
FILE_NAME='mydata.txt'

fp=open(FILE_NAME, mode='w', encoding='utf-8')
fp.write("asdasd")
fp.close()



#모드 'x'로 파일쓰기
#존재하는 파일 =>오류발생
#존재하지 않는 파일=> 파일 생성 후 쓰기
FILE_NAME='happy.txt'

fp=open(FILE_NAME, mode='x', encoding='utf-8')
fp.write("happyhappy")
fp.close()




#모드 'a'로 파일쓰기
#존재하는 파일 =>끝부분에 추가
#존재하지 않는 파일=> 파일 생성 후 쓰기
FILE_NAME='happy.txt'

fp=open(FILE_NAME, mode='a', encoding='utf-8')
fp.write("qweijoiwjer")
fp.close()