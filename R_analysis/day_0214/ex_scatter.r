#--------------------------------------------------
#내장데이터 cars활용
#cars 데이터 정보 출력
#50대 자동차의 속도와 제동거리 관계 그래프화
#--------------------------------------------------
#데이터 로딩----------------------------------------
test<-cars
test
#데이터 확인----------------------------------------
# (1) 데이터 요약 정보 & 구조 출력
str(test)

# (2) 행과 열 출력
dim(test)

# (3-1) 행 갯수만 출력
nrow(test)

# (3-2) 열 갯수만 출력
ncol(test)

# (4) 컬럼명 출력
colnames(test)

#데이터 표현 By 산점도 그래프------------------------
x<-test$speed
y<-test$dist
plot(x,y,main='속도 vs 거리',xlab='속도',
ylab='거리')


# 나일강의 1871 ~ 1970 년 유속
Nile
str(Nile)

# (2) 행과 열 출력
river<-Nile

river=data.frame(river)

river$year<-1871:1970
river

dim(river)

# (3-1) 행 갯수만 출력
nrow(river)

# (3-2) 열 갯수만 출력
ncol(river)

# (4) 컬럼명 출력
colnames(river)

#데이터 표현 By 산점도 그래프------------------------
plot(river$year,river$river)

plot()



# 