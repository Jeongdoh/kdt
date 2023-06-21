#내장 데이터airquality 활용---------------------------------------------------------------------

#내장데이터 확인
str(airquality)

#컬럼명 확인 >> colnames()
colnames(airquality)

#갯수 >> dim()
dim(airquality)

#결측치 체크 >> 단위 : 행 >> complete.cases()----------------------------------------------------
sel<-complete.cases(airquality)
sel

#결측치 없는 행만 추출 >> 데이터[인덱싱]
airquality[1,]      # 1번 행만 선택
airquality[sel,]    # 결측치 없는 행만 선택

# 결측치가 존재하는 행만 추출 >> 
airquality[!sel,]    # 결측치 있는 행만 선택 >> T > F, F > T

# 결측치 행 삭제 >> na.omit()
airquality<-na.omit(airquality)

# 특정 컬럼에 대한 통계량 ( 평균, 분산, 표준편차, 최빈값)-------------------
ozone<-airquality$Ozone
ozone

# 평균 >> mean()
mean(ozone)
# 분산 >> var()
var(ozone)
# 표준편차 >> sd()
sd(ozone)
# 최빈값 >> 빈도표 + 최대값
freq<-table(ozone)
freq

sort(freq)
max(freq)
which.max(freq)





# 내가 한것
airquality
sum(is.na(airquality))

sum(is.na(airquality$Ozone))
sum(is.na(airquality$Solar.R))

na.omit(airquality$Ozone)
na.omit(airquality$Solar.R)

c(airquality[,3])
#평균
airquality.m<-mean(airquality[,3])
airquality.m

#편차
airquality[,3]-airquality.m

#분산
sum(airquality[,3]-airquality.m)
(airquality[,3]-airquality.m)^2

#루트
sqrt(mean((airquality[,3]-airquality.m)^2))


#----------------------------------------------------------------
c(airquality[,4])
#평균
airquality.m<-mean(airquality[,4])
airquality.m

#편차
airquality[,4]-airquality.m

#분산
sum(airquality[,4]-airquality.m)
(airquality[,4]-airquality.m)^2

#루트
sqrt(mean((airquality[,4]-airquality.m)^2))


#----------------------------------------------------------------
c(airquality[,5])
#평균
airquality.m<-mean(airquality[,5])
airquality.m

#편차
airquality[,5]-airquality.m

#분산
sum(airquality[,5]-airquality.m)
(airquality[,5]-airquality.m)^2

#루트
sqrt(mean((airquality[,5]-airquality.m)^2))

#----------------------------------------------------------------
c(airquality[,6])
#평균
airquality.m<-mean(airquality[,6])
airquality.m

#편차
airquality[,6]-airquality.m

#분산
sum(airquality[,6]-airquality.m)
(airquality[,6]-airquality.m)^2

#루트
sqrt(mean((airquality[,6]-airquality.m)^2))

