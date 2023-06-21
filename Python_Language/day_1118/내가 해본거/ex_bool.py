# 논리 - 참, 거짓 -bool -1 true
#                     - 0 false
#                                                    클래스

# 숫자 - 정수 int
#        실수float
#        복소수 complex
# 문자(글자) - str
# 컨테이너 타입 - list[]
#                tuple() 수정x
#                dict{}  keyvalue
#                set{} inx ,x  중복제거


#-----------------------------------------------------------------------------
#논리 자료형 bool type(불)
# - 저장하는 데이터 : true, false
# - bool타입으로 형변환 해주는 함수 : bool(데이터)
#-----------------------------------------------------------------------------
# bool타입 데이터 저장하기
isrun = False
isok = False

# 데이터를 bool타입 형태 변환시키기----------------------------------------------
# 숫제 데이터 ==> bool타입으로 변환시킬때
# False => 0 , True => 나머지 숫자들
isnumber=bool(5)
print(isnumber)

isnumber=bool(-3)
print(isnumber)

isnumber=bool(0)
print(isnumber)

isnumber=bool(0.1)
print(isnumber)

isnumber=bool(1.23)
print(isnumber)

isnumber=bool(0.0)
print(isnumber)



# 문자열 str 타입 => bool로 형변환
#true => 공백문자라도 있으면 true
#false=> 아무것도 없는것 '' ""
print('[str=> bool]-------------------------------')
ismessage=bool(' ')
print(ismessage)

ismessage=bool('good한글')
print(ismessage)

ismessage=bool('')
print(ismessage)


# list/tuple 타입 => bool로 형변환
#true => 요소가 1개라도 있는경우
#false=> 요소가 하나라도 없는경우
print('[list/tuple=> bool]-------------------------------')
nums=[]
datas=()
print(bool(nums), bool(datas))
print(bool([1]), bool(1))


# dict/set 타입 => bool로 형변환
#true => 요소가 1개라도 있는경우
#false=> 요소가 하나라도 없는경우
print('[dict/set=> bool]-------------------------------')


print(bool({}), bool())
print(bool({'a':10}), bool({1}))