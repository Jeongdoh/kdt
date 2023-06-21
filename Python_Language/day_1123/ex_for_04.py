# ----------------------------------------------
# for 반복문 - 리스트 컨프리핸션(내포)
# ----------------------------------------------
# nums리스트의 요소들을 nums2에 담겠습니다.
# 단 nums요소들의 값에 3을 곱한 값으로 담아주세요.

# 단순 List와 for문 ============================= 
nums=[1,2,3]
nums2=[]
for n in nums:
    nums2.append(n*3)

nums3=[n*3 for n in nums]    
#      --- -------------
#       2       1

print(f'nums2=> {nums2}')    
print(f'nums3=> {nums3}') 

# List와 for문 if문 ============================ 
# nums의 요소값이 짝수인것만 nums2에 3을 곱해서 
# 넣어주세요.
nums=[1,2,3,4,5,6,7]
nums2=[]
for n in nums:
    # if not n%2 :  # 2로 나눈 나머지값 0, 1 => False, True
    #     nums2.append(n*3)

    if n%2==0 :  # 2로 나눈 나머지값 0, 1 => False, True
        nums2.append(n*3)

nums3=[ n*3  for n in nums  if not n%2  ]  
#       ---  -------------  ----------  
#        3        1             2 결과 True >> 3번으로 이동
#                 1             2 결과 False >> 1번으로 이동    

print(f'nums2=> {nums2}')        

# List와 for문 if문 else ============================ 
# nums의 요소값이 짝수인은 nums2에 3을 곱해서 넣고
# 홀수인것은 그대로 리스트에 추가 
nums=[1,2,3,4,5,6,7]
nums2=[]

for n in nums:
    # if n%2:
    #     nums2.append(n)
    # else:
    #     nums2.append(n*3)
    nums2.append(n if n%2 else n*3)

nums3=[ n if n%2 else n*3  for n in nums ]
#       -----------------  --------------
#              2                  1
print(f'nums2=> {nums2}')        