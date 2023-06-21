# ---------------------------------------------
# 내가 만드는 함수들
# ---------------------------------------------

# ---------------------------------------------
# 기    능 : 2개 숫자를 덧셈 후 반환하는 기능
# 함 수 명 : addTwo
# 매개 변수: num1  num2
# 반 환 값 : 덧셈 결과
# --------------------------------------------- 
def addTwo(num1, num2):
    return num1+num2

# ---------------------------------------------
# 기    능 : 2개 숫자를 뻴셈 후 반환하는 기능
# 함 수 명 : subTwo
# 매개 변수: num1, num2
# 반 환 값 : 뺄셈 결과
# ---------------------------------------------
def subTwo(num1, num2):
    return num1-num2

# ---------------------------------------------
# 기    능 : 2개 숫자를 곱셈 후 반환하는 기능
# 함 수 명 : multiTwo
# 매개 변수: num1 num2
# 반 환 값 : 곱셈 결과
# ---------------------------------------------
def multiTwo(num1, num2):
    return num1*num2

# ---------------------------------------------
# 기    능 : 2개 숫자를 나눗셈 후 반환하는 기능
# 함 수 명 : divTwo
# 매개 변수: num1 num2
# 반 환 값 : 나눗셈 결과
# ---------------------------------------------
def divTwo(num1, num2):
    # if num2>0:
    #     return num1/num2 
    # else:
    #     return None
    return num1/num2 if num2>0 else None

# ---------------------------------------------
# 기    능 : 계산기 프로그램 메뉴 출력 기능
# 함 수 명 : printMenu
# 매개 변수: 없음
# 반 환 값 : 없음
# ---------------------------------------------
def printMenu():
    print('-'*14)   
    print(' <나의계산기>')
    print('-'*14)
    print(' 1.입    력')
    print(' 2.덧    셈')
    print(' 3.뺄    셈')
    print(' 4.곱    셈')
    print(' 5.나 눗 셈')
    print(' 6.종    료')
    print('-'*14) 


# ---------------------------------------------
# 나의 계산기 프로그램
# ---------------------------------------------

# -------------------
#     <나의계산기>
# -------------------
#     1. 입    력
#     2. 덧    셈
#     3. 뺄    셈
#     4. 곱    셈
#     5. 나 눗 셈
#     6. 종    료
# --------------------
isCheck=False
while True:
    #메뉴 출력
    printMenu()

    choice=input("메뉴 선택(1~6): ").strip()
    if choice=='6': 
        print('나의계산기 프로그램을 종료합니다.')
        break
    elif choice=='1':
        nums=input("숫자 2개 입력 :(예: 1, 7) ").strip()
        num1, num2 =nums.split(',')  # ['1','7']
        num1, num2 =int(num1), int(num2)
        print(f'num1 :{num1}/{type(num1)}, num2 :{num2}/{type(num2)}')
        isCheck = True
    elif choice=='2': # 덧셈
        if isCheck:
            print(f'{num1}+{num2}={addTwo(num1, num2)}')
        else:
            print("입력된 데이터가 없습니다.")

    elif choice=='3': # 뺄셈
        if isCheck:
            print(f'{num1}-{num2}={subTwo(num1, num2)}')  
        else:
            print("입력된 데이터가 없습니다.")              

    elif choice=='4': # 곱셈
        if isCheck:
            print(f'{num1}-{num2}={multiTwo(num1, num2)}') 
        else:
            print("입력된 데이터가 없습니다.")            

    elif choice=='5': # 나눗셈
        if isCheck:
            print(f'{num1}-{num2}={divTwo(num1, num2)}')
        else:
            print("입력된 데이터가 없습니다.")






def vending_machine():
    global input_money

    input_money = int(input(" 동전을 투입하세요"))

    menu= choose_menu()
    while (menu != 5 and input_money >= 300):



def plusTwo(num1, num2):
    print(f'num1={num1}, num2={num2}')
    value=num1+num2
    return value


print(plusTwo(1,5))