# -----------------------------------------------
# 문자 데이터 => str 타입 자료형
# -표현방법
#   : '문자', "문자", '''문자''', """문자"""
# -----------------------------------------------
# 이름 데이터 저장하기
name='마징가'
name="마징가"
name="Maginga"

# name 변수를 통해서 데이터 출력
print(f'name => {name}')

# ------------------------------------
# str에서 문자 1개만 출력하기
# 인덱싱(Indexing)
# ------------------------------------
# "M  a g i n g a"
#  0  1 2 3 4 5 6
#  -7-6-5-4-3-2-1
# 변수명[인덱스]
print(name[0],  name[-7])
print(name[-1], name[6])

# [실습] 'Good Luck~!'문자열에서 Luck만 출력하기
msg='Good Luck~!'
#    012345678910
print(msg)
print(msg[0], msg[1], msg[2])
print(msg[3], msg[4], msg[5])
print(msg[6], msg[7], msg[8])
print(msg[5], msg[6], msg[7], msg[8])

# ---------------------------------------------------------
# 슬라이싱 
# => 문자열에서 구간(범위) 정해서 일부 문자열 잘라내기
# => 변수명[시작인덱스:끝인덱스+1]
# => 변수명[시작인덱스: ]  끝까지 
# => 변수명[  :끝인덱스+1] 처음부터 즉 0번부터 
# => 변수명[  :  ] 처음부터 끝까지
# ---------------------------------------------------------
# Luck 슬라이싱으로 출력
#msg='Good  Luck ~!'
#     01234 5678 910
#   ------- ---- --
#   1110987 6543 21
print(msg[5:9], msg[-6:-2], msg[5:-2])

# [실습]-----------------------------------------
msg="Merry Christmas~ 2022 12 24^^"
#    0         1         2
#    01234567890123456789012345678
# (1)"2022 12 24"만 출력하기
print(msg[17:27])

# (2)"Christmas~"출력하기
print(msg[6:16])

# (3)"2022 12 24^^"출력하기
print(msg[17:28])  # 17<= <29
print(msg[17:])    # 17번부터 끝까지

# (4) "Merry" 출력하기
print(msg[0:5], msg[:5])

# [실습]-----------------------------------------
strNumber="CODE_123456789"
#          01234567890123
# (1)"13579"만 출력
print(strNumber[5], strNumber[7],
      strNumber[9], strNumber[11], strNumber[13] )

# 연속되지 않지만 규칙이 있음 => 슬라이싱
# 변수명[시작인덱스:끝인덱스+1:규칙/간격]
print(strNumber[5:14:2], strNumber[5::2])

# [실습] ------------------------------------------
# 생년월일 계절을 한번에 입력 받아서 년, 월, 일, 계절을
# 4개의 변수에 저장하기
# -------------------------------------------------
# (1) 입력받기 => input()
mybirth=input("당신의 생년월일과 계절을 입력하세요.")
#[예:2022 12 14 spring] ")

# 입력받은 데이터의 타입 확인해보기
#print(f'mybirth 타입 : {type(mybirth)}')
print(type(mybirth))

# (2) 년, 월, 일, 계절을 문자열에서 추출해서 변수에 저장
# 2022 12 14 spring
# 01234567890123456
year=mybirth[:4]
month=mybirth[5:7]
day=mybirth[8:10]
sea=mybirth[11:]

print(year+"년 "+month+"월 "+day+"일 "+ sea+"에 태어남")

print("%s년 %s월 %s일 %s에 태어남" %(year, month, day, sea))

print(f"{year}년 {month}월 {day}일 {sea}에 태어남")

print("{year}년 {month}월 {day}일 {sea}에 태어남")
