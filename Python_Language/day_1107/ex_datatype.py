# --------------------------------
# -데이터 타입 / 자료형
# -컴퓨터에 저장하는 데이터 종류
# -종류
# *숫자형 = > 정수 int타입
# *숫자형 = > 실수float타입
# *숫자형 = > 복소수 complex
# *문자형 = > 문자열 str
# *논리형 = > 논리 bool
# *바이트형 = > byte 타입
# -데이터의 종류에 따라서 사용되는 메모리 칸수 다름
# -저장되는 숫자 범위가 다름
#-----------------------------------

# 데이터의 자료형 알려주는 내장함수
# => type(데이터), type(변수명)
print( type(4), type('A'), type(4.98))
print( type(False), type(1+2j))

number='4'
name=2022
isHappy=True

print(type(number), type(name), type(isHappy))

