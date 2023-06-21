# ----------------------------------------
# List 전용의 함수들 => 메소드(Method)
# ----------------------------------------
# List 객체 생성 
nums=[1,2,3,4,5,6,7,8,9,10]

# List 전용 메서드 다루기 -----------------
# (1) 리스트 요소/원소를 역순으로 출력하기
# 리스트 데이터의 요소 순서를 반대로 해서 저장
# List.reverse()
print( f'전 nums => {nums}' )
nums.reverse()
print( f'후 nums => {nums}' )

# (2) 리스트 요소/원소의 인덱스를 반환하는 메서드
# List.index(요소값) => 없으면 Error/ 있으면 인덱스
nIdx=nums.index(1)
print(f'5의 인덱스 : {nIdx}')

#nIdex=nums.index(0)

# (3) 리스트의 요소/원소 삭제하는 메서드 - (1)
# 제일 첫번째 발견되는 요소값만 삭제
# List.remove(요소값)
nums.remove(7)
print(f'nums => {nums}')

# (3) 리스트의 요소/원소 꺼내는 메서드 - (2)
# 해당하는 요소가 리스트에서 없어짐
# List.pop()      : 제일 마지막 요소를 꺼내기
# List.pop(index) : 지정된 인덱스의 요소 꺼내기
pickNum=nums.pop()
print(f'pickNum : {pickNum} , nums => {nums}')

# 3번째 요소를 꺼내기
pickNum=nums.pop(3)
print(f'pickNum : {pickNum} , nums => {nums}')

# (3) 리스트의 요소/원소 삭제하는 명령어 - (3)
# del 삭제하고 싶은 요소
# del (삭제하고 싶은 요소)
del nums[-1]
print(f'nums => {nums}')

del(nums[0])
print(f'nums => {nums}')

# (4) 리스트의 모든 요소/원소 삭제하는 메서드 
# List.clear()
nums.clear()
print(f'nums => {nums}')

# (5) 리스트에 요소/원소 추가하는 메서드 -(1)
# List.append() : 제일 마지막에 추가
print(f'nums => {nums}, {len(nums)}개')
# nums[0] = 10 # <=인덱스란? 이미 존재하는 데이터에 부연된 번호

nums.append(3)
nums.append(1)
nums.append(8)
print(f'nums => {nums}, {len(nums)}개')

# (6) 리스트에 요소/원소를 지정된 위치에 추가하는 메서드 -(2)
# List.insert(위치인덱스, 요소값) 
nums.insert(1,11)
print(f'nums => {nums}, {len(nums)}개')

nums.insert(-1,11)
print(f'nums => {nums}, {len(nums)}개')

nums.insert(len(nums),11)
print(f'nums => {nums}, {len(nums)}개')

# (7) 리스트 요소/원소 정렬하는 메서드 
# List.sort()
# 기준 : 작은값 >>>> 큰값   오름차순(ascending) 정렬
#       큰  값 >>>> 작은값  내림차순(decending) 정렬
nums.sort()
print(f'nums => {nums}, {len(nums)}개')

# 내림차순 정렬
nums.sort(reverse=True)
print(f'nums => {nums}, {len(nums)}개')

# (8) 리스트 확장시켜주는 메서드
# List.extend(리스트)
nums.extend([77,66,55])
print(f'nums => {nums}, {len(nums)}개')

nums.extend([True, True, False, "Good"])
print(f'nums => {nums}, {len(nums)}개')