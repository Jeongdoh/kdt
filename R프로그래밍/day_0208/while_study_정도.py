#3번 map으로 풀기
while 1:
    a,b=input("숫자 입력").split(" ")
    print(a,b)
    if a=='0' and b=='0':
        print("입력받은 숫자가 모두 0입니다.")
        break
    else:
        num1,num2=map(int,[a,b])
        print(num1+num2)


# 리스트 컴프리핸션
a=[i for i in range(1,51) if i%3==0]
print(a)

#문제1.while문을 이용하여 다음처럼 별찍기를 하세요.

while 1:
    for i in range(1,6):
        print(i*'*')
    break


#문제2. fruits = ["사과", "귤", "수박", “딸기”, “바나나”]에서 요소를 while 반복문 사용하여 모두 출력하세요.

fruits = ["사과", "귤", "수박", "딸기", "바나나"]

while 1:
    for i in fruits:
        print(i, end=' ' if i != "바나나" else "\n")
    break


#문제3.두 정수 A와 B를 입력받은 다음 A+B를 출력하는 프로그램을 작성하세요.
#      A, B 모두 0이 들어올때까지 무한 반복하고 A,B 모두 0이 들어오면 멈춥니다.


#int 씌울때는 strip안해줘도 된다!!!

while 1:
    num1=int(input("A를 입력하세요 : ").strip())
    num2=int(input("B를 입력하세요 : ").strip())
    if num1==0 and num2==0:
        print("입력받은 숫자 모두 0입니다.")
        break
    else:
        print(num1+num2)



#문제4. 1부터 100사이의 모든 3의 배수의 합을 계산하여 출력하세요.
while 1:
    a=[]
    for i in range(1,101):
        if i%3==0:
            a.append(i)
    print(sum(a))
    break



#문제5. 정수 안의 각 자리수의 합을 계산하여 출력하세요.. 예를 들어서 1234라면 (1+2+3+4) 10이 출력되어야 합니다.

while 1:
    input_num=int(input("숫자입력 4자리 : "))
    a=input_num//1000
    a
    b=(input_num-1000*a)//100
    b
    c=(input_num-1000*a-100*b)//10
    c
    d=input_num-1000*a-100*b-10*c
    d
    print(a+b+c+d)
    break

