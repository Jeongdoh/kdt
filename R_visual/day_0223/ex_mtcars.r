#-----------------------------------------------------------
# 내장 데이터 셋 mtcars
# -독립변수 & 종속변수
source("utils\\util.r")
mtcars
displayInfo(mtcars)

checkNa(mtcars)
checkMode(mtcars)
colnames(mtcars)
mtcars.cor<-cor(mtcars[-5])
mtcars.cor


# 데이터 전처리
# 데이터 컬럼 상관계수 확인 후 상관계수 0.7이상 컬럼만 추출
sortData<-sort(abs(cor(mtcars)[,"mpg"]),decreasing=T)[-1]
selNames<-names(sortData<-sortData[sortData>0.7])
selNames<-c(selNames,"mpg")

mtcars[,selNames]
str(mtcars)


# 다중선형모델 생성------------------------------------------------
# 종속변수 ~ .
mModel<- lm(mtcars$mpg~.,data = mtcars)


# (1) 회귀계수
coef(mModel)

# (2) 잔차체크
resid(mModel)

# (3) 선형회귀식기반 연비 예측 결과
pre_value<-round(fitted(mModel),1)
pre_value

x<-1:dim(mtcars)[1]
x

plot(x, pre_value, col='blue',pch=20, cex=2)


# 예측해주는 함수 => predict()

library(car)
Prestige


sData<-scale(Prestige$income)
sData

mean(sData); sd(sData)

mean(Prestige$income); sd(Prestige$income)

# -회귀모델 생성





# -회귀계수만 출력





#-----------------------------------------------------------
