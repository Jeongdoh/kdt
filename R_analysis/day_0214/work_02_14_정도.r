# 1. R에서 데이터 자료형 분류
#    -> 데이터 자료형의 특징, 저장 데이터 타입
#    -> 자료형 변환 관련 함수들

# 1. 스칼라(Scala)
#구성인자가 하나인 벡터

# 2. 벡터(Vector)
#동일한 유형의 데이터가 1차원으로 구성되어 있는 데이터 구조

# 3. 팩터, 요인(Factor)
#범주형데이터(자료)를 표현하기 위한 데이터 타입

# 4. 행렬(Matrix)
#동일한 유형의 2차원 데이터 구조 (예) : (행(Row), 열(Column))

# 5. 배열(Array)
#배열은 동일한 유형의 다차원 데이터 구조
#> arr1 <- array(1:12, dim = c(2,2,3))
# > arr1

# , , 1 

# [,1] [,2]

# [1,] 1 3

# [2,] 2 4

 
# , , 2 

# [,1] [,2]

# [1,] 5 7

# [2,] 6 8


# , , 3 

# [,1] [,2]

# [1,] 9 11

# [2,] 10 12



# 6. 리스트(List)
#리스트는 서로 다른 구조의 데이터를 모두 묶은 객체

# 7. 데이터프레임(Data.frame)
#데이터 유형에 상관없이 2차원 형태의 데이터 구조




# 2. 메타데이터란?
#    -> 개념

#meta는
#~에 관한 , ~에 대한이라는 뜻으로
#데이터를 구조화한 데이터. 또는 속성정보라고 함

#다량의 정보안에서 일정한 규칙에따라 찾아낸, 효율적으로 쓰기위한 데이터.






# 3. 기술적통계 방식으로 데이터 표현
#    -> 데이터 :  사회일반 > 가족실태조사 > 총괄(제공) > 2020
#    -> 추출 데이터 : 지역, 가족원합계, 세대구성, 가구구성, 교육정도_학력
homedata<-read.csv("day_0214/data/2020_가족실태조사.csv", header = F)
homedata
#데이터 확인------------------------------------------------------
# 구조 및 정보 출력 -> str()
str(homedata)

# 행과 컬럼 갯수 출력 -> dim()
dim(homedata)


# 행 갯수 & 컬럼 갯수 출력 -> 행 갯수 : nrow(), 컬럼 갯수 : ncol()
nrow(homedata); ncol(homedata)

# 컬럼명 출력 -> colnames()
colnames(homedata)


# 컬럼명 지정 -> colnames()=
colnames(homedata)=c("지역","가족원합계","세대구성","가구구성","교육정도_학력")
head(homedata)



#    (3-1) 지역
#    - 지역별 세대구성 비중, 가구구성 비중

region<-factor(homedata$지역,levels=c(11,21:26,29,31:39),labels=c('서울특별시
','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원도','충청북도',
'충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도'))

generation<-factor(homedata$세대구성,levels=c(1:6),labels=c('1세대','2세대','3세대','4세대','1인 가구','비혈연'))

household<-factor(homedata$가구구성,levels=c(1:26),labels=c('미혼여성','미혼남성','기혼여성','기혼남성','여성노인','남성노인',
'부부','부부 + 자녀','모 + 자녀','부 + 자녀','모 + 자녀부부',
'부 + 자녀부부','부모 + 자녀부부','부모 + 자녀부부 + 손자녀','부모 + 모 + 손자녀'
,'부모 + 부 + 손자녀','모 + 자녀부부 + 손자녀','부 + 자녀부부 + 손자녀'
,'모친 + 모 + 손자녀','모친 + 부 + 손자녀','부친 + 부 + 손자녀','부친 + 모 + 손자녀'
,'조부모 + 손자녀','조모 + 손자녀','조부 + 손자녀','기타'))


round(prop.table(table(region, generation),margin=1),3)
round(prop.table(table(region, household),margin=2),3)


plot(region, generation)
plot(region, household)


#    - 가장 많은 세대구성, 가구구성,  가장 적은 세대구성, 가구구성,  평균 세대구성, 가구구성


max(homedata$세대구성)
max(homedata$가구구성)

min(homedata$세대구성)
min(homedata$가구구성)

mean(homedata$세대구성)
mean(homedata$가구구성)


#    (3-2) 가족원합계
#    - 전체에 대한 비중으로 표현
#    - 가장 많은 가족원 수, 가장 적은 가족원 수, 평균 가족원 수 
familly<-table(homedata$가족원합계)
familly
familly<-data.frame(familly)
familly
colnames(familly)<-c('구성','가족원합계')
familly

total<-sum(familly$가족원합계)
total
high<-max(homedata$가족원합계)
high
low<-min(homedata$가족원합계)
low
avg<-mean(homedata$가족원합계)
avg




#    (3-3) 세대구성
#     - 세대구성별 수

gen_df_<-table(homedata$'세대구성')
gen_df<-data.frame(gen_df)
gen_df
colnames(gen_df)<-c('구성','세대구성')
gen_df
barplot(table(homedata$'세대구성'))



#     - 1인가구 수와 나머지 세대구성 수 비교


no1<-table(homedata$'세대구성')[1]
no1

many<-table(homedata$'세대구성')[2:6]
many<-sum(many)
many

pie(cbind(many,no1),labels=c('나머지 세대','1인 세대'))





#    (3-4) 가구구성과 교육정도_학력
#     - 가족구성와 학력의 관계

#데이터 표현 By 산점도 그래프------------------------
plot(homedata$교육정도_학력,homedata$가구구성)





