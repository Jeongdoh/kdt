#다양한 조건문------------------------------------------------------------------
#
#[실습] 해당 점수가 합격/불합격/대기 인지 출력하세요.
# 기준: 80점 이상이면 합격, 70점 이상 대기, 나머지 불합격
jumsu=80


if jumsu>80:
    print(f'{jumsu} 합격')
elif jumsu>=70:
    print(f'{jumsu} 대기')
else:
    print(f'{jumsu} 불합격')


if jumsu>=70:
    if jumsu>80:
        print(f'{jumsu} 합격')
    else:
        print(f'{jumsu} 대기')
else:
    print("불합격")