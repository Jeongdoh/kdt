# -----------------------------------------------
# for ~ in 반복문
# - 유사하거나 동일한 코드를 줄여서 처리하는 문법
# -----------------------------------------------
msg="Merry Chrismas 2022"
#    0123456789012345678
# print(msg[0])
# print(msg[1])
# print(msg[2])
# print(msg[18])
#for 원소/요소/데이터 in 여러개, 인덱스 객체:
for m in msg:
    print(m,end='')
print()

# --------------------------------------------
# 내장 함수 print(재료) <- 매개변수 parameter
# --------------------------------------------
print(10,20,30, sep='*', end='\t')
print()    
print(10,20,30)  


print("Happy")  # Happy\n
print("Happy", "New", "year")  # Happy New year\n
print("Happy", "New", "year", sep='-')  # Happy-New-year\n

print("Happy", end='\t')  # Happy\t
print("Happy", end='\t')  # Happy\t     Happy\t
print("Happy", end='\t')  # Happy\t     Happy\t     Happy\t
print("Happy", end='\t')  # Happy\t     Happy\t     Happy\t     Happy\t

print()
# -----------------------------------------
# 1~1000숫자 중에서 7의배수로 구성된 데이터
# 데이터의 모든 요소를 출력하고 싶습다
# 단) 한 줄에 10개씩 출력하세요
#------------------------------------------
sevens=[1,2,3,4,5,6,7,8,9,10]
#       0 1 2 3 4 5 6 7 8 9
for num in sevens:
    if num%3:
        print(num, end='\t')  #1\t2\n3\t4\n5\t6\n
    else:
        print(num, end='\n')

# 1~100범위에서 7의 배수만 데이터로 담기
sevens=list(range(7, 101, 7))
print(f'7의 배수 데이터 : {len(sevens)}개\n{sevens}')

# 7의 데이터의 모든 원소 출력
for m in sevens:
    if m%35:
        print(m,end=' ')                #35의 나머지가 0이 아니면 '\t'을 주세요
    else:
        print(m, end='\n')              #35의 나머지가 0이 되고난 뒤는 '\n'을 주고 반복해주세요

print()
# sevens의 인덱스 => 갯수 len(sevens)   
for idx in range(0,len(sevens),2):
    if idx%5==4:
        print(sevens[idx], end='\n')
    else:
        print(sevens[idx], end='\t')

r=range(10) # 0 ~ 9
print(type(r), r, r[0], r[1])