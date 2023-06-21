# --------------------------------------------------------------
# 메모리와 변수
# - 메모리 : 데이터를 저장하는 공간
# - 변  수 : 데이터가 저장된 메모리 주소를 가지고 있음 
#            => 참조하고 있음
#            => 주소로 메모리를 찾아가서 데이터 읽기/변경
# --------------------------------------------------------------
name='Hong'
age=20

# 여려개 변수에 한꺼번에 데이터 저장하는 방법 ----------------
# 언패킹(Unpacking)

data1=('원더우먼', '히어로')
print(data1[0],data1[1])

data2='원더우먼', '히어로'
print(data2[0],data2[1])

data3=[1,2,3]
print(data3[0],data3[1])

data4=1,2,3
print(data4[0],data4[1])


kor,eng,n,art=98,99,'A',81
print(f'kor 타입 => {type(kor)},eng 타입 => {type(eng)},n 타입 => {type(n)},art 타입 => {type(art)}')


# 변수와 복사 --------------------------------------------
year=2022
data=year

nums=[['A'],1,2,3 ]
backs=nums
nums_copy=nums.copy()

print('id(nums) : ', id(nums),  'id(nums_copy) : ', id(nums_copy))
print('nums[0]  :' , nums[0] ,  'nums_copy[0]  : ', nums_copy[0])

nums[0][0]=11

print('nums[0]  :' , nums[0] ,  'nums_copy[0]  : ', nums_copy[0])
print('id(nums) : ', id(nums),  'id(nums_copy) : ', id(nums_copy))

nums[:]

a=3
b=5
a,b=b,a