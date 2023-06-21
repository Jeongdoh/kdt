# 1. 아래 데이터를 활용하여 분석해 주세요. - heightweight.csv iris.csv
# - 전처리 - 데이터 기술통계
hw_df<-read.csv("day_0223\\data\\height_weight.csv")
iris_df<-read.csv("day_0223\\data\\iris.csv")

source("utils\\util.r")

# -------------------------------------------------------------------
# 선형회귀 분석
# -조건 : 선형성이 존재
#        독립변수 - 종속변수 => 인과관계, 상관관계
#        정규분포 형태로 데이터 분포
# - 결과 : 선형회귀식 => 회귀계수
# - 평가 : RSE 작을 수록, R^2 높을 수록
# - 검정 : 잔차에 대한 검정
# -------------------------------------------------------------------
# 데이터 준비 --------------------------------------------------------
file="day_0223\\data\\iris.csv"
iris_df<-read.csv(file)


# 데이터 기본 정보 확인------------------------------------------------
# (1) 수치값으로 확인
str(iris_df)
summary(iris_df)

# (2) 그래프로 확인
# 컬럼과 컬럼 사이의 관계
plot(iris_df)

# 컬럼별 정규성 확인 >>qqnorm()/qqline()/hist()/lines()
par(mfrow=c(2,4))

for(col in colnames(iris_df)[-5]){
    qqnorm(iris_df[,col],main=paste(col,"Q-Q"))
    qqline(iris_df[,col],col='red',lwd=2)
}


for(col in colnames(iris_df)[-5]){
    hist(iris_df[,col],freq=FALSE,main=paste(col,"HIST"))
    lines(density(iris_df[,col]),col='red',lwd=2)
}


class(iris_df$sepal_length)
class(iris_df["sepal_length"])
class(iris_df[,"sepal_length"])


shapiro.test(iris_df$petal_length)
shapiro.test(iris_df$petal_width)


# (3) 통계함수 수치 값 확인
# 컬럼과 컬럼 사이의 관계 => cor.test()(변수1, 변수2)
# => petal_length, petal_width 선택
cor.test(iris_df$sepal_length,iris_df$petal_length)
cor.test(iris_df$sepal_length,iris_df$sepal_width)
cor.test(iris_df$petal_length,iris_df$petal_width)


# 컬럼별 정규성 확인 >> shapiro.test()
for(col in colnames(iris_df[-5])){
    print(paste(col,round(shapiro.test(iris_df[,col])$p.value, 4)))
}


# 데이터 전처리----------------------------------------------------
# (1) 결측치 체크 & 최빈값

# (2) 중복 데이터 체크 => unique()

# (3) 이상치 체크 & 처리

# (4) 데이터의 값의 범위 => 데이터 변환 scale()

#------------------------------------------------------------------
# petal_length, petal_width의 선형회귀 분석 구현
# - 독립변수 : petal_length
# - 종속변수 : petal_width
# - 분석방식 : 단순선형회귀
# - lm(종속 ~ 독립 ,data=데이터)
#------------------------------------------------------------------


# (1)단순 선형회귀 모델 생성
irisMD<-lm(iris_df$petal_width~iris_df$petal_length, data = iris_df)
irisMD

# (2)단순선형회귀 관련 값들 확인

# (2-1)회귀계수 coef()
iris_slope<-round(coef(irisMD)[2],4)
iris_inter<-round(coef(irisMD)[1],4)
iris_slope;iris_inter

# (2-2) 잔차 확인 => resid()
mean(resid(irisMD)^2)


# (3) 예측값 : 회귀식 실행결과
pre_y<-fitted(irisMD)

iris_df$petal_width[1]; pre_y[1]

# (4) 단순선형회귀 보고서(설명서)
summary(irisMD)

#------------------------------------------------------------------
# 잔차검정
# - 정규성 : shapiro.test()
# - 등분산성 : ncvTest() <- car 패키지
# - 독립성 : lmtest패키지 > dwtest()
#------------------------------------------------------------------

# (1) 모델에 대한 검정그래프 출력
plot(irisMD)

# (2) 함수기반 수치값 검정
# (2-1) 정규성
shapiro.test(resid(irisMD))

# (2-2) 등분산성
library(car)
ncvTest(irisMD)

# (2-3) 독립성
library(lmtest)
dwtest()








