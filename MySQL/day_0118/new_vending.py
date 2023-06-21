def printMenu():
    global in_money

    in_money=int(input("동전을 투입해주세요 :  (예) 300 ").strip())

    print('-'*14)
    print('-'*14)   
    print('커피 자판기 (300원)')
    print('1.블랙 커피')
    print('2.프림 커피')
    print('3.설탕 프림 커피')
    print('4.재고 현황')
    print('5.종     료')
    print('-'*14)
    print('-'*14)

    return choice=input("메뉴를 선택하세요: ").strip()


def black_coffee(in_money):
    print(f"블랙 커피를 선택하셨습니다. 잔돈: {in_money-300}")

    machine_coffee = machine_coffee-30
    water = water-100
    cup = cup-1
    in_money-=300
    


def frima_coffee(in_money):
    print(f"프림 커피를 선택하셨습니다. 잔돈: {in_money-300}")
    #global in_money
    machine_coffee=machine_coffee-15
    frima=frima-15
    water=water-100
    cup = cup-1
    in_money-=300
    


def sugar_coffee(in_money):
    print(f"설탕 프림 커피를 선택하셨습니다. 잔돈: {in_money-300}")
    #global in_money  
    machine_coffee=machine_coffee-10
    frima=frima-10
    sugar=sugar-10
    water=water-100
    cup = cup-1
    in_money-=300
    


def machine_stock(in_money):
    print(f"재고 현황 :\n커피: {machine_coffee}, 프림: {frima}, 설탕: {sugar},\n물: {water}, 종이컵: {cup},\n자판기 남은 돈: {machine_money+in_money}, 잔돈 현황: {in_money}")


machine_money=10000
water=1000
machine_coffee=500
frima=500
sugar=500
cup=30



in_money=int(input("동전을 투입해주세요 :  (예) 300 ").strip())
if in_money<300:
    print(f"잔돈이 부족해서 종료합니다.")
while 1:

    
    if in_money>=300:
        printMenu()

        choice=input("메뉴를 선택하세요: ").strip()

        if choice=='5': 
            print('커피 자판기 동작을 종료합니다.')
            break
        elif choice=='1':
            black_coffee()
            if in_money<300:
                print(f"잔돈이 부족해서 종료합니다.")
                break

        elif choice=='2':
                frima_coffee()
                if in_money<300:
                    print(f"잔돈이 부족해서 종료합니다.")
                    break

        elif choice=='3':
                sugar_coffee()
                if in_money<300:
                    print(f"잔돈이 부족해서 종료합니다.")
                    break

        elif choice=='4':
                machine_stock()
                if in_money<300:
                    print(f"잔돈이 부족해서 종료합니다.")
                    break
        else:
            print(f"잔돈이 부족해서 종료합니다.")
            break
    else:
        print(f"돈이 부족합니다 {in_money}원.")
        break




