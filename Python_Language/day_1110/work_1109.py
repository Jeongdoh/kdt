# 3. 정수 31을 2진수, 8진수, 10진수, 16진수로 출력하세요. 
# 내장함수=> bin(), oct(), hex()
number=31
print(f'{number} 2진수  => {bin(number)}')
print(f'{number} 8진수  => {oct(number)}')
print(f'{number} 16진수 => {hex(number)}')

# 4. 자료형(데이터 타입)을 변경하는 것을 
# (형변환 / 타입캐스팅 / 캐스팅 )이라 합니다.
#  아래 데이터를 지정하는 자료형으로 변환하세요. 
average=98.7
#  => 정수로 변환 _______int()_________ 
print(int(average))
average=int(average)

year=2022 
#  => 실수로 변환 __________float()______ 
print(float(year))
year=float(year)  
 
# 5. 2개 정수를 입력 받아서 산술연산, 
# 비교연산, 논리연산 수행 결과를 출력하는   
# 코드를 작성하세요.
num1=input("숫자 1개 입력 : ")
num2=input("숫자 1개 입력 : ")

# 입력 받은 데이터의 타입 확인 => type(변수명)
print(f'num1의 타입 : {type(num1)}')

# input()함수로 입력 받은 데이터는 전부 str 타입
# str => int 타입 형변환
num1=int(num1)
num2=int(num2)

# 산술연산 => +, -, * , / , // 몫, % 나머지, ** 제곱근
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'{num1}//{num2}={num1//num2}')
print(f'{num1}%{num2}={num1%num2}')
