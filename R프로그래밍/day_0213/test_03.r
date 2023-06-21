# 데이터 불러오기
data<-read.csv('C:/Users/y2kjd/Desktop/company.csv', header=TRUE,fileEncoding = "cp949")

data

# 머신러닝 맛보기

iris

#열 확인하기
colnames(iris)

#회귀모형
lm(Sepal.Length ~ Petal.Width, data=iris)

z=lm(iris[,1]~iris[,4])
summary(z)

plot(iris[,1]~iris[,4])
abline(z)

zz=lm(iris[,1]~iris[,2]+iris[,3]+iris[,4])
zz

summary(zz)

# 기본 데이터 탐색
str(iris)

#앞서 6개 데이터
head(data)

#차원분석
dim(data)


###분류 알고리즘 : 로지스틱 회귀분석, 의사결정나무, 랜덤포레스트, 인공신경망
install.packages('ROCR') # roc커브를 그리기 위한 패키지
install.packages('e1071')#범주형 로지스틱회귀
install.packages('MASS') #범주형 로지스틱회귀
install.packages('pscl') #
install.packages('caret')#데이터전처리용
install.packages('kernlab')
install.packages('nnet')#인공신경망
install.packages('car') #데이터 전처리
install.packages('SparseM')
install.packages('glmnet') # lasso 변수선택방법
install.packages('elasticnet')
install.packages("corrplot") #다중공선성을 알아보기 위해 상관플롯을 그르기위한 패키지


###머신러닝 맛보기
library("corrplot")
library('elasticnet')
library('glmnet')
library('SparseM')
library('car')#
library('pscl')#
library('e1071')# 범주형 로지스틱회귀
library('MASS')# 범주형 로지스틱회귀
library('caret')#
library('kernlab')
library('nnet')# 인공신경망
library('ROCR')#


#데이터 불러오기
data<-read.csv('C:/Users/y2kjd/Desktop/company.csv',header=TRUE,fileEncoding = "cp949")

#데이터 구조 보기
str(data)

#앞서 6개 데이터
head(data)

#아래 데이터 확인
tail(data)

#차원 살펴보기
dim(data)

#변수별 결측치 수 살펴보기
colSums(is.na(data))#결측치를 중앙값으로 대처하기
for (i in 1:dim(data)[2]){ data[is.na(data[,i]),i]=median(data[,i],na.rm=T)}##이런식으로 결측치를 대처 가능

colnames(data)

#종속변수 전처리#1~10사이값을 가지며 1로갈수록 높은것임
data$KIS.신용평점.0A3010<-ifelse(data$KIS.신용평점.0A3010<=5,0,1)
data$KIS.신용평점.0A3010<-as.factor(data$KIS.신용평점.0A3010)
data$KIS.신용평점.0A3010

#데이터 분할
set.seed(123)
intrain<-createDataPartition(y=data$KIS.신용평점.0A3010,p=0.7,list=FALSE)
intrain

training<-data[intrain,]## 트레이닝데이터
training

testing<-data[-intrain,]## 테스트 데이터 나눔
testing


###로지스틱 회귀분석
colnames(data)
m2<-train(KIS.신용평점.0A3010 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 
+ 단기차입금.총자본,data=training,method='glm')
summary(m2)

#예측
predictions2<-predict(m2,newdata=testing)
predictions2

conictions2=confusionMatrix(predictions2,testing$KIS.신용평점.0A3010)
conictions2


###의사결정나무
install.packages('rpart')
library('rpart')
head(training)
m<-rpart(KIS.신용평점.0A3010 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 +
 단기차입금.총자본,data=training)
plot(m,compress=TRUE,margin=0.1)
text(m,cex=0.8)
#뭔가 보기 불편함

install.packages('rpart.plot')
library('rpart.plot')
prp(m, type=4, digits=3) # type extra digits 숫자 바꿔보면 더 예쁘게 꾸며짐.


#예측
pre_rpart<-predict(m,newdata=testing)
head(pre_rpart)
head(testing)

pre_rpart<-round(pre_rpart[,2]) # p값을 0.5로 두자.
pre_rpart

pre_rpart<-as.vector(pre_rpart)
pre_rpart

pre_rpart<-as.factor(pre_rpart)
pre_rpart

test_rpart<-testing$KIS.신용평점.0A3010
test_rpart

test_rpart<-as.factor(test_rpart)
test_rpart

confusionMatrix(pre_rpart,test_rpart)


###랜덤포레스트
install.packages('randomForest')
library('randomForest')
head(training)
m2<-randomForest(KIS.신용평점.0A3010 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 +
단기차입금.총자본,data=training)
m2

#변수중요도
importance(m2)
#그래프 그리기
varImpPlot(m2)

#
pred=as.factor(as.vector(predict(m2,testing)))
pred

