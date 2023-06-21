#기술적 통계--(2) 숫자 방식 특징 요약-------------------------
#외부데이터 로딩---------------------------------------------
file_name="day_0215/data/cafedata.csv"
cafe_data<-read.csv(file_name)
str(cafe_data)


# 특정 행 선택 및 출력--------------------------------------
cafe_data[1] # 인덱스에 해당하는 columns
cafe_data[1,] # 인덱스에 해당하는 row
cafe_data[34,] # 34번 행의 인덱스 선택


#결측치 체크 및 처리----------------------------------------
#is.na()=T,F
#sum(is.na())=T,F
sum(is.na(cafe_data))
sum(is.na(cafe_data$Coffees))




# 행단위 NA검사 >> 행의 모든 요소가 NA가 아니면 TRUE
#complete.cases(cafe_data)
is.na(cafe_data)
complete.cases(cafe_data)



#결측치 삭제------------------------------------------------
#na.omit()
na.omit(cafe_data)
is.na(cafe_data)



## 최빈값---------------------------------------------------
# x = c(1, 1, 2, 3, 3, 3, 3, 4) 		
# y <- table(x)					# 값별 개수 즉 빈도표
# names(y)[ which(y==max(y)) ]
# 함수 제공안됨!
#Coffee 컬럼에 대한 최반값
# (1) 값에 갯수 즉, 빈도 >>(2) 빈도표에서 최대값
coffee<-table(cafe_data$Coffees)
coffee
max(coffee)

#names(coffee)[ which(coffee==max(coffee)) ]



# 줄기-잎 그래프-------------------------------------------
# 숫자로 그래프 표현
data<-c(1,1,2,2,3,3,3,3,4)
stem(data)

data<-c(11,11,22,22,23,31,32,33,34,40)
stem(data)


# 표준편차-------------------------------------------------
# 데이터의 분포 확인
height <- c(164, 166, 168, 170, 172, 174, 176)
height

# (1)평균 >> mean()
height.m=mean(height)
height.m


# (2)편차 >> 값 - 평균 =
height-height.m


# (3) 분산 >> 전체 데이터의 평균과의 거리(차)
sum(height-height.m)  # +,- 부호들 때문에 상쇄됨
(height-height.m)^2   # 제곱근으로 처리

mean((height-height.m)^2) # 분산 

# 루트 >> sqrt()
sqrt(mean((height-height.m)^2)) # 표준편차



# R함수 사용---------------------------------------------
# 표본에 대한 분산과 표준편차 계산 진행
var(height); sd(height);




