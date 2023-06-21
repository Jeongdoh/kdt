#------------------------------------------------------------
# 내장 데이터셋_iris
# -데이터분석
# -독립변수, 종속변수
# -선형분석 후 선형식 도출
#------------------------------------------------------------
# 데이터 준비 및 확인-----------------------------------------
source("utils\\util.r")
displayInfo(iris)
iris





# 데이터 전처리-----------------------------------------------
checkNa(iris)
checkMode(iris)

# 데이터 분포 형태 체크---------------------------------------
iris.cor<-cor(iris[-5])
iris.cor
dataDF<-data.frame(length=iris$Petal.Length, width=iris$Petal.width)

plot(dataDF$length,dataDF$width)



# 독립변수 & 종속변수 선택------------------------------------
# 종속 변수 : 너비
# 독립 변수 : 길이


# 선형 회귀식 도출 및 결과 출력-------------------------------
model<-lm(dataDF$width~dataDF$length,data=dataDF)
model

# 선형 회귀식 상세보기
summary(model)


# 회귀 계수만 추출 => coef(선형객체)
mCoef<-coef(model)

# 회귀식 y=기울기*x+절편
pre_y<-mCoef[2]*dataDF$length+mCoef[1]


# 잔차 => (관측치 - 예측치)^2
r_err<-sum((dataDF$width-pre_y)^2)
r_err














