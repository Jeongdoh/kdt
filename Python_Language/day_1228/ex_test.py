#문제1
for num in range(1,10):
    # print(f'---{dan}---', end=' ')
    for dan in range(2,10):
        print(f'{dan}*{num}={dan*num:02}',end = '\n' if dan==9 else ' ')

#리스트 컴프리핸션
gugu=[print(f'{dan}*{num}={dan*num:02}',end = '\n' if dan==9 else ' ') for num in range(1,10) for dan in range(2,10)]


#문제2
def addData(*nums):
    total=0
    for num in nums:
        total+=num
    
    if len(nums)>0:
        return total
    # else:
    #     return None   이 구문이 있으나 없으나 값이 없으면 NONE출력해줌

    return total if len(nums)>0 else None

print(addData())
print(addData(-1,1,0))


