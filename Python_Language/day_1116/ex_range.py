# --------------------------------------------------------
# range() : 내장 함수
#           정수의 범위를 만들어주는 함수
#           예) 1 ~ 50, 1~5
# - 사용법
#   range(시작번호, 끝번호, 간격)
#   range(끝번호) : 0<= ~ <끝번호, 간격 1씩 증가
#   range(1, 끝번호) : 1<= ~ <끝번호 간격 1씩 증가
#   range(1, 끝번호, 2) : : 1<= ~ <끝번호 간격 2씩 증가
# -------------------------------------------------------
# 1~50숫자로 구성된 리스트 객체 생성하세요.
#nums=[1,2,3,4,5,6,7,8,9,10,...,50]

# range 함수 이해하기 -------------------------------------
nums=range(10)
print(f'nums => {nums}, 요소/데이터 수 : {len(nums)}개')
print(f'nums 타입 => {type(nums)}')

nums=list(nums)
print(f'nums => {nums}, 요소/데이터 수 : {len(nums)}개')
print(f'nums 타입 => {type(nums)}')

# 1~10숫자를 저장하는 리스트
nums=range(11)
nums=list(nums)
print(f'nums => {nums}')

nums=range(1,11)
nums=list(nums)
print(f'nums => {nums}')

# 1 ~10 사이 숫자 중 3의 베수로 리스트 구성
# 3, 6, 9
nums=range(3,11,3)
nums=list(nums)
print(f'nums => {nums}')

# 1 ~ 1000으로 구성된 리스트
nums=list(range(1, 1001))
