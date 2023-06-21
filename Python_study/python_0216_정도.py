# def std_weight(height, gender):
#     if gender=='man':
#         height=height*height*22
#         print(f"{height}")
#     elif gender=='woman':
#         height=height*height*21
#         print(f"{height}")

# std_weight(1.77,'man')


# # # # 1. 반복문을 이용하여 60의 약수를 구하세요.
# a=[]
# for i in range(1,61):
#     if 60%i==0:
#         a.append(i)
# print(*a, sep=', ')


# # # 2. 12+22+32+...+n2의 값을 계산하세요.(n=input()으로 받습니다.)
# n=int(input("n의 값을 입력하시오 : "))
# a=[]
# for i in range(1,n+1):
#     a.append(i*i)
# print(sum(a))


# # 3. 커피 자판기를 간단하게 만들어주세요.
# # 돈은 input으로 받습니다.
# # 커피 한잔에 200원입니다.
# # 돈이 부족하거나 종료를 누르면 거스름돈이 나오고 종료됩니다.


# def menu():
#     print("---메뉴 선택---")
#     print("1. 커피뽑기")
#     print("2. 종료")


# money=int(input("돈을 넣어주세요 : "))
# while 1:
#     coffee=200
#     if money>=200:
#         menu()
#         choice=input("메뉴를 선택하세요(예 :1) : ")
#         if choice=='1':
#             print("커피가 나옵니다. 남은 돈은 {0}원 입니다.".format(money-coffee))
#             money=money-coffee
#             if money<200:
#                 print("돈이 부족합니다. 거스름돈은 {0}원 입니다.".format(money))
#                 break
#         elif choice=='2':
#             print("종료합니다. 거스름돈은 {0}원 입니다.".format(money))
#             break
#     else:
#         print("돈이 부족합니다. 거스름돈은 {0}원 입니다.".format(money))
#         break
        

    

# # # 4. 두 정수 A,B를 받아 A+B를 출력하세요. 이 과정을 5번 반복하세요.
# num=1
# while num<=5:
#     A=int(input("A를 입력하세요 : "))
#     B=int(input("B를 입력하세요 : "))
#     print(A+B)
#     num+=1

# ######
# while 1:
#     a,b=map(int, input().split())
#     if a==0 and b==0:
#         break
#     print(a+b)


# ######
# n=int(input())
# for _ in range(n):
#     a,b=map(int,input().split())
#     print(a+b)


# # # 5. 다이아 몬드 모양의 별찍기를 하세요. 단 n=input으로 이루어집니다.

# for 문
# for i in range(1,9+1):
#     print('1'*(9-i),end='')
#     print('*'*(1+(i-1)*2),end='')
#     print('')
# for j in range(9,0,-1):
#     print('1'*(9-j),end='')
#     print('*'*(1+(j-1)*2),end='')
#     print('')



# n=int(input("n을 입력하세요 : "))
# while 1:
#     for i in range(1,n+1):
#         print(' '*(n-i),end='')
#         print('*'*(1+(i-1)*2),end='')
#         print('')
#     for j in range(n,0,-1):
#         print(" "*(n-j+1),end="")
#         print("*"*(1+(j-2)*2),end="")
#         print("")
#     break





# # 호림씨 방법
# n=int(input())
# i=1
# switch=True
# while True:
#     star='*'*(2*i-1)
#     if switch==True:
#         print(star.center(2*n+1))
#         i+=1
#         if i==n+1:
#             switch=False
#     else:
#         print(star.center(2*n+1))
#         i-=1
#         if i==-1:
#             break

# # 호림씨 방법
# n=int(input())
# i=0
# switch=True
# while True:
#     if switch==True: 
#         print(' '*(n-i),'*'*(2*i+1 ))
#         i+=1
#         if i==n+1:
#             switch=False

#     else:
#         if i==-1: 
#             break
#         i-=1        
#         print(' '*(n-i+1),'*'*(2*i-1 )) 







# 6. 5번 문제를 함수로 만들어 보세요.

def diamond(n=int(input("n을 입력하세요 : "))):
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        print('*'*(1+(i-1)*2),end='')
        print('')
    for j in range(n,0,-1):
        print(" "*(n-j+1),end="")
        print("*"*(1+(j-2)*2),end="")
        print("")


diamond()





