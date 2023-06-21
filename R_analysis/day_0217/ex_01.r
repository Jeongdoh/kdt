# clt실습-------------------------------------------------------------------------
# 정규분포 모집단-----------------------------------------------------------------
# 평균 : 52, 표준편차 : 5
# 데이터 수 : 10000
# 함수 : rnorm()
n<-10000
nData<-rnorm(n,mean=52,sd=5)
hist(nData,main='정규분포 형태의 모집단')



# 표본집단 => 샘플크기 : 10, 30, 50
x.bar<- c()
for (i in 1:10000){
    x.bar <- c(x.bar,mean(sample(nData,size = 30)))
}
hist(x.bar,col ='skyblue', freq=F)


# 균등분포 모집단-----------------------------------------------------------------
# 최소값 : 0 , 최대값 : 1000
# 데이터 수 : 10000
# 함수 : runif()
uData<-runif(n,min=0,max=100)
hist(nData,main='균등분포 형태의 모집단')



# 표본집단 => 샘플크기 : 10, 30, 50
x.bar<- c()
for (i in 1:100){
    x.bar <- c(x.bar,mean(sample(uData,size = 30)))
}
hist(x.bar,col ='skyblue', freq=F)


# 카이 제곱분포--------------------------------------------------------
# 검정에 사용
# 자유도(df) 기준으로 확률분포, (누적확률, 확률밀도,..)계산
#---------------------------------------------------------------------
# x에 대한 확률
df=30; x=43.77
dchisq(x, df)

# x에 대한 누적확률
pchisq(x, df)       # 디폴트값이 <=X
pchisq(x, df, lower.tail = F)   # P[X>x] 

# 퍼센트에 해당하는 확률변수 값
qchisq(0.95,df)

#실습문제
df=1:5

set.seed(2022)
X<-rbinom(n=10000, size = 100, prob = 0.5)
hist(X,col='lightgray',breaks=15,freq=F)

x<-seq(0,100,1)
curve(dnorm(x,mean(X),sd(X)),add=T,col='tomato',lwd=2)



binom.test(x=65,n=100,p=0.5)






















