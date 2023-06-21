# ---------------------------------------------------------------------
#while 반복문
# - 반복의 횟수가 고정이 아닌경우 사용하는 반복문
# - 단순 카운팅용 반복문
# - 필수조건] 반복을 중단 할 수 있는 코드 필수
#----------------------------------------------------------------------

#무한 반복문 -----------------------------------------------------------
# 반드시 반복을 종료할 수 있는 코드 또는 업데이트 필수
# while ' ':
#     print("1")

# while 반복문 - (1) 반복카운팅------------------------------------------
# 20번 "Hello World" 출력하기
count=1

while count<=20:
    print('Hello')
    count=count+1  # 중요! 해당코드 없으면 무한반복


count=20
while count>0:
    print('World')
    count=count-1  # 중요! 해당코드 없으면 무한반복




for n in range(20):
    print("Hello World")


#--------------------------------------------------------------------------------
# break => for/while 반복문에 반복을 중단시키는 키워드
#--------------------------------------------------------------------------------
# 1부터 100까지 숫자를 하나씩 더해서
# 덧셈의 결과가 71보다 작을때까지만 더해주세요.
num=1
total=0
while num<=100:
    total=total+num
    print(f'num=>{num}, total=> {total}')
    if total>=71: break
    num=num+1
print(f'total => {total}, num=> {num}')

# for문으로 풀었을때.
total=0
for num in range(1,101):
    total=total+num
    if total>=71: break


#--------------------------------------------------------------------------------
# continue 계속해서...==> for/while 반복문에서
#                         아래 코드 실행하지 않고
#                         제일 위에 코드로 돌아감
#--------------------------------------------------------------------------------
# 1부터 20까지 출력하세요.
num=1
while num<=20:
    print(num)
    num=num+1

# 1~ 20에서 2의 배수만 빼고 출력하세요.
num=1
while num<=20:
    if num%2:
        print(num)
    num=num+1


num=0
while num<=20:
    num=num+1
    if not num%2: continue
    print(num)



num=0
while num<=20:
    num=num+1
    if not num%2: continue
    print(num)


isEnd=False
for n in [1,2,3]:
    if isEnd: break
    for n2 in [11,22,33]:
        if n2>=20:
            isEnd=True
            break
        print(f'n2=>{n2}')

    print(f'n=>{n}')