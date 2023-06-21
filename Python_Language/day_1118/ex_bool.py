# ------------------------------------------------
# 논리 자료형 bool type (불)
# - 저장하는 데이터 : True, False
# - bool타입으로 형변환해주는 함수 : bool(데이터)
# ------------------------------------------------
# bool타입 데이터 저장
isRun = False
isOK = False

# 데이터를 bool타입 형태 변환 시키기-----------------
# 숫자 데이터 ===> bool타입으로 변환
# False => 0, True => 나머지 숫자들
isNumber=bool(5)
print(isNumber)

isNumber=bool(-3)
print(isNumber)

isNumber=bool(0)
print(isNumber)

isNumber=bool(0.1)
print(isNumber)

isNumber=bool(1.23)
print(isNumber)

isNumber=bool(0.0)
print(isNumber)


# 문자열 str => bool 형변환------------------------
# True => 공백문자라도 있으면 True
# False => 이무것도 없는것 '' ""
print('[str=> bool]---------------')
isMessage=bool(' ')
print(isMessage)

isMessage=bool('Good한긓')
print(isMessage)

isMessage=bool('')
print(isMessage)

# List/Tuple => bool 형변환------------------------
# True  => 요소가 1개라도 있는 경우
# False => 요소가 하나도 없는 경우
print('[List/Tuple=> bool]---------------')
nums=[]
datas=()
print(bool(nums), bool(datas))
print(bool([1]), bool((1)))

# dict/set => bool 형변환------------------------
# True  => 요소가 1개라도 있는 경우
# False => 요소가 하나도 없는 경우
print('[Dict/Set=> bool]---------------')
print(bool({}), bool(set()))
print(bool({'a':10}), bool({1}))