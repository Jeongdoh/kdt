# -----------------------------------------
# 제어문 : 실행 코드 제어
# - 조건문 : 경우땨른 코드 실형 여부 결정 코드
# -----------------------------------------
# 숫자가 양수인지 음수인지 검사 후 출력해 주세요.
# 양수 >0,  음수 <0  
num=10

if num>0:
    print(f'{num}은 양수입니다.')
else:
    print(f'{num}은 0또는 음수입니다.')

print('---END---')

# 딕셔너리 안에 키 검사
jumsu={'kor':90, 'eng':89}

# 딕셔너리의 키만 추출 => dict.keys()
keys=jumsu.keys()

subject='kor'

print( subject in keys)

if subject in keys:
    print(f'{subject}  => {jumsu[subject]}')
else:
    print(f'{subject} 키는 존재하지 않습니다.')

# [ 실습 ] ------------------------------------------
# 데이터를 입력 받고 입력 받은 데이터가 있다면 OK 출력
# 없다면 '데이터 없음' 출력
data=input("메시지 입력 : ").strip()

if len(data)>0:
    print(f"data => {data}, OK")
else:
    print("다시 확인하세요.",
          "공백이거나 입력된 데이터가 없습니다.")

# [ 실습 ] ------------------------------------------
# 정수 데이터 입력 받은 후 정수만큼 '*'를 출력해주세요
number=input("정수입력 : ").strip()

if (len(number)>0) and (number.isdecimal()) :
    print('*'*int(number))
else:
    print("정.수.를.입.력.하.세.요!!")


if (len(number)>0):
    if (number.isdecimal()) :
        print('*'*int(number))
    else:
        print("정.수.를.입.력.하.세.요!!")
else:
    print("공백이거나 입력된 데이터가 없음!!")
    
