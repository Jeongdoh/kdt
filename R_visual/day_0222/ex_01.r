#-----------------------------------------------------------
#상관관계 & 상관분석
# - 상관계수 : -1 ~ 1
#-----------------------------------------------------------
# 다른 R 스크립트 파일 포함----------------------------------
source("utils\\util.r")
# 데이터 준비 - 내장 데이터셋 cats---------------------------
# 기본정보 확인
library(MASS)
displayInfo(cats)


# 전처리----------------------------------------------------
# (1) 결측치=>is.na()- 원소단위 , complete.cases()- 행 단위
checkNa(cats)

# (2) 최빈값
# 요소에 대한 빈도 데이블, 최빈값 체크
checkMode(cats)


# (3) 이상치/ 특이값 체크
# => 과제

# 기술통계 분석 - 그래프 방식 -----------------------------
# 컬럼/변수 2개에 대한 산점도
# 포뮬러 형식 : 종속 ~ 독립
# 종속 변수 : 심장무게
# 독립 변수 : 몸무게
plot(cats$Hwt~cats$Bwt,main="고양이 무게에 따른 심장무게",
    xlab="몸무게(BWT, kg)",ylab="심장무게(HWT, g)")

# 기술통계 분석 - 통계함수 / 수치 방식 -----------------------------
# (1) 변수 / 칼럼의 상관관계 체크
# => 정규분포 여부 --> 계산 방법 선정

# (1-1) 정규성 검정 >>
shapiro.test(cats$Hwt)
shapiro.test(cats$Bwt)


# (1-2) 상관관계 계산 방법 검정 및 계산
# >> 몸무게랑 심장무게랑 양의 상관관게가 있다.
cor(cats$Hwt, cats$Bwt)
cor(cats$Hwt, cats$Bwt,method = "spearman")
cor(cats$Hwt, cats$Bwt,method = "kendall")


# 검증----------------------------------------------------------
# 귀무가설 : 상관계수가 0 이다. 즉, 아무런 관련이 없다.
cor.test(cats$Hwt,cats$Bwt)

cor.test(cats$Hwt,cats$Bwt,method="spearman")
cor.test(cats$Hwt,cats$Bwt,method="kendall")



# 데이터 준비 - 내장 데이터셋 iris---------------------------
# (1) 데이터 기본 정보 확인
displayInfo(iris)


# 전처리----------------------------------------------------
# (1) 결측치 체크
checkNa(iris)

# (2) 최빈값 체크 <- NA가 아닌 이상 데이터 확인
checkMode(iris)

# 기술통계 분석----------------------------------------------

# 컬럼들의 상관계수
iris.cor<-cor(iris[-5])
class(iris.cor)
iris.cor


# 4개 컬럼들의 상관계수 검정--------------------------------
# >> 추가 패키지 설치 psych
#install.packages("psych")

library(psych)

corr.test(iris[-5])

iris.cor <- cor(iris[, -5])

class(iris.cor)

str(iris.cor)

iris.cor["Petal.Width", "Petal.Length"]

#install.packages("gmm")
#install.packages("corrgram")
library(corrgram)
corrgram(iris[-5],upper.panel = panel.conf)

#상관계수 및 분석 관련 그래프: 
#psych 패키지의 paris.panels() 함수 이용
pairs.panels(state.x77,
main="Correlation Plot of US States Data",
bg="red", 
pch=21, 
hist.col="gold")


#psych 패키지의 paris.panels() 함수 이용
library(corrgram) 
corrgram(state.x77,
main="Corrgram of US States Data", 
order=TRUE, 
lower.panel=panel.shade, 
upper.panel=panel.pie, 
text.panel=panel.txt)

#상관계수 및 분석 관련 그래프: 
#psych 패키지의 paris.panels() 함수 이용
library(corrgram)
cols <- colorRampPalette(c("darkgoldenrod4", 
"burlywood1", 
"darkkhaki", 
"darkgreen")) 
corrgram(state.x77,
main="Corrgram of US States Data", 
order=FALSE, 
col.regions=cols,
lower.panel=panel.pie, 
upper.panel=panel.conf, 
text.panel=panel.txt)




























