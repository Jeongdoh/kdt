#1 번 문제

 # 난수생성 함수
# runif(1)
# runif(10, min=1, max=10)

x<-table(round(runif(12,1,6)))
x

y<-table(round(runif(120,1,6)))
y

z<-table(round(runif(12000000,1,6)))
z
rbind(x,y,z)

hist(runif(12,1,6))
hist(runif(120,1,6))
hist(runif(12000000,1,6))



x<-sample(1:6,12,replace = T)
x
y<-sample(1:6,120,replace = T)
y
z<-sample(1:6,12000000,replace = T)
z
12000000
rbind(x,y,z)

hist(sample(1:6,12,replace = T))
hist(sample(1:6,120,replace = T))
barplot(table(sample(1:6,12000000,replace = T)))



#sample() : 몬테크롤러
#비복원추출
# sample(1:10,3)

#sample(1:2,10)  비복원추출 에러뜸
# 그래서 하는게 아래방법
#--->복원추출
# nums<-sample(1:2,10, replace = T)
# nums

# 확률지정
# nums<-sample(1:2,10, replace = T,prob=c(0.8,0.2))
# nums






# 2번

# n_sim <- 10000
# y <- rbinom(n_sim, 100, 0.5)
# hist(y, xlab='X', ylab='mass', main ='B(100, 0.5)', prob = T, breaks = 30)



x <-10000
hist(rbinom(x, 100, 0.5))
hist(rbinom(x, 100, 0.1))
hist(rbinom(x, 100, 0.9))


#3번

# 정규분포 : normal distribution---------------------------------
# set.seed(2022)
# x<-rnorm(n=1000, mean=172,sd=7)
# hist(x,col='blue',breaks=7)

# pbinom()함수 : 이항분포의 누적확률값

# 중심에 데이터가 집중되어있고 좌우는 작은 데이터가 아주 작은
# 종 형태의 분포
# => 규격화 => 표준정규분포 : 평균 0, 표준편차 1
# 키 평균 : 172, 표준편차 : 10
# n=1000
# data<-rnorm(n,mean=172, sd=10)
# data

answer<-pnorm(35000, 30000, 10000) - pnorm(25000, 30000, 10000)
answer

