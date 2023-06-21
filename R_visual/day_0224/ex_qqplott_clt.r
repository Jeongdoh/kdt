# ------------------------------------------------------------------------
# 모집단 데이터 - 
# ------------------------------------------------------------------------
population=c(1:10,40:50,90:100)
qqnorm(population)
qqline(population)


# ------------------------------------------------------------------------
# 표본 3000개, 표본 원소 1 ~ 1000개
# ------------------------------------------------------------------------
par(mfrow = c(3, 2))

Sample_Mean=numeric()

# 표본 크기 1개, 3000개 생성 및 평균값 저장 =================================
for(i in 1:3000) 
    Sample_Mean[i]=mean(sample(population,1,replace=TRUE))

# 시각화
hist(Sample_Mean,freq=FALSE,main="n=1",xlab="Sample_Mean (n=1)")
lines(density(Sample_Mean))


# 표본 크기 5개, 3000개 생성 및 평균값 저장 =================================
Sample_Mean=numeric()

for(i in 1:3000) Sample_Mean[i]=mean(sample(population,5,replace=TRUE))

hist(Sample_Mean,freq=FALSE,main="n=5",xlab="Sample_Mean (n=10)")

lines(density(Sample_Mean))


# 표본 크기 10개, 3000개 생성 및 평균값 저장 =================================
Sample_Mean=numeric()

for(i in 1:3000) Sample_Mean[i]=mean(sample(population,30,replace=TRUE))

hist(Sample_Mean,freq=FALSE,main="n=30",xlab="Sample_Mean (n=30)")

lines(density(Sample_Mean))


# 표본 크기 100개, 3000개 생성 및 평균값 저장 =================================
Sample_Mean=numeric()

for(i in 1:3000) Sample_Mean[i]=mean(sample(population,100,replace=TRUE))

hist(Sample_Mean,freq=FALSE,main="n=100",xlab="Sample_Mean (n=100)")

lines(density(Sample_Mean))


# 표본 크기 500개, 3000개 생성 및 평균값 저장 =================================
Sample_Mean=numeric()

for(i in 1:3000) Sample_Mean[i]=mean(sample(population,500,replace=TRUE))

hist(Sample_Mean,freq=FALSE,main="n=500",xlab="Sample_Mean (n=500)")

lines(density(Sample_Mean))


# 표본 크기 1000개, 3000개 생성 및 평균값 저장 =================================
Sample_Mean=numeric()

for(i in 1:3000) Sample_Mean[i]=mean(sample(population,1000,replace=TRUE))

hist(Sample_Mean,freq=FALSE,main="n=1000",xlab="Sample_Mean (n=1000)")

lines(density(Sample_Mean))