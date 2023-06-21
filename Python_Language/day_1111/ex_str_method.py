#------------------------------------------------
#메서드(method)
#특정 클래스에서만 사용되는 함수를 말함
#사용 : 객체 생성 후 사용가능 가능
# 예시 ) name= 'hong'
#        name.메서드명()
#        name.thrtjdaud
#-----------------------------------------------
msg="Merri Christmas!"

# 'i'로 적은걸 y로 변경
# 방법1 . 인덱스로 변경 = > 변경 불가
#msg[4]='y'
#print(msg)

# 방법2) str타입의 전용 메서드 => replace(바꿀 문자열, 새로운 문자열)
# 변경된 문자열은 다시 저장해야 함!!
msg=msg.replace('i', 'y')
print(msg)

# 문자열에서 인덱스 찾아주는 메서드
# find(문자열) => 양수 인덱스 / 없는경우 : -1
# index(문자열) => 양수인덱스 / 없는경루 : error
print(f'{msg} = C 인덱스 : {msg.find("C")}')
print(f'{msg} = c 인덱스 : {msg.find("c")}')

#여러개 문자가 모인 경우에는 문자가 시작되는 인덱스 반환
print(f'{msg} = mas 인덱스 : {msg.find("mas")}')

#특정문자가 여러개 존재하는 경우 => 제일 먼저 발견되는 문자 인덱스를 줌.
print(f'{msg} = r 인덱스 : {msg.find("r")}')

#문자열의 뒤에서 부터 인덱스를 찾는 경우는 rfind()메서드
print(f'{msg} = r 인덱스 : {msg.rfind("r")}')

# index() 메서드로 문자의 인덱스 찾기
print(f'{msg} = C 인덱스 : {msg.index("C")}')
#print(f'{msg} = c 인덱스 : {msg.index("c")}')

# 문자열에서 특정 문자열이 몇개있는지 알려주는 메서드 => count()
data = "Happy happy"
pCount=data.count('p')

#data 문자열에서 'p'가 존재하는 갯수만큼 data를 화면에 출력해주세요.
print(data*pCount)
print(pCount)

# 대소문자 변경해주는 메서드
# 소문자 => 대문자로 변경 upper
# 대문자 => 소문자로 변경 lower
print(data.upper(), data.lower())
print(data)

# 앞부분 / 뒷부분 공백 제거하는 메서드
# strip() : 앞/ 뒤 공백제거
# lstrip() : 앞부분 공백제거
# rstrip() : 뒷부분 공백만 제거
data1=" Happy Happy "

# 내장함수 => len(변수명) => 갯수 /길이를 리턴
print(f'{data1} 길이 : { len(data1)}')

data2=data1.strip()
print(f'{data2} 길이 : { len(data2)}')

data3=data1.lstrip()
print(f'{data3} 길이 : { len(data3)}')

data4=data1.rstrip()
print(f'{data4} 길이 : { len(data4)}')


# 문자열 쪼개기, 특정 문자를 기준으로 쪼개기 => split()
# - 기본 : 공백을 기준으로 문자열 나누기
data="happy new year 2023"

# data="happy new year 2023" 기본 공백으로 나누기
datas=data.split()
print(datas)


data=data.replace(' ', '*')
print(data)

# '*'로 문자열 나누기
data="happy new year*2023"
datas=data.split('*')
print(datas)

# 휴대폰번호 나누기
#010-3512-1287
#2022/12/24
#123233-232323
data='010-3512-1287'
datas=data.split('-')
print(datas)

year='2022/12/24'
year1=year.split('/')
print(year1)


adress='123233-232323'
adress1=adress.split('-')
print(adress1)



# 여러개의 문자열 연결 또는 삽입 메서드 = > join()
# 형식 : 연결할 문자열.join(여러개의 문자열)
phone='010-1234-5678'

phone2=phone.split('-')
print(f'phone2: {phone2}')

# 나누어진 전화번호 문자열 합치기/ 연결
new_phone='.'.join(phone2)
print(f'new_phone : {new_phone}')

new_phone=' '.join(phone2)
print(f'new_phone : {new_phone}')

new_phone='^^'.join(phone2)
print(f'new_phone : {new_phone}')

# [실습] --------------------------------------
# 하고싶은 말 입력받아서 출력하기
#---------------------------------------------
talk=input("하고싶은 말 입력 : ")

print(type(talk))
print(f'talk 길이 : {len(talk)}')


# 입력받은 데이터 공백제거하기
talk=talk.strip()
