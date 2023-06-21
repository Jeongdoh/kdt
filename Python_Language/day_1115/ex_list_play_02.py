# -----------------------------------------------------
# List 자료형 가지고 놀기
# -------------------------------------------------------
# [실습2] 3과목 점수를 입력 받고 합계, 평균 계산하여 출력
#        (조건) 과목별로 점수 입력 받기 => input() 3번 호출
# - 생각1 : input() 3번 실행
# - 생각2 : 3개 문자열 데이터 생성
# - 생각3 : 3개 문자열 데이터를 하나에 담기 => list
# - 생각4 : 아무겂도 없는 빈 리스트 준비 => 추가 메서드 append()/insert()
# - 생각5 : 숫자 문자열 => 정수 변환 => int()
# - 생각6 : 합게 ==> 리스트안에 모든 요소 더하기
#           평균 ==> 합계/갯수 len()
# -------------------------------------------------------------
# 방법1) 
# # (1) 3과목 입력 받기
# kor=input("국어 점수 입력 : ")
# eng=input("영어 점수 입력 : ")
# math=input("수학 점수 입력 : ")

# # (2) str -> int 타입변환
# kor=int(kor)
# eng=int(eng)
# math=int(math)
# (1)(2) 3과목 입력 받고 int 타입 변환
kor=int(input("국어 점수 입력 : ").strip())
eng=int(input("영어 점수 입력 : ").strip())
math=int(input("수학 점수 입력 : ").strip())

# (3) 정수 형태에 3과목을 합계 / 평균
total=kor+eng+math
avg=total/3

# (4) 결과 출력
print(f'{kor},{eng},{math} 3과목  합계 : {total}, 평균 : {avg}')


# 방법2) list사용해서 해결하기
# (1) 3과목 점수를 저장할 빈 리스트 변수 선언
jumsu=[]

# (2) 입력 받은 과목 점수를 리스트에 추가 => append()
value=input("국어 점수 : ")
value=int(value)
jumsu.append(value)

# 3줄의 코드를 1줄 코드로 가능 
#jumsu.append(int(input("국어 점수 : ")))

value=input("영어 점수 : ")
value=int(value)
jumsu.append(value)

value=input("수학 점수 : ")
value=int(value)
jumsu.append(value)

print(f'3과목 점수 => {jumsu}')

# (3) 합계 & 평균
total=jumsu[0]+jumsu[1]+jumsu[2]

# 내장함수 sum(): 여러개 값의 합계 반환
total=sum(jumsu)
avg=total/len(jumsu)


# (4)결과 출력
print(f' 3과목 합계 :{total}점\n평균 : {avg:^10.1}점') # 평균값이 이상하게 나오는건 진수표기법이라서 그렇다고함
