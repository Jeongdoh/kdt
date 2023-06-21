#-------------------------------------------------------------------
#람다(lambda) 함수 : 익명함수, 1줄 함수
#                   짧은 코드의 함수--------------------------------------------------------
#문법형식 : lambda 인자 : 실행코드
# 입력받은 숫자를 모두 더해서 합계를 출력하느 코드
nums=input("원하는 수만큼 숫자를 입력하세요. (예: 1,2,5,2)")


#'1 3 5 7 9' ==> ['1','3','5','7','9']
nums=nums.split() # [1, 3, 5, 7, 9]

#str 요소 => int(요소)
nums[0]=int(nums[0])
for idx in range(0,len(nums)):
    nums[idx]=int(nums[idx])

print(f'1번 => {nums}')


# 리스트 컴프리핸션
nums=[int(n) for n in nums]
print(f'2번 => {nums}')

#원래값에 3을 곱한값 반환하는 함수
def threeNum(num): 
    return num*3



# 내장함수 => map(함수명, 반복가능 객체)-->map 객체
nums2=list(map(str, nums))
print(f'3번 => {nums2}')



nums4=list(map(threeNum, nums))
print(f'4번 => {nums4}')



nums5=list(map(lambda n:n*3, nums))
print(f'5번 => {nums5}')

