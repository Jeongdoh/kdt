#---------------------------------------------------------------------------------
# 모듈(module) 및 패키지(package)살펴보기
#
# [조건] 동일한 목표/ 목적으로 구성됨
# 모듈(module) - 변수, 함수, 클래스를 하나의 파일로 묶은것 
# 패키지(package) - 모듈들을 하나로 묶은 것
#---------------------------------------------------------------------------------
# 사용법
# 모듈안의 모든 것 포함하기
# import 모듈명             => 모듈명.변수명, 모듈명.함수, 모듈명.클래스
# import 모듈멸 as 별칭     => 별칭.변수명, 별칭.함수, 별칭.클래스
#
# 모듈안에서 선택한 것만 포함하기---------------------------------------------------
# from 모듈명 import 변수, 함수, 클래스 => 변수명, 함수, 클래스
#---------------------------------------------------------------------------------


# 파이썬 기본제공 모듈, 표준모듈
# import math as m            # 모듈전체 포함
# from math import pow        # 모듈에서 선택한 것만 포함
from math import *          # *아스타리크 의미 : 모든 것




# 포함한 모듈사용하기--------------------------------------------------------------
# print(m.pi)                 # 모듈명.변수명
# print(m.factorial(5))       # 모듈명.함수명()
print(pow(2,3))               # from import 함수명()
print(factorial(4))           # from import 함수명()


# 임의의 수 생성 관련 모듈 사용=====================================================
import random as rm

# 임의의 숫자를 1개 출력
# random() : 0.0<~<=1.0 사이의 임의의 실수 반환
for _ in range(10):
    print(round(rm.random()*10, 2), end=' ')

print('\n------------------------------------------------------')

# 범위지정 임의의 정수 숫자 1개 출력
# randint(st num, ed num): st num<= ~ <= ed num 사이의 임의의 정수 반환
for _ in range(10):
    print(rm.randint(1, 5), end=' ')

print('\n------------------------------------------------------')


# 지정된 범위에서 임의의 숫자 범위 생성
# randrange(start, end, step)
print(rm.randrange(1,50,2))




# mylotto----------------------------------------------------------------
import random as mylotto

a=[]

for i in range(6):
    if i not in a:
        a.append(mylotto.randint(1,45))
    a.sort()
print(*a)


print('------------------------------------------------------')


for _ in range(6):
    print(mylotto.randrange(1,46), end=' ')


print('\n------------------------------------------------------')


# 파일입출력에서 open() 함수랑 함께 사용================================================
import os.path

FILE_NAME='Good.txt'
if not os.path.exists(FILE_NAME):
    print("존재하는 파일인지 체크하세요")
else:
    fp=open(FILE_NAME, mode='r', encoding='utf-8')
    print(fp.read())
    fp.close()