##인공신경망
m<-nnet(KIS.신용평점.0A3010 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 + 단기차입금.총자본,size=5, #은닉층 노드
갯수linout=FALSE, # TRUE이면 활성함수가 선형출력(liner output) FALSE면 로지스틱함수가 적용MaxNWts=1000, # 가중치의 최대개수로 기본값은 1000, 모델이 복잡하다면 가중치의 수를 증가시켜야함.
data=training)
#나머지 옵션도 있음. 찾아볼 것.
pre_nnet<-predict(m,newdata=testing)
head(pre_nnet)
pre_nnet<-as.factor(round(pre_nnet))
pre_nnet
#예측
confusionMatrix(pre_nnet,testing$KIS.신용평점.0A3010)


# 기초시각화
# [ plot 함수 구문 ]
# plot(y축 데이터, 옵션)
# plot(x축 데이터, y축 데이터,옵션)

# [ type 인수의값]
# main = “메인 제목” 제목설정
# sub = “서브 제목” 서브제목설정
# xlab=“문자”, ylab=“문자” x, y 축에 사용할 문자열을 지정

# [ 그래프 타입 선택]
# type=“p” 점
# type=“l” 선
# Type=“b” 점과선
# Type=“c” “b”에서 점을 생략한 모습
# Type=“o” 겹친 점과선
# Type=“h” 수직선
# Type=“s” 수평선 우선의 계단모양
# Type=“S” 수직선 우선의 계단모양
# Type=“n” 그래프를 그리지 않음

# [ 선의 모양 선택 ] 
# lty=0, lty=“black” 투명선
# lty=1, lty=“solid” 실선
# lty=2, lty=“dashed” 대쉬선
# lty=3, lty=“dotted” 점선
# lty=4, lty=“dotdash” 점선과 대쉬선
# lty=5, lty=“longdash” 긴 대쉬선
# lty=6, lty=“twodash” 2개의 대쉬선
# [색, 기호 등]
# col=1, col=“blue” 기호의 색 지정
# 1:검정, 2:빨강, 3:초록, 4:파랑, 5:연파랑, 6: 보라, 7: 노랑, 8:회색
# pch=0, pch=“문자” 점의 모양 지정
# bg=“blue” 그래프의 배경색 지정
# lwd=“숫자” 선을 그릴 때 선의 굵기 지정
# cex=“숫자” 점이나 문자를 그릴 때 점이나 문자의 굵기를 지정


var1<-c(1,2,3,4,5)
plot(var1)


var2<-c(3,3,3)
plot(var2)


x<-1:5 
y<-5:1 
plot(x,y)


x<-1:3
y<-3:1
plot(x, y, xlab="x축 값", ylab="y축 값", main="Plot Test")


#Plot 함수로 여러 개의 차트 그리기
x1 <- 1:5 
y1 <- x1^2 
z1 <-5:1
(mat1<-cbind(x1,y1,z1)) # 행렬 생성

#Plot 함수로 여러 개의 차트 그리기
par(mfrow=c(2,3)) # 2행 3열
plot(y1, main="index")
plot(x=x1, y=y1, main="x^2")
plot(mat1, main="matrix")
plot(x1, y1, type="l", main="line")
plot(x1, y1, type="h", main="high density")
plot(x1, y1, type="s", main="steps")
par(mfrow=c(1,1)) 




# 실습
KIS <- read.csv("C:/Users/y2kjd/Desktop/KIS.csv")
plot(KIS$Trust, KIS$DeR, type="l", main="KIS Chart", xlab="신뢰도", ylab="부채비율")

#points()는 점을 찍는 함수
# [points() 함수 구문]
# points(x, y, type=“p”,....)


x=rep(1:5, rep(5,5))

y=rep(1:5, 5)

pchs=c("!", "@", "#", "$", "%") 
plot(1:5, type='n', xlim=c(0,7.5), ylim=c(0.5,5.5), main="points by ‘pch’ ")
points(x, y, pch=1:25, cex=2.5)
text(x-0.4, y, labels=as.character(1:25), cex=1.5)


# 실습문제
plot(iris$Sepal.Width, iris$Sepal.Length, cex=1, pch=20, xlab="width", ylab="length", main="iris") 
points(iris$Petal.Width, iris$Petal.Length, cex=1, pch="+", col="blue") 
points(iris$Sepal.Width, iris$Sepal.Length, cex=1, pch=15, col="pink")


# #선을 그리는 함수: abline(), lines(), arrows()
# [abline() 함수 구문] 
# abline(x축 데이터, y축 데이터, h인수, v인수, reg인수, coef인수)

cars[1:4,]
z <- lm(dist ~ speed, data = cars)
is(z)
z$coef
plot(cars,main = "abline")

abline(h = 20)

abline(h = 30)

abline(v = 20, col="blue")


abline(a = 40, b = 4, col="red") # y = a + bx

