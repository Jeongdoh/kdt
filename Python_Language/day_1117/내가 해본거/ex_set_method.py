#-----------------------------------------------------------------
#set 자료형 메서드
#------------------------------------------------------------------
# 아래 문자열에서 중복 알파벳은 제거 후 저장하기
msg="merry christmas Happy new year"
msg=msg.replace(' ','')
print(msg)

data=set(msg)
print(data)

# set 자료형에 요소 추가 메서드 => set.add(요소)
data.add("H")
print(data)
print(list("Hab"))


# set 자료형에 여러개의 요소 추가 메서드 => set.update()
data.update(['A', 'Hab', 'Happy'])
print(data)

nums={1,4,2,3,}
nums.add(1)
nums.update([5,6,4,3,5,6])
print(nums)


# 요소 제거하는 메소드 => set.remove(요소)
nums.remove(4)
print(nums)

# 요소 꺼내는 메서드 = set.pop(요소)
nums.pop()
print(nums)

#---------------------------------------------------------------------------
# 멤버 연산자 A in B => a가 b에 존재하면 true/ 없으면 false
# 멤버 연산자 A not in B => a가 b에 존재하면 false/ 있으면 true
#---------------------------------------------------------------------------
print(f'3 in [1,3,5,] => {3 in [1,3,5,]}')
print(f'7 in [1,3,5,] => {7 in [1,3,5,]}')

print(f'H in "Hello" => {"H" in "Hello"}')
print(f'b in "Hello"=> {"b" in "Hello"}')

print(f' A in {{"A" :10, "B":30}} => {"A" in {"A":10, "B":30} }')
print(f' 10 in {{"A" :10, "B":30}} => {10 in {"A":10, "B":30} }')
