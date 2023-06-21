#money=True      # 변수명 = 1 과 같음
#money=False    # 변수명 = 0 과 같음

#if money:       # 참이기때문에 수행됨

# 헷갈리는거    x != y:   <-- x와 y가 같지않은게 참이면 이라는 뜻
#               switch=True
#               if not switch:  <-- 스위치가 트루가 아닌것이 참일때 실행

# money=2000
# card=0

# if money>=3000 or card:
#     print("택시 타고 가라")
# else:
#     print("걸어가라")


# treehit=0

# while treehit<10:
#     treehit+=1
#     print(f'나무를 {treehit}회 찍었습니다. ')
#     if treehit==10:
#         print(f'나무가 넘어 갑니다.')


# number=0

# while not number==4:                  # 0과 4가 같지않은게 참이냐고 묻는거고 참이면 실행
#     number=input("숫자를 입력하세요")
#     if number=='1':
#         print("입력받은 값은 1입니다.")
#     elif number=='2':
#         print("입력받은 값은 2입니다.")
#     elif number=='3':
#         print("입력받은 값은 3입니다.")
#     elif number=='4':
#         print("입력받은 값이 4라서 종료합니다")
#         break

# print(not 0==4)


coffee=10
money=int(input("돈을 넣어주세요"))

while money:
    money-=50
    coffee-=1
    print(f"커피가 나옵니다. 잔돈은 {money}입니다. 남은커피{coffee}잔")
    if money<50:
        print("돈이 부족합니다.")
        break
    elif coffee==0:
        print("커피가 부족합니다.")
        break