abline(z, lty = 2, lwd = 2, col="green")


#선을 그리는 함수
cars[1:10,] 
z=lm(dist~speed, data=cars) 
is(z)
plot(cars, main="abline") 
abline(h=30) ## h인수
abline(h=50) ## h인수
abline(v=10, col="purple") ## v인수
abline(a=5, b=5, col="red") ## a,b인수
abline(z, lty=2, lwd=2, col="blue") ## reg인수
abline(z$coef, lty=3, lwd=2, col="orange") ## coef인수


#선을 그리는 함수
# [lines() 함수 구문] 
# lines(x축 데이터, y축 데이터, lty인수)

#lines() 함수는 좌표의 점들을 이어서 선을 그리는 함수
lty1 = c('blank', 'solid', 'dashed', 'dotted', 'dotdash', 'longdash', 'twodash')
lty2 = c('33', '24', 'F2', '2F', '3313', 'F252', 'FF29') 
plot(0:6, 0:6, type='n', ylim=c(0,20), xlab='', ylab='', main='lines')
lines(c(1,3), c(20,20), lty=1)
lines(c(1,3), c(19,19), lty=2)
lines(c(1,3), c(18,18), lty=3)
lines(c(1,3), c(17,17), lty=4)
lines(c(1,3), c(16,16), lty=5)
lines(c(1,3), c(15,15), lty=6)
lines(c(1,3), c(14,14), lty=lty1[1])
lines(c(1,3), c(13,13), lty=lty1[2])
lines(c(1,3), c(12,12), lty=lty1[3])
lines(c(1,3), c(11,11), lty=lty1[4])
lines(c(1,3), c(10,10), lty=lty1[5])

lines(c(1,3), c(9,9), lty=lty1[6]) 
lines(c(1,3), c(8,8), lty=lty1[7])
lines(c(1,3), c(7,7), lty=lty2[1])
lines(c(1,3), c(6,6), lty=lty2[2])
lines(c(1,3), c(5,5), lty=lty2[3])
lines(c(1,3), c(4,4), lty=lty2[4])
lines(c(1,3), c(3,3), lty=lty2[5])
lines(c(1,3), c(2,2), lty=lty2[6])
lines(c(1,3), c(1,1), lty=lty2[7])
legend(3.5, 20, legend=1:6, lty=1:6)
legend(3.5, 13, legend=c(lty1,lty2), lty=c(lty1,lty2))

#화살표를 그리는 함수
# [arrows() 함수 구문]
# arrows( x, #시작점 x축값y, #시작점 y축값
# x1, #끝점 x축값
# y1, #끝점 y축값
# length 인수, angle 인수, code 인수...)

#화살표 그리는 함수
plot(1:9, type='n', axes=F, xlab='', ylab='', main='arrows')
arrows(1, 9, 4, 9, angle=30, length=0.25, code=2)
arrows(1, 8, 4, 8, length=0.5)
arrows(1, 7, 4, 7, length=0.1)
arrows(1, 6, 4, 6, angle=60)
arrows(1, 5, 4, 5, angle=90)
arrows(1, 4, 4, 4, angle=120)
arrows(1, 3, 4, 3, code=0)
arrows(1, 2, 4, 2, code=1)
arrows(1, 1, 4, 1, code=3)

text(4.5, 9, adj=0, 'angle=30, length=0.25, code=2 (default)')
text(4.5, 8, adj=0, 'length=0.5')
text(4.5, 7, adj=0, 'length=0.1')
text(4.5, 6, adj=0, 'angle=60')
text(4.5, 5, adj=0, 'angle=90')
text(4.5, 4, adj=0, 'angle=120')
text(4.5, 3, adj=0, 'code=0')
text(4.5, 2, adj=0, 'code=1')
text(4.5, 1, adj=0, 'code=3')


#rect() 함수는 사각형 도형
# [rect() 함수 구문] 
# rect(xleft 인수, ybottom 인수, xright 인수, ytop 인수, density 인수, angle 인수, col 인수, border 인수, lty 인수, lwd
# 인수...)

#rect() 함수는 사각형 도형
op <- par(no.readonly = TRUE) 
par(mar = c(0, 2, 2, 2))
plot(1:10, type = "n", main = "rect", xlab = "", ylab = "", axes = F)
rect(xleft = 1, ybottom = 7, xright = 3, ytop = 9)
text(2, 9.5, adj = 0.5, "defalut")
rect(1, 4, 3, 6, col = "gold")
text(2, 6.5, adj = 0.5, "col = \"gold\"")
rect(1, 1, 3, 3, border = "gold")
text(2, 3.5, adj = 0.5, "border = \"gold\"")
rect(4, 7, 6, 9, density = 10)
text(5, 9.5, adj = 0.5, "density = 10")
rect(4, 4, 6, 6, density = 10, angle = 315)
text(5, 6.5, adj = 0.5, "density=10, angle=315")

