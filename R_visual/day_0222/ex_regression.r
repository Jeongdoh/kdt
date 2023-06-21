#-----------------------------------------------------------------
# 회귀(Regression)
# - 선형 데이터의 관계를 나타내는 모델 => 선형회귀모델 또는 선형회귀식
# - 전제 : 선형관계에 데이터
# - 예측 => 미래 데이터에 대한 예측 가능해짐
#-----------------------------------------------------------------
# 데이터 준비 -----------------------------------------------------
library(HistData)
source("utils\\util.r")

# 콜덴 패밀리 데이터셋 정보 확인
displayInfo(GaltonFamilies)


# 전처리-----------------------------------------------------------




# 부모 키 & 자식 키 데이터 관련성-----------------------------------
family_df<-GaltonFamilies

# by 그래프
plot(family_df$midparentHeight,family_df$childHeight)


# by 수치
shapiro.test(family_df$midparentHeight)
shapiro.test(family_df$childHeight)

cor(family_df$midparentHeight,family_df$childHeight)
cor(family_df$midparentHeight,family_df$childHeight, method = "kendall")


# 부모의 키와 자식의 키에 영향이 있다=> 직선
# 종속~독립<==family_df$childHeight~family_df$midparentHeight
#lm()
lm(family_df$childHeight~family_df$midparentHeight,data=family_df)


# 임의의 값 생성
set.seed(14)
x<-runif(n=7,min=0,max=10)
y<-3+2*x+rnorm(n=7,mean=0,sd=5)
round(x,2)
round(y,2)

str(df)
# 선형회귀모델
model<-lm(y~x,data=df)
coef(model)
intercept<-coef(model)[1]
slope<-coef(model)[2]
y.hat<-intercept+slope*x
round(y.hat,2)
r<- y-y.hat
round(r,2)

