# ----------------------------------------
# 문자열 str타입 연산수행
#-----------------------------------------

name="Hong"
gender='M'

# 산술연산 수행-----------------------------
# 덧셈(+) : str + str = 문자열 연결
print(f'{name}+{gender} = {name+gender}')


# str + int 안됨!! 오직 str + str 만 됨
# str타입으로 형변환 해서 덧셈 가능 => 바꾸고 싶은 데이터에다가 str(데이터)
print(f'{name}+{str(2022)} = {name+str(2022)}')


# 산술연산 수행-----------------------------
# 뺄셈(-) : str - str = 지원되지 않는 기능
#print(f'{name}-{gender} = {name-gender}')

# 산술연산 수행-----------------------------
# 곱셈(*) : str * int = str을 지정된 정수만큼 반복
print(f'{name}*{5} = {name*5}')

# 산술연산 수행-----------------------------
# 나머지(%) : 문자열 안에 변수값 설정에 사용
# %알파벳1개 => %d는 변수값이 정수, %f는 실수, %s 는 문자열
print('%s, %d, %s'%(name, 12, gender))
print('%s, %s, %s'%(name, 12, gender))


# [실습]------------------------------------------------------
# 출력 => =======================================
#                       my program
#         =======================================

print("\t==========================\n\t\tMy Program\t\t\n\t==========================")
print("="*30)
print("\tMy Program")
print("="*30)

print(("="*30 )+ "\n\tMy Program\n" + ("="*30))

# 멤버 연산자 -----------------------------------------
# 요소 in 그룹 : 요소가 그룹에 존재 하는지 true / false
# 요소 not in 그ㅡ룹 ; 요소가 그룹에 존재하지 않으면 true
# -----------------------------------------------------

data="Good"

print(f'G in {data} : {"G" in data}')
print(f'g in {data} : {"g" in data}')
print(f'OD in {data} : {"OD" in data}')
print(f'od in {data} : {"od" in data}')

print(f'OD not in {data} : {"OD" not in data}')
print(f'od not in {data} : {"od" not in data}')


print((20).real)