rect(4, 1, 6, 3, density = 25)
text(5, 3.5, adj = 0.5, "density = 25")
rect(7, 7, 9, 9, lwd = 2)
text(8, 9.5, adj = 0.5, "lwd = 2")
rect(7, 4, 9, 6, lty = 2)
text(8, 6.5, adj = 0.5, "lty = 2")
rect(7, 1, 9, 3, lty = 2, density = 10)
text(8, 3.5, adj = 0.5, "lty=2, density=10")
par(op) 


# [polygon() 함수 구문]
# polygon() 함수는 다각형을 그리는 함수
# polygon(x좌표, y좌표, density 인수, angle 인수, border 인수, col 인수, lty 인수...)

op <- par(no.readonly = TRUE)
par(mar = c(0, 2, 2, 2))
theta <- seq(-pi, pi, length = 12)
x <- cos(theta)
y <- sin(theta)
plot(1:6, type = "n", main = "PLOYGON", xlab = "", ylab = "", axes = F)
x1 <- x + 2 
y1 <- y + 4.5


polygon(x1, y1)
x2 <- x + 2
y2 <- y + 2
polygon(x2, y2, col = "red", border="blue")
x3 <- x + 5
y3 <- y + 4.5
polygon(x3, y3, density = 10, angle=135)
x4 <- x + 5
y4 <- y + 2
polygon(x4, y4, lty = 2, lwd = 2)
text(2, 5.7, adj = 0.5, "defalut")
text(5, 5.7, adj = 0.5, "density = 10")
text(5, 3.2, adj = 0.5, "lty = 2, lwd = 2")
par(op)


# ploygon 함수로 원 그리기
# 원을 그리는 함수 존재하지 않는다
# 원의 방정식 : x^2 + y^2 = r^2
# x=cos(theta), y=sin(theta) 이용

theta <- seq(-pi, pi, length=361)# length : 361로 나눈다 (갯수 증가 : 촘촘함 증가)
x <- cos(theta); y <- sin(theta)# x축 및 y축 데이터 할당

# # plot 생성
plot(x,y,type="n")# 그림 2# 원 그리기
polygon(x,y)# 중심 : (0,0) / 반지름 : 1


#원 중심 이동 + 반지름 길이 조정

plot(x,y,type="n")# 그림 2# 원 그리기
x <- 0.5 + 0.1*cos(theta)
y <- -0.5 + 0.1*sin(theta)
#중심이동 # 반지름 조절
polygon(x,y,col="red", border="white")
# 원 중심 찍기
points(0.5,-0.5,pch=20)


#양궁 표적지 그리기
plot(x,y,type="n")# 그림 2# 원 그리기
x <- 0.5 + 0.1*cos(theta)
y <- -0.5 + 0.1*sin(theta)
#중심이동 # 반지름 조절
polygon(x,y,col="red", border="white")
# 원 중심 찍기
points(0.5,-0.5,pch=20)


#x축이 1에서 8, y축이 –4에서 4까지인 플롯 위에 아래와 같은 그래프를 그리시오

plot(c(1, 8), c(-4, 4), type = "n")
x <- c(1, 2, 3, NA, 4, 4, 6, 6)
y <- c(1, -4, 3, NA, -3, 3, 3, -3)
polygon(x, y, col = c("pink", "blue"), border = c("red", "orange"), lwd = 2,
lty = c("dotted", "solid")) 
lines(c(1,8), c(-2,-2), lty=4, col="green") 
arrows(1, 2, 8, 2, length=0.5) 
title("Polygons")





### 제출 과제 ###

# 기초시각화
# [ plot 함수 구문 ]
# plot(y축 데이터, 옵션)
# plot(x축 데이터, y축 데이터,옵션)

# [ type 인수의값]
# main = “메인 제목” 제목설정
# sub = “서브 제목” 서브제목설정
# xlab=“문자”, ylab=“문자” x, y 축에 사용할 문자열을 지정


# polygon(x좌표, y좌표, density 인수, angle 인수, border 인수, col 인수, lty 인수...)


# [rect() 함수 구문] 
# rect(xleft 인수, ybottom 인수, xright 인수, ytop 인수, density 인수, angle 인수, col 인수, border 인수, lty 인수, lwd
# 인수...)


plot(c(0,200),c(0,200))

polygon(c(65,100,140),c(0,30,0),col = "#d49e44")
polygon(c(65,100,10),c(0,30,0),col = "#a78648")



polygon(c(30,70,110),c(0,43,0),col='#eaae4c')
polygon(c(30,70,10),c(0,43,0),col = "#c59340")



polygon(c(10,35,70),c(0,35,0),col = "#febe5b")
polygon(c(0,35,10),c(0,35,0),col = "#d59f3a")








