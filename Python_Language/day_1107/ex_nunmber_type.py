# # ------------------------------
# # 숫자 데이터 타입
# # ------------------------------
# 다양한 숫자 표기법
bNum=0b11101 #2진수
oNum=0o35 #8진수
dNum=29 #10진수
xNum=0x1d #16진수

print(f'{bNum} : {bNum}, {bNum:#b}')
print(f'{oNum} : {oNum} , {oNum:#o}')
print(f'{dNum} : {dNum} , {dNum:#o}')
print(f'{xNum} : {xNum} , {xNum:#o}')

# 숫자에 대한 2진수 , 8진수 , 16진수 값을 알려주는 내장함수
print( 31, hex(31), oct(31), bin(31))

# -------------------------------------
# # 산술연산자 => +, - , *, /, //, %, **
# -------------------------------------
num1=11
num2=3

print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1+num2}')
print(f'{num1}*{num2}={num1+num2}')
print(f'{num1}/{num2}={num1+num2}')


print(f'{num1}//{num2}={num1+num2}') #몫
print(f'{num1}%{num2}={num1+num2}') #나머지
print(f'{num1}**{num2}={num1+num2}') #제곱

#비교연산자=> > , < , <=, >=, 
print(f'{num1} > {num2} = {num1>num2}')
print(f'{num1} < {num2} = {num1>num2}')
print(f'{num1} >= {num2} = {num1>num2}')
print(f'{num1} <= {num2} = {num1>num2}')
print(f'{num1} == {num2} = {num1>num2}')
print(f'{num1} != {num2} = {num1>num2}')


#논리연산자
# => Left, and Right : 왼쪽/ 오른쪽 모두 true
# => Left or Right : 왼쪽/ 오른쪽 중 한개이상만 true면 true
# => not data : true > false, false > true

print(f'{num1}>{num2} and {num1}=={num2} : {(num1>num2)and(num1==num2)}')
print(f'{num1}<{num2} and {num1}=={num2} : {(num1<num2)and(num1==num2)}')
print(f'{num1}>{num2} and {num1}>={num2} : {(num1>num2)and(num1>=num2)}')

# ---------------------------------------------------------------------------

print(f'{num1}>{num2} or {num1}=={num2} : {(num1>num2)or(num1==num2)}')
print(f'{num1}<{num2} or {num1}=={num2} : {(num1<num2)or(num1==num2)}')
print(f'{num1}>{num2} or {num1}>={num2} : {(num1>num2)or(num1>=num2)}')

#-------------------------------------------------------------------------------
print(f'not {num1}>{num2} : {not num1>num2}')
print(f'not {num1}=={num2} : {not num1==num2}')

# 객체비교 연산자
#A is B => A와 B가 같은 객체이면 True
#A is Not B => A와 B가 다른 객체이면 True

num1=10
num2=num1

print(f'id(num1) : {id(num1)}, id(num2) : {id(num2)}')
print(f'idnum1 : {num1}, num2 : {num2}')
print(f'{num1} is {num2} : {num1 is num2}')
print(f'{num1} == {num2} : {num1 == num2}')

#------------------------------------------------------
num2=10.0
print(f'id(num1) : {id(num1)}, id(num2) : {id(num2)}')
print(f'idnum1 : {num1}, num2 : {num2}')
print(f'{num1} is {num2} : {num1 is num2}')
print(f'{num1} == {num2} : {num1 == num2}')

#------------------------------------------------------
# 형변환 TYPE CASTING
# - 자료형 즉 DATA TYPE을 변경시켜주는것
# - 데이터 손실이 발생도 가능
# - 내장함수 => 자료형이름() int(), float(), str()
#------------------------------------------------------
avg=89.23

print(f'{avg} => {type(avg)}')

#해당 순간만 타입이 변경된것
print(f'int{avg} => {type(int(avg))}')

#int타입으로 변환된 데이터를 다시 저장
# 영구적으로 변경
avg=int(avg)

print(f'{avg} => {type(avg)}')