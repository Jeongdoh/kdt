# 멤버연산자 --------------------------------------------------
# a in A     => a가 A에 포함되면 True, 그렇지 않으면 False
# a not in A => a가 A에 포함되지 않으면 True, 그렇지 않으면 False
#-------------------------------------------------------------
# Hello 단어 있고 사용자가 입력한 알파벳이 Hello 단어에 
# 포함되는지 결과를 출력
print( 'a' in 'Hello')
print( 'lo' in 'Hello')
print( 'h' in 'Hello')

print('lo' in list("Hello"))
print('l' in list("Hello"))
print('o' in list("Hello"))

# [실습] 점수를 입력받고 학점 A ~ F 에서
# 해당 점수의 학점을 출력해주세요.
jumsu=int(input("당신의 점수를 입력해주세요 : ").strip())
grade=''

if jumsu>=90:  # 100 ~ 90
    grade='A'
elif jumsu>=80:  # 89 ~80
    grade='B'
elif jumsu>=70:  # 79 ~70
    grade='C'  
elif jumsu>=60:  # 69 ~60
    grade='D'       
else:
    grade='F'

print(f'{jumsu}는 {grade}학점')

# [실습] ------------------------------------------
member=['마징가','홍길동','베트맨','세종대왕','나']


name=input(" 이름을 입력하세요. ").strip()

if name in member:
    isMember=True
else:
    isMember=False

print(f'{name}은 우리 멤버 : {isMember}')


# [실습] -------------------------------------------
# nums=[16,3,7,9,12]
# 사용자로부터 숫자를 입력받고 존재하지 않는 숫자면
# 추가해 주시고, 존재하는 숫자라면 '이미 존재합니다.'라고 
# 출력해 주세요.
# --------------------------------------------------
nums=[16,3,7,9,12]
#nums.append(5)   # 제일 뒤에 추가해주는 메서드
#nums.insert(0,1) # 지정된 위치에 추가해주는 메서드

n = int(input("숫자 입력 : ").strip())

if n in nums:
    print(f'{n}은 이미 존재합니다.')
else:
    nums.append(n)
    print(f'현재 nums => {nums}')

if n not in nums:
    nums.append(n)
else:
    print(f'{n}은 이미 존재합니다.')  

# [실습] ------------------------------------------------
# nums=[16,3,7,9,12]
# 사용자로부터 숫자를 입력받고 존재하지 않는 숫자면 추가해 주세요. 
# 단 가장 작은값보다 크고, 가장 큰값보다 작은 경우만
# -------------------------------------------------------
# 멤버연산자 in/not in
# max(nums)> , min(nums)<



# 방법1) ---------------------------------------------------
n =int( input("숫자 입력 : "))

if n not in nums:
    if (max(nums)>n) and (min(nums)<n):
        nums.append(n)
else:
    print("존재합니다.")

# 방법2) -------------------------------------------------
max_num=max(nums)
min_num=min(nums)

n =int( input("숫자 입력 : "))

if (n not in nums) and (max_num>n) and (min_num<n):
    nums.append(n)
else:
    print("존재합니다.")







