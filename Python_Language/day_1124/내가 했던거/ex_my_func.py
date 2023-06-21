#---------------------------------------------------------------
#내가 만드는 함수들
#---------------------------------------------------------------

#-------------------------------------------------------------------------------
#기 능 : 2개 숫자를 덧셈 후 반환하는 기능
#함 수 명 : 
#매개 변수 : 
#반 환 값 : 
#--------------------------------------------------------------------------------




def num_plus(num1,num2):
    print(f'{num1}+{num2}={num1+num2}')
    value=num1+num2
    return value

print(num_plus(21,9))


#-------------------------------------------------------------------------------
#기 능 : 2개 숫자를 뺄셈 후 반환하는 기능
#함 수 명 : nums_plus
#매개 변수 : num1, num2
#반 환 값 : 덧셈값
#--------------------------------------------------------------------------------


def num_minus(num1,num2):
    print(f'{num1}-{num2}={num1-num2}')
    value=num1-num2
    return value


print(num_minus(21,9))


#-------------------------------------------------------------------------------
#기 능 : 2개 숫자를 곱셈 후 반환하는 기능
#함 수 명 : 
#매개 변수 : 
#반 환 값 : 
#--------------------------------------------------------------------------------

def num_n(num1,num2):
    print(f'{num1}*{num2}={num1*num2}')
    value=num1*num2
    return value


print(num_n(21,9))


#-------------------------------------------------------------------------------
#기 능 : 2개 숫자를 나눗셈 후 반환하는 기능
#함 수 명 : 
#매개 변수 : 
#반 환 값 : 
#--------------------------------------------------------------------------------


def num_m(num1,num2):
    if num2>0:
        return num1/num2
    else:
        return None
    
    return num1/num2 if num2>0 else None
    # print(f'{num1}/{num2}={num1/num2}')   #내가 한거
    # value=num1/num2
    # return value


# print(num_m(21,9))


#-----------------------------
#       <나의 계산기>
#-----------------------------
#       1. 입    력
#       2. 덧    셈
#       3. 뺄    셈
#       4. 곱    셈
#       5. 나 눗 셈
#       6. 종    료
#-----------------------------


isCheck=False
while True:
    print('-'*14)
    print('<나의 계산기>')
    print('-'*14)
    print('1. 입    력')
    print('2. 덧    셈')
    print('3. 뺄    셈')
    print('4. 곱    셈')
    print('5. 나 눗 셈')
    print('6. 종    료')
    print('-'*14)

    choice=input("메뉴 선택(1~6): ").strip()
    if choice=='6':
        print('나의계산기 프로그램을 종료합니다.')
        break


    elif choice=='1':
        nums=input("숫자 2개 입력 : (예: 1, 7) ").strip()
        num1, num2=nums.split(',')
        num1, num2=int(num1), int(num2)
        print(f'num1 : {num1}/{type(num1)}, num2 : {num2}/{type(num2)}')
        isCheck=True

    elif choice=='2': # 덧셈
        if isCheck:
            print(num1, '+', num2,'=', num_plus(num1, num2))
        else:
            ("입력된 데이터가 없습니다.")

    elif choice=='3': # 뺄셈
        if isCheck:
            print(num1, '-', num2,'=', num_minus(num1, num2))
        else:
            ("입력된 데이터가 없습니다.")

    elif choice=='4': # 곱셈
        if isCheck:
            print(num1, '*', num2,'=', num_n(num1, num2))
        else:
            ("입력된 데이터가 없습니다.")


    elif choice=='5': # 나눗셈
        if isCheck:
            print(num1, '/', num2,'=', num_m(num1, num2))
        else:
            ("입력된 데이터가 없습니다.")
    