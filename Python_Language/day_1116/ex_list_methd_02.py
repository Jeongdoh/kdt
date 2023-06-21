# --------------------------------------
# List 자료형의 메소드(Method)
# --------------------------------------

# pop()/pop(인덱스) :  데이터 꺼내는 메서드
#                     리스트에서 데이터 제거
nums=[1,3,5,"ABC",False,3]

# 데이터 3, "ABC"를 삭제해 주세요
# =>  remove(), pop()

# -----------------------------------------------------
# 방법1) list.remove(데이터)메서드
#        해당 데이터가 리스트에 있다면 삭제
#        해당 데이터가 여러개 있는 경우 제일 첫번째것 삭제
print(f'nums => {nums}, 요소수: {len(nums)}개')
print(f'nums[2] => {nums[2]}')
#nums=[1,3,5,"ABC",False,3]
#      0 1 2 3     4     5
nums.remove(3)
print(f'nums => {nums}, 요소수: {len(nums)}개')
print(f'nums[2] => {nums[2]}')
#nums=[1,5,"ABC",False,3]
#      0 1 2     3     4

nums.remove(3)
print(f'nums => {nums}, 요소수: {len(nums)}개')
print(f'nums[2] => {nums[2]}')

# -------------------------------------------------------------
# 방법2) list.pop() : 제일 마지막 요소 꺼내기/삭제
#        list.pop(인덱스) : 지정된 인데스의 데이터 꺼내기/삭제
nums=[1,3,5,"ABC",False,3]

print(f'nums => {nums}, 요소수: {len(nums)}개')
nums.pop()

print(f'nums => {nums}, 요소수: {len(nums)}개')
nums.pop(1)

print(f'nums => {nums}, 요소수: {len(nums)}개')

# -------------------------------------------------------------
# 방법3) del 요소 : 해당 요소 삭제 명령어
nums=[1,3,5,"ABC",False,3,4,2]
#     0 1 2 3     4     5 6 7
del nums[5]

#nums=[1,3, 5,"ABC",False, 4,2]
#      0 1  2  3    4      5 6
del nums[1]


