# -----------------------------------------------------
# 편상관관계 & 편상관계수
# > 두 변수의 상관관계에 영향을 미치는 제 3의 변수에
# 의해서 잘못 검사된 상관계수 도출 가능성 있음

# >해당 문제를 해결하기 위한 제 3의 변수를 제어(통제)해서
# 상관계수 값 추출 하도록 함
# ------------------------------------------------------

# 내장 데이터 셋 - mtcars--------------------------------

source("utils\\util.r")

# mtcars 데이터 정보 확인
displayInfo(mtcars)
# (1)데이터와 데이터 타입 체크
# 숫자 또는 문자 => 범주형
mtcars2<-within(mtcars,{
    vs<-factor(vs, label=c("V","S"))
    am<-factor(vs, label=c("auto","menu"))
    cyl<-ordered(cyl)
    gear<-ordered(gear)
    carb<-ordered(carb)
})

displayInfo(mtcars2)


# 전처리-------------------------------------------------
# (1) 결측치 체크
checkNa(mtcars)

# (2) 최빈값 체크
checkMode(mtcars)

# 기술통계 분석-------------------------------------------
# 연비 - 마력(hp), 무게(wt), 실린더(cyl) 값 확인
mtcars.cor<-cor(mtcars)
cor(mtcars[-8])
class(mtcars.cor[,"mpg"])
mtcars[which.max(cor(mtcars)),'carb']
#mpg와 상관계수가 가장 높은 컬럼과 가장 낮은 컬럼
# (1) mpg와 나머지 컬럼과의 상관계수 값 추출
mtcars.cor[,"mpg"]

# (2) 정렬 또는 가장 높은 컬럼과 가장 낮은 컬럼
# mpg컬럼만 추출 mpg데이터 제거
corData<-mtcars.cor[,'mpg']
corData<-corData[-1]

# 최대값, 최소값
max(corData)
min(corData)

# 정렬 후 저장
ret<-sort(corData)
ret

# 범주형 제거 후 상관계수 전체
cor(mtcars2[-c(2,8:11)])

# 상관계수값 확인 후 2개 변수 선택--------------------
# 연관성이 있는 변수 선택
# pcor(,9k,,9)



























