# 대수의 법칙----------------------------------------------
?rbinom

x<-rbinom(10,1,0.5)
sum(x)/10
mean(x)


x<-rbinom(100,1,0.5)
sum(x)/100
mean(x)


x<-rbinom(1000,1,0.5)
sum(x)/1000
mean(x)


x<-rbinom(10000,1,0.5)
sum(x)/10000
mean(x)

#sample() : 몬테크롤러
#비복원추출
sample(1:10,3)
#sample(1:2,10)  비복원추출 에러뜸
# 그래서 하는게 아래방법
#--->복원추출
nums<-sample(1:2,10, replace = T)
nums

# 확률지정
nums<-sample(1:2,10, replace = T,prob=c(0.8,0.2))
nums


# 난수생성 함수
runif(1)
runif(10, min=1, max=10)


# 확률 변수의 기댓값
x<-c(0,1,2)
px<-c(1/4,2/4,1/4)


#
dbinom(7,10,prob=0.5)

#균일분포
hist(runif(100,0,100), col='orange')
hist(runif(1000,0,100), col='salmon')
hist(runif(10000,0,100), col='tomato')

# 이항분포
#x가 이항분포 B(10,0.2)일 경우, P[X=2]의 확률값은 dbnom(2,10,0.2)

a<-seq(0,50,by=1)

b<-dbinom(a,50,0.2)

plot(a,b)

b<-dbinom(a,20,0.6)
plot(a,b)


# 이항분포의 누적확률값
#pbinom()함수 : 이항분포의 누적확률값

pbinom(3,10,0.2)

dbinom(0,10,0.2)


# 정규분포 : normal distribution---------------------------------
set.seed(2022)
x<-rnorm(n=1000, mean=172,sd=7)
hist(x,col='blue',breaks=7)


# 중심에 데이터가 집중되어있고 좌우는 작은 데이터가 아주 작은
# 종 형태의 분포
# => 규격화 => 표준정규분포 : 평균 0, 표준편차 1
# 키 평균 : 172, 표준편차 : 10
n=1000
data<-rnorm(n,mean=172, sd=10)
data

mean(data)
sd(data)
