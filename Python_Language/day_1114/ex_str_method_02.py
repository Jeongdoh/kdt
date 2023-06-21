# -----------------------------------------------
# 함수(function) & 메서드(method)
# - 공통점 : 형태 동일
# - 차이점 : 이름이 다름, 사용범위
#          - 누구나 사용 가능 => 함수
#          - 특정 데이터 타입만 사용 가능 => 메서드
#            특정 데이터 타입 객체변수명.메서드()
# ----------------------------------------------

# str 데이터 타입 전용 함수 즉 메서드 ------------
msg='good lucck!'

# => 대문자 변환 메서드 upper()
print(msg.upper(), msg)

# => 이전 문자 ->새로운문자 변경 메서드 replace()
print(msg.replace('cc','c'), msg)

# => 문자열을 특정 기준으로 문자열 나누기 메서드 split()
print(msg.split(), msg)

# 재밌는 str 메서드 ----------------------------
# 문자열 첫부분 체크 후 결과 True/False => startswith()
print(msg.startswith('go'))
print(msg.startswith('!@'))

# 문자열 끝부분 체크 후 결과 True/False => endswith()
print(msg.endswith('!'))
print(msg.endswith('!@'))

# 입력받은 데이터가 숫자, 문자인지 검사 후 결과 True/False 
# => isXXX()
print(msg, msg.isnumeric())
print("hello", "hello".isalpha())