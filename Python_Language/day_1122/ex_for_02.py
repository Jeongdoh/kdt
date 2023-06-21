# --------------------------------
# for 반복문 다루기
# --------------------------------
nums=[11,22,33,44,55, 66, 77, 88, 99]

#1부터 10000까지 1 ~ 1000 정수 범위 만들어 함수 range()
bigNums=range(10001)    # 0 ~ 10000
bigNums=range(1,10001)  # 1 ~ 10000

print(type(bigNums), bigNums, bigNums[0], bigNums[-1])
print(bigNums[:3])

# 짝수 인덱스 요소만 출력해주세요 ------------------------
# 리스트, 튜플, 딕셔너리, set집합, 문자열 => 갯수 파악 len()
# 요소 갯수 => 인덱스범위 0 ~ 요소갯수-1
# 인덱스 범위 : range(0, len(nums))  0<= ~ <len(nums)
for idx in range(0, len(nums)):
    if idx%2 == 0 :
    # if not idx%2:
        print(nums[idx])

for idx in range(0, len(nums),2):
    print(nums[idx])

# 2단 ~ 9단 구구단 출력 ------------------------
for dan in range(2, 10):
    print(f'---[{dan}]단---')

    for num in range(1,10):
        print(f'{dan}*{num}={dan*num:2}')

# 숫자문자열을 정수로 형변환하기 ----------------
nums=['1','3','8','10','2','5','9']
print(nums)

# nums[0]=int(nums[0])    # int('1')
# nums[1]=int(nums[1])    # int('3')
# nums[2]=int(nums[2])    # int('8')
# nums[3]=int(nums[3])    # int('10')
# nums[4]=int(nums[4])    # int('3')
# nums[5]=int(nums[5])    # int('5')
# nums[6]=int(nums[6])    # int('9')

for idx in range(len(nums)):
    nums[idx]=int(nums[idx])

print(nums)









