#-------------------------------------------------------------
#List, Tuple => 저장 순서대로 파이썬에서 번호 부여
#               인덱스
#-------------------------------------------------------------
data='1 ,2 ,3 ,4 5'

# str-----------------> list() 형변환 => 추가작업 필요
print(list(data))


# str 클래스 => 문자열을 나누어주는 기능 메서드 split(','): 기본 공백 기준
# 리스트로 변환
data=data.split(',')
print(data)

#len(data) : 요소의 수
print(len([1,4,3]), len([]), len(data))


#-------------------------------------------------------------
#dict => {키 : 값, 키: 값, 키: 값}
#           키로 값을 사용, 키 중복x => 값 변경
#-------------------------------------------------------------
#         키     값     키  값   키 값
person={'name':'hong', 12:'num', 7:2023}


# 키만 가져오기 => 메서드 keys()
keys=person.keys()
print('keys => ', keys)

for k in keys: print(k)

# 값만 가져오기 => 메서드 values()
v=person.values()
print('v =', v)
for vv in v: print(vv)

#키와 값의 묶음으로 => 메서드 items()  (키, 값)  키, 값
datas = person.items()
print('datas => ', datas)

#  0   1
# (키, 값)
for data in datas: print(data)


# 언패킹 => 묶음을 풀어서 가져오는 방법, 요소 갯수만큼 변수 필요
for a, b in datas: print(a,b)


# 추가하기 => 키로 값넣기
person['birth']='1224'
print(person)


# 존재하는 키
person[12]='Good'
print(person)


# 합계 계산하는 내장함수 => sum([]..)
print(sum([3,4,5,6]))

sum='Good'

print(sum([1,2,3,4]))
