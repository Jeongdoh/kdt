# class Calculator:
#     def __init__(self, *x):
#         self.z=[]
#         for y in x:
#             if y==int(y):
#                 self.z.append(int(y))
#             else:
#                 self.z.append(y)
        
            
#     def __add__(self):
#         return sum(self.z)

#     def __sub__(self):
#         num=0
#         for y in self.z:
#             num-=y
#         return num

#     def __mul__(self):
#         num=1
#         for y in self.z:
#             num*=y
#         return num

#     def __truediv__(self):
#         num=1
#         for y in self.z:
#             num/=y
#         return num




# cal1=Calculator(5,5.0,7,12,4)
# print(cal1.__add__())
# print(cal1.__mul__())
# print(cal1.__sub__())
# print(cal1.__truediv__())



# class calc : 
    
#     def __init__(self,*x):
#         self.x = x
        
          
#     def plus(self):
#         v=0
#         for c in list(self.x) :
#           v = v+c
#         return v

#     def minus(self):
#         v=0
#         for c in list(self.x) :
#           v = v-c
#         return v

#     def multi(self):
#         v=1
#         for c in list(self.x) :
#           v = v*c
#         return v

#     def truediv(self):
#         v=1
#         for c in list(self.x) :
#           v = v/c
#         return v



# d = calc(5,5.0)
# print(d.plus())
# print(d.minus())
# print(d.multi())
# print(d.truediv())




# id='900312-1034567'
# A=[]
# 별자리=['물병자리','물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','궁수자리','염소자리']
# 띠=['원숭이띠','닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠','용띠','뱀띠','말띠','양띠']


# if int(id[7])==1 or int(id[7])==2:
#     A.append(19)
# else:
#     A.append(20)

# for i in id:
#     if i.isdigit():
#         A.append(int(i))

# print(A)

# #나이

# B=A[0]*100+A[1]*10+A[2]+A[3]
# print(B)
# print(f'{2022-B+1}세',end=', ')


# #생년월일
# print(f'{B}년{A[3]*10+A[4]}월{A[5]*10+A[6]}일',end=' ')


# #띠
# if B%12 ==0: print(띠[0],end=' ')
# if B%12 ==1: print(띠[1],end=' ')
# if B%12 ==2: print(띠[2],end=' ')
# if B%12 ==3: print(띠[3],end=' ')
# if B%12 ==4: print(띠[4],end=' ')
# if B%12 ==5: print(띠[5],end=' ')
# if B%12 ==6: print(띠[6],end=' ')
# if B%12 ==7: print(띠[7],end=' ')
# if B%12 ==8: print(띠[8],end=' ')
# if B%12 ==9: print(띠[9],end=' ')
# if B%12 ==10: print(띠[10],end=' ')
# if B%12 ==11: print(띠[11],end=' ')


# #별자리
# C=A[3]*1000+A[4]*100+A[5]*10+A[6]



# if 120 <= C <=218: print(별자리[0])
# if 219 <= C <=320: print(별자리[1])
# if 321 <= C <=419: print(별자리[2])
# if 420 <= C <=520: print(별자리[3])
# if 521 <= C <=621: print(별자리[4])
# if 622 <= C <=722: print(별자리[5])
# if 723 <= C <=822: print(별자리[6])
# if 823 <= C <=923: print(별자리[7])
# if 924 <= C <=1022: print(별자리[8])
# if 1023 <= C <=1122: print(별자리[9])
# if 1123 <= C <=1224: print(별자리[10])
# if 1225 <= C or C <=119: print(별자리[11])

# print(C , end=' ')




# def gugudan(start_n,end_n):
#     n = start_n
#     k = 1
#     switch = True       #반복문 안에 스위치라는 변수의 브레이크를 만들어둠 *기능
    
#     while k != 10:      #k가 10이 아닐동안 반복
#         if switch:      #스위치가 참이면 실행
#             print(f"--[{n}단]--",end='     ')   #--2단-- --3단-- 문을 출력하고 공백을 줌 
#             n +=1                               #start_n단 ~ end_단까지 먼저 출력되기위해 n에+1 

#             if n==end_n+1:      #위 if문이 실행되다가 2~9단까지 출력되기 위해서 n과 end_n까지 출력 후 
#                 switch = False      #break
#                 n = start_n         #이후에 n*1 n*2...처럼 출력하기 위해 n을 초기화
#                 print()             #줄바꿈

#         if switch==False:       #스위치가 false 인게 참이면 실행
#             print(f"{n}*{k}= {n*k:2}",end='       ')        #초기화된 n값과 k=1을 곱해서 2*1 3*1...9*1 이렇게 출력하는 기능
#             n +=1               #2*1, 3*1....9*1 을 위해 n에 1씩 +

#             if n==end_n+1:      #위 if문 출력하다가 만약 n이 9*1까지 출력하고 n이 10이되면
#                 n = start_n         # n은 다시 2*2를 위해 초기화
#                 k +=1               # k는 n*2...n*9를위해 1씩 +
#                 print()             #


# gugudan(2,9)

# for dan in range(2,10):
#     print(f'---{dan}---', end=' ')
# print()


# gugu=[ print(f'{dan}*{num}={dan*num:2}',end = '\n' if dan==9 else '  ') for num in range(1,10) for dan in range(2,10)]





for i in range(1,4):
    print('----------')