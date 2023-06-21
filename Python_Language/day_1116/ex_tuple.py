# ---------------------------------------------
# 튜플(Tuple) 자료형 
# - 여러가지 종류의 여러 개의 데이터를 저장하는 타입
# - 저장 후 수정/삭제/추가 안됨!!
# - 저장된 데이터/요소 읽기만 가능 ==> Read Only List
# - 형태
#   * (데이터1, 데이터2,...., 데이터N)
#   * 데이터1, 데이터2,...., 데이터N
#   * (데이터,)
#   * 데이터,
# -----------------------------------------------
# 튜플 객체 생성하기 ------------------------------
empty=()
nums1=(1,2,3)
nums2=1,2,3
nums3=(1,)
nums4=1,
nums5=(1)
nums6=1

print(f'empty 타입 : {type(empty)}')
print(f'nums1 타입 : {type(nums1)}')
print(f'nums2 타입 : {type(nums2)}')
print(f'nums3 타입 : {type(nums3)}')
print(f'nums4 타입 : {type(nums4)}')
print(f'nums5 타입 : {type(nums5)}')
print(f'nums6 타입 : {type(nums6)}')

# 튜플 요소/데이터/원소 읽기 --------
# 인덱싱 & 슬라이싱
nums=range(1,21)
nums=tuple(nums)

# 튜플과 내장함수
print(len(nums), type(nums))
print(sum(nums), max(nums), min(nums))

# 인덱싱 & 슬라이싱
print(nums[0], nums[-1])
print(nums[:3], nums[::2])

# 요소 값 변경 => 안됨!
#nums[0]='A'

# 요소 삭제 => 안됨!
#del nums[0]

# 요소 추가 => 안됨!

# List 형변환 => 변경 => Tuple 형변환

# str => list 형변환
word='Hello'
word=list(word)
print(word)

print(str(word))
