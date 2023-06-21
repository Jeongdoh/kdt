# -------------------------------------------------
# List 자료형으로 코드 작성하기
# -------------------------------------------------
# [실습1] 입력받은 데이터를 저장 후 최대값, 최소값 찾아서
#         출력하기
#         (조건) 숫자 5개 입력 받음, input() 1번만 사용
# - 생각 1 : input() 내장함수 사용
# - 생각 2 : 타입 전부 str 타입 ==> int 타입 형변환
# - 생각 3 : 하나의 str로 숫자 문자열 ==> 문자열 나누기 split()
# - 생각 4 : 내장함수 => len() : 요소 수 , max():최대값, min():최소값

# (1) 입력 받기
nums=input("숫자 5개 입력 : (예:5, 7, 3, 1, 0) ")

# (2) 데이터 나누기 및 확인
nums=nums.split(',')
print(f'nums=> {nums}')

# (3) 데이터 공백 제거 및 타입 변환
print(f'nums[0]=> {type(nums[0])}')
# nums[0]=nums[0].strip()
# nums[0]=int(nums[0])
nums[0]=int(nums[0].strip())
nums[1]=int(nums[1].strip())
nums[2]=int(nums[2].strip())
nums[3]=int(nums[3].strip())
nums[4]=int(nums[4].strip())

print(f'nums=> {nums}')

# (4) 리스트 요소 중 가장 큰 숫자, 가장 작은 숫자 출력
# 내장 함수 => max(), min()
firstValue=max(nums)
lastValue=min(nums)

print(f'리스트 nums의 최대값 : {firstValue}, 최소값 : {lastValue}')
