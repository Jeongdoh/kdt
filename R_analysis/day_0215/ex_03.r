# 이상치(outlier)데이터 체크----------------------------------
# : 정상범위를 벗어난 데이터를 의미
# 내장데이터 cars 활용
# 컬럼 : speed, dist
# (1)데이터 구조 및 구성 확인
str(cars)

# (2) 거리 데이터만 선택
distData<-cars$dist
distData

# (3) 거리 데이터에 대한 통계값 확인
mean(distData)
median(distData)
min(distData)
max(distData)

hist(distData, breaks=seq(0,120,by=10))

# (4) 이상치 체크 >> 사분위수
Q<-quantile(distData, probs = seq(0, 1, 0.25), na.rm = FALSE)
Q


# IQR 정상데이터 구간 값
iqr<-IQR(distData)
iqr

# 하위 이상치 & 하위 이상치 계산
lout<-Q[2]-(1.5*iqr)
lout

uout<-Q[4]+(1.5*iqr)
uout


boxplot(distData)


# 이상치를 제외한 데이터 선택
distData>lout
distData<uout

sum(distData<lout)
sum(distData>uout)











