# -------------------------------------------------
# 리스트 List 데이터 타입
# - 여러가지 종류의 데이터를 담는 자료형
# - 형태 : [데이터1, 데이터2,..., 데이터N]
# - 요소/원소 : 리스트 안에 들어있는 데이터
# -------------------------------------------------
# 리스트 객체 생성 ---------------------------------
emList=[]
numList=[5,23,0.9, 7, -1]
strList=['A', 'BCD', "한글", "123"]
dataList=[12, 'A', True, 235]
dataList2=[1,2,3,['a','b', []]]

# 리스트 안에 요소 수 출력 => 내장함수 len(변수명)
print(f'emList 갯수    : {len(emList)}개, {emList}')
print(f'numList 갯수   : {len(numList)}개, {numList}')
print(f'strList 갯수   : {len(strList)}개, {strList}')
print(f'dataList 갯수  : {len(dataList)}개, {dataList}')
print(f'dataList2 갯수 : {len(dataList2)}개, {dataList2}')

# 리스트 안에 요소 값 읽기 => 인덱스 사용
#   G o o d
#>> 0 1 2 3      0부터 시작하는 양수 인덱스
#  -4-3-2-1 <<  -1부터 시작하는 음수 인덱스
# ==> 리스트 동일한 방식으로 요소 사용 
# ==> 리스트객체변수명[인덱스]

# numList 요소 출력하기 -------------------
print(numList)
print(numList[0], numList[-5])
print(numList[1], numList[-4])
print(numList[2], numList[-3])
print(numList[3], numList[-2])
print(numList[4], numList[-1])

# dataList2 요소 출력하기 -----------------
# [1,2,3,['a','b', []]]
#  0 1 2 3
# -4-3-2-1
#          0   1   2
#         -3  -2  -1
print(dataList2)
print(dataList2[0], dataList2[-1])
print(type(dataList2[0]), type(dataList2[-1]))

print('a => ', dataList2[-1][0], type(dataList2[-1][0]))
print('b => ', dataList2[-1][1], type(dataList2[-1][1]))
print('[] => ', dataList2[-1][2], type(dataList2[-1][2]))

a=[1,2,['a','b',['life', 'is']]]
#  - - ------------------------
#  0 1 2
#       -   -  ----------------
#       0   1  2
#              -------  ----
#                0       1

print('is => ', a[2][2][1], a[-1][-1][-1])

# 요소 값 변경 ==> 변수명[인덱스]=새로운값------
# str타입은 지원하지 않음
#msg="Pithon"
#msg[1]='y'

nums=[1,20,3,4,5]
#     0  1 2 3 4
nums[1]=2
print('nums => ', nums)

# 슬라이싱 -------------------------------------------------------
# [시작인덱스:끝인덱스+1]  => 범위 시작인덱스이상<= ~ < 끝인덱스미만

# 1번요소 ~ 3번요소 출력
print(nums[1:4])
# 0번요소부터 짝수 인덱스 요소만 출력 => [시작인덱스:끝인덱스+1:간격]
print(nums[0::2])

# 1번요소 ~ 3번요소 값을 5로 변경
nums[1]=5
nums[2]=5
nums[3]=5
print(nums)

# 1번요소 ~ 3번요소 값을 'a'로 변경
nums[1:4]=['a','a','a']
print(nums)

nums[1:4]=['b','b','b','b','b']
print(nums)

nums[1:4]=[0]
print(nums)

nums[1:4]=[]
print(nums)

nums[:]=[]
print(nums)