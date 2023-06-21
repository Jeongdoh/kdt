#-----------------------------------------------------------------
# 제어문 : 실행 코드 제어
# -조건문 : 경우에 따른 코드 실행여부 결정코드
#-----------------------------------------------------------------
# 숫자가 양수인지 음수인지 검사 후 출력해주세요.
# 양수 > 0, 음수 <0 


# num=int(input("숫자 입력: "))

# if num>0:
#     print(f'{num}은 양수입니다.')
# else:
#     print(f'{num}은 0또는 음수입니다.')

# print('---END---')


# 딕셔너리 안에 키 검사
jumsu={'kor':90, 'eng':89}

# 딕셔너리의 키만 추출 => dict.keys()
keys=jumsu.keys()

print('math' in keys)
print('kor' in keys)

subject='kor'


if 'subject' in keys:
    print(f'{subject} => {jumsu["subject"]}')

else:
    print(f'{subject} 키는 존재하지 않습니다.')


if 'math' in keys:
    print(f'math => {jumsu["math"]}')

else:
    print(f'math 키는 존재하지 않습니다.')


# [실습]-----------------------------------------------------------------
# 데이터를 입력받고 입력받은 데이터가 있다면 ok 출력
# 없다면 '데이터 없음' 출력

# 내가한거-------------------------------------------
data=input("데이터를 입력하세요")

if len(data) :
    print(f'데이터 => ok')

else :
    print('데이터 없음')

# 풀이-----------------------------------------------
data=input("데이터를 입력하세요").strip()

print(f'data => {data}, 길이 : {len(data)}')

if len(data)>0:
    print(f'data => {data}, ok')

else:
    print("다시확인하세요. \n공백이거나 입력된 데이터가 없습니다.")




# [실습]-----------------------------------------------------------------
# 정수 데이터 입력받은 후 정수만큼 '*' 를 출력해주세요

number=input("정수를 입력해주세요.").strip()

# 내가한거-------------------------------------------
if (number):
    print(f'number => {number}')


# 풀이-----------------------------------
number=input("정수입력 :").strip()



if (len(number)>0) and  (number.isdecimal()):
    print('*'*int(number))
else:
    print("정.수.를.입.력.하.세.요!!")




if (len(number)>0):
    if(number.isdecimal()):
        print('*'*int(number))
    else:
        print("정.수.를.입.력.하.세.요!!")
    
else:
    print("다시확인하세요. \n공백이거나 입력된 데이터가 없습니다.")