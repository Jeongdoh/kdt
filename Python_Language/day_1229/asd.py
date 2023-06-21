# #-------------------------------------------------------------------------------
# #-------------------------------------------------------------------------------
# # 매개변수 => 값, 가변값, 키=값 가변, 디폴트 값
# #-------------------------------------------------------------------------------
# #-------------------------------------------------------------------------------


# def calc(num1, num2, op='+'):
#     if op =='+':
#         result =num1+num2
#     elif op =='-':
#         result =num1-num2
#     elif op =='*':
#         result =num1*num2
#     elif op == '/':
#         result =num1/num2 if num2>0 else '0으로 나눌 수 없습니다.'

# print(calc(10,2,op='*'))
# print(calc(10,2))




# def calc2(num1, num2, op='+'):
#     if op =='+':
#         result =num1+num2
#     elif op =='-':
#         result =num1-num2
#     elif op =='*':
#         result =num1*num2
#     elif op == '/':
#         result =num1/num2 if num2>0 else '0으로 나눌 수 없습니다.'
#     return result


class Calculator:
    def __init__(self):
        pass

    def add(first, second):
        return first + second

    def sub(first, second):
        return first - second

    def mul(first, second):
        return first * second

    def div(first, second):
        return first / second

    op = 1  # 스위치
    num = []  # 입력받은 값을 넣어줄 리스트
    while op != "=":  #저 밑에 입력받은 oper 문자가 =이 아닐때 까지 반복
        if len(num) >= 1:  # 연산되는 부분 , else문 끝나고 num 리스트 길이가 1보다 크거나 같아지니 실행, 그러나 맨첨엔 아직 받은 값이 없으니 else문으로 내려감
            num1 = int(input("(3) 데이터를 입력해주세요.").strip()) #1 (3) num1이라는 변수에 입력받기
                                                                  #2 연산을 입력받으면 다시 올라와서 len(num) >= 1 조건이 만족되니깐 앞에 값이랑 연산할 숫자를 물어봄
            if op == "+":     #입력받고 부호를 + 누르면 실행
                num[0] = add(num[0], num1)      #num[0] 이라는 인덱스 변수에 add함수를 불러서 else에서 추가된 값과 방금 입력받은 num1값을 더해서 num[0]변수에 저장
                print(num[0])       #확인을 위해 출력해줌

            elif op == '-':   #입력받고 -누르면 실행
                num[0] = sub(num[0], num1)  #위랑 똑같음
                print(num[0])   #위랑 똑같음

            elif op == '*':   #입력받고 *누르면 실행
                num[0] = mul(num[0], num1)  #위랑 똑같음
                print(num[0])   #위랑 똑같음

            elif op == '/':   #입력받고 /누르면 실행
                if num1 == 0:   #근데 만약에 num1값이 0이되면 나눌수가 없으니까 브레이크 시켜주기위해서
                    print("0으로 나눌 수 없습니다") # 프린트문 실행하고
                    break   #브레이크

                else:       # 그게아니고 나눌수 있다면
                    num[0] = div(num[0], num1)      # 아까처럼 값을 나눠서 num[0]인덱스에 담아줌
                    print(num[0])   #그리고 num[0]리스트를 출력

            elif op == "=":   #만약에 입력받은 오퍼값이 =이면 마지막 연산값을 출력후 브레이크되어짐
                print(f'결과값 : {num[0]}')
                break
            op = input("(4) 연산자를 입력해주세요.").strip()  
            #1 (4) 숫자를 더하고나면 다시 실행되는 연산자 묻는 입력함수\
            #2 부호 받고 결과를 출력하면 그 값에 다시 연산자를 입력함

        else:       # 첨에 실행하면 len(num) >= 1 위 조건에 맞지않으니 else문으로 들어옴
            num1 = int(input("(1) 데이터를 입력해주세요.").strip()) # (1) 데이터를 입력받고 int로 변형된 숫자로 형변환해줌

            op = input("(2) 연산자를 입력해주세요.").strip() # (2) 연산자를 입력하고

            num.append(num1) #num1에 입력받은 형변환된 숫자만 num이라는 빈리스트에 추가 추가되고 나면!!!!!!!!!!