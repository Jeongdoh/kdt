#----------------------------------------------------------------
# 메모리와 변수
# -메모리 : 데이터를 저장하는 공간
# -변  수 : 데이터가 저장된 메모리 주소를 가지고있음 
#        => 참조하고 있음
#        => 주소로 메모리를 찾아가서 데이터 읽기/변경
#-----------------------------------------------------------------
name='Hong'
age=20

# 여러개 변수에 한꺼번에 데이터 저장하는 방법
# 언패킹(unpacking)
name, age= ('마징가', 12)
data1=('원더우먼', '히어로')
data2='원더우먼', '히어로'
kor, eng, math, art=[98,99,100,81]

print(f'name= {name} | {type(name)}age => {age}')
print(f'data1= {data1} | {type(data1)}')
print(data1[0],data1[1], data2[0], data2[1] )
print(kor, eng )


# 변수와 복사---------------------------------------------------------
year=2022
data=year

nums=[['A'],1,2,3]
backs=nums
nums_copy=nums.copy()  # 얕은복사

print('id(nums) : ', id(nums), 'id(nums_copy): ', id(nums_copy))
print('nums[0] :' , nums[0] , 'nums_copy[0] :' , nums_copy[0])


nums[0][0]=11

print('nums[0] :' , nums[0] , 'nums_copy[0] :' , nums_copy[0])
print('id(nums) : ', id(nums), 'id(nums_copy): ', id(nums_copy))

