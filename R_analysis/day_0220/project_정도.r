# 1970년부터 2015년까지 기대수명 대 의료비 지출
# 보건 금융은 연간 1인당 보건 지출로 보고되며 국가 간 인플레이션과 물가 수준 차이에 따라 조정됩니다


# 파일 불러와서 health_df변수에 저장
health_df<-read.csv("day_0220/healthexp.txt")

#라이브러리 사용
library(dplyr)
library(ggplot2)


# 데이터 확인
str(health_df)
health_df

# 컬럼확인
colnames(health_df)
#[1] "Year"            "Country"         "Spending_USD"    "Life_Expectancy"

# 나라
# Canada
# Germany
# France
# Great Britain
# Japan
# USA

#1970년부터 2015년까지



# 결측치 확인
is.na(health_df)
sum(is.na(health_df))

# 데이터 전처리 할 것 없음





# 탐색적데이터 분석 수행 및 시각화

# Spending_USD(의료비 지출) 평균값과 가장 많은 수치 확인해보기
mean(health_df$Spending_USD)
health_df[which.max(health_df$Spending_USD),'Spending_USD']

# Life_Expectancy(기대수명) 평균값과 가장 많은 수치 확인해보기
mean(health_df$Life_Expectancy)
health_df[which.max(health_df$Life_Expectancy),'Life_Expectancy']






# 최대비용 지출한 나라 찾기
max_spending<-health_df[which.max(health_df$Spending_USD),"Country"]
# health_df 데이터셋에서 Spending_USD 변수에서 최대값을 가지는 행을 찾고, 해당 행의 Country 변수 값을 출력.

# which.max() 함수는 최대값을 가지는 원소의 인덱스를 반환.
# 따라서 which.max(health_df$Spending_USD)는 Spending_USD 변수에서 최대값을 가지는 행의 인덱스를 반환. 
# health_df[which.max(health_df$Spending_USD), "Country"]는 해당 행의 Country 변수 값을 반환. 


# 결과 출력
cat("가장 많은 지출을 한 나라", max_spending, "\n")
# cat() 함수는 출력할 문자열을 연결하여 출력하는 함수. print와 비슷함.




# 최저비용 지출한 나라 찾기
min_spending<-health_df[which.min(health_df$Spending_USD),"Country"]

# 결과 출력
cat("가장 적게 지출을 한 나라", min_spending, "\n")



# Spending_USD 에서 가장 평균값이 높은 나라 구하기
#library(dplyr) 사용


health_df %>%
  group_by(Country) %>%
  summarise(mean_spending = mean(Spending_USD, na.rm = TRUE)) %>%
  arrange(desc(mean_spending)) %>%
  head(3)

# dplyr 패키지의 group_by() 함수를 사용하여 국가별로 그룹화한 후,
# summarise() 함수를 사용하여 각 그룹의 Spending_USD의 평균값을 계산.
# 그리고 arrange() 함수를 사용하여 평균값이 큰 순으로 정렬하고,
# head() 함수를 사용하여 보고싶은 상위 n개 나라의 정보만을 출력.




#기술적 분석기법 적용

# ggplot2 패키지 사용

# Spending_USD, Life_Expectancy 관계그래프 그리기
ggplot(data = health_df, aes(x = Spending_USD, y = Life_Expectancy)) + geom_point()




# 각 국의 기대수명 그래프 그리기
#ggplot 사용

ggplot(health_df, aes(x=Year, y=Life_Expectancy, color=Country)) + 
  geom_line() + 
  labs(title="Life Expectancy vs. Year by Country", x="Year", y="Life Expectancy", color="Country")

# aes(): ggplot() 함수 내에서 aesthetic mappings을 설정. x=Year, y=Life_Expectancy, color=Country는 
# 각각 x축, y축, 색상 aesthetic mapping을 설정.

# geom_line()은 선 그래프를 그리기 위한 함수. 선 그래프는 x와 y 값을 연결하여 그래프를 그리는 방식.

# labs() 함수는 그래프의 제목, x축 레이블, y축 레이블, 색상 범례 레이블을 지정.

# title: 그래프의 제목을 지정.
# x: x축 레이블을 지정.
# y: y축 레이블을 지정.
# color: 색상 범례 레이블을 지정.




# 각 나라별 그래프
#library ggplot2 사용

# 그래프 그리기
ggplot(health_df, aes(x = Year, y = Life_Expectancy)) +
  geom_line() +
  facet_wrap(~Country, ncol = 3) +
  labs(title = "Life Expectancy vs. Year by Country", x = "Year", y = "Life Expectancy")


# aes(): ggplot() 함수 내에서 aesthetic mappings을 설정해줌. x=Year, y=Life_Expectancy, color=Country는 
# 각각 x축, y축, 색상 aesthetic mapping을 설정.

# geom_line()은 선 그래프를 그리기 위한 함수. 선 그래프는 x와 y 값을 연결하여 그래프를 그리는 방식.

# labs() 함수는 그래프의 제목, x축 레이블, y축 레이블, 색상 범례 레이블을 지정.

# title: 그래프의 제목을 지정.
# x: x축 레이블을 지정.
# y: y축 레이블을 지정.
# color: 색상 범례 레이블을 지정.





#-------------------------------------------------------------------------------------------------------------------------------------------

#통계적 분석기법 적용

#-------------------------------------------------------------------------------------------------------------------------------------------
#가설 설정1(의료비를 지출할수록 기대수명은 높아진다.)

# Spending_USD와 Life_Expectancy의 상관계수 구하기

# Pearson 상관계수 계산
result <- cor.test(health_df$Spending_USD, health_df$Life_Expectancy, method = "pearson")

# 결과 출력
cat("Pearson 상관계수:", result$estimate, "\n")
cat("p-value:", result$p.value, "\n")

#상관분석
cor(health_df$Spending_USD,health_df$Life_Expectancy)

# 결과 분석

#상관계수가 0.7 이상이면 강한 양의 상관관계, -0.7 이하이면 강한 음의 상관관계
#p-value가 0.05보다 작다면 두 변수 사이의 상관관계가 유의미


#상관계수: 0.5794305의 수치결과 양의 상관관계가 있다고 보여지며,
#p-value: 5.704081e-26를 보았을때 0.05보다 작기때문에 상관관계가 있다고 보여짐





#가설 설정 및 검정 진행

# 가설 설정2 (의료비 지출이 가장 높은 나라는 미국일 것이다.(세계경제를 주도하기 때문))
ggplot(health_df, aes(x=Spending_USD, y=Life_Expectancy, color=Country)) + geom_point()
# geom_point 함수를 사용하여 Spending_USD 변수를 x축에,
# Life_Expectancy 변수를 y축에 배치한 산점도를 그리며,
# color 매개변수를 사용하여 국가별로 다른 색상으로 표시함.


# 최대비용 지출한 나라 찾기
max_spending<-health_df[which.max(health_df$Spending_USD),"Country"]

# 결과 출력
cat("가장 많은 지출을 한 나라", max_spending, "\n")







# 의료비 지출은 미국이 가장 많다.



#-------------------------------------------------------------------------------------------------------------------------------------------


# 가설 설정3 (의료비 지출이 높은 국가는 평균 수명이 높을 것이다.)



# 미국 지출 그래프



# 미국과 다른나라의 비교
# library(dplyr) 사용

health_df %>%
  group_by(Country) %>%
  summarise(Spending_USD_mean = mean(Spending_USD),
            Life_Expectancy_mean = mean(Life_Expectancy))
# 위 코드를 실행하면, healthexp 데이터셋을 Country 열을 기준으로 그룹화한 다음,
# 그룹별 Spending_USD와 Life_Expectancy의 평균값을 계산함. 이 결과를 바탕으로,
# 미국과 다른 나라를 구분한 후 각각의 그룹에서 t-검정을 수행할 수 있음.


usa_group <- health_df %>% filter(Country == "USA")
others_group <- health_df %>% filter(Country != "USA")
# 먼저, 미국 그룹과 다른 나라 그룹을 만듦.


t.test(usa_group$Spending_USD, others_group$Spending_USD)
t.test(usa_group$Life_Expectancy, others_group$Life_Expectancy,alternative='greater')
# 이제 usa_group과 others_group 데이터프레임을 이용하여 t-검정을 수행할 수 있음.
# 이때는 t.test() 함수를 사용.

# 위 코드를 실행하면, usa_group와 others_group 각각의 Spending_USD와
# Life_Expectancy 평균값의 차이가 통계적으로 유의미한지 여부를 검정한 결과가 출력.

# alternative hypothesis: true difference in means is greater than 0
# 대립가설: 평균 Life_Expectancy의 차이가 0보다 크다

# 95 percent confidence interval:
# 95% 신뢰구간: -3.193144 ~ Inf (무한대)

# sample estimates:
# 표본평균: Spending_USD 지출이 높은 국가 = 75.84314, Spending_USD 지출이 낮은 국가 = 78.38206

# 즉, 95% 신뢰수준에서 평균 Life_Expectancy의 차이에 대한 검정결과,
#검정통계량이 음수이기 때문에 Spending_USD 지줄이 높은 국가의 Life_Expectancy이 더 낮을 가능성이 있음.






# 결과 분석

# 의료비 지출은 미국이 가장 많다. 하지만,
# 의료비 지출이 많다고 해서 기대수명이 높은 것은 아니다.
# 다른 요인이 작용할수도 있을 것 ((예) 미국은 총기 합법화...)건강이 안좋아서 병원비가 많이 들수도 있고..


#-------------------------------------------------------------------------------------------------------------------------------------------


# 가설 설정4 (코로나로 인해 모든 나라는 2020년에 수명이 줄었을 것이다.)

# 2020년 데이터와 그 이전 년도 데이터로 분리
health_before_2020 <- subset(health_df, Year < 2020)
health_2020 <- subset(health_df, Year == 2020)

# 2020년과 그 이전 년도의 Life_Expectancy 평균 계산
lifeexp_mean_before_2020 <- mean(health_before_2020$Life_Expectancy)
lifeexp_mean_2020 <- mean(health_2020$Life_Expectancy)

# t-test 수행
result <- t.test(health_before_2020$Life_Expectancy, health_2020$Life_Expectancy, alternative = "greater")

# 결과 출력
cat("2020년 Life_Expectancy 평균:", lifeexp_mean_2020, "\n")
cat("이전 년도 Life_Expectancy 평균:", lifeexp_mean_before_2020, "\n")
cat("p-value:", result$p.value, "\n")

# 위 코드에서는 2020년 데이터와 그 이전 년도 데이터를 분리,
# 각각의 데이터에서 Life_Expectancy의 평균을 계산. 이후 두 데이터셋 간의 t-test를 수행,
# 2020년의 Life_Expectancy가 그 이전 년도 대비해서 줄었는지 여부를 검정함.
# 만약 2020년의 Life_Expectancy가 줄었다면, 두 평균의 차이는 0보다 작아질 것. 따라서 alternative 옵션을 "greater"로 설정.

# 실행 결과 p-value가 0.001보다 작게 나왔으므로, 이는 유의미한 결과. 
# 따라서 healthexp 데이터에서 모든 나라의 Life_Expectancy는 2020년도에는 다른 년도 대비해서 줄었을 가능성이 높다고 할 수 있음.
# 하지만, 단순히 상관분석 결과이기 때문에 원인-결과 관계를 규명하기에는 한계가 있음.


# 결과
# 전부 다 떨어지지는 않았고 나라별로 차이가 있다. 떨어진 나라는 왜 떨어졌을까?? 코로나 때문일 가능성.

#-------------------------------------------------------------------------------------------------------------------------------------------

# 최고 기대수명인 나라는 누구?

# 최고 기대수명 나라 찾기
max_long<-health_df[which.max(health_df$Life_Expectancy),"Country"]

# 결과 출력
cat("가장 높은 기대수명 국가", max_long, "\n")

# 왜 일본이지????? 그럼 차이가 있다는 결과가 나온게 일본 때문일까???
# 그래서
# 일본과 다른나라의 평균지출과, 평균 기대수명 t검정 실시


# health_df에서 일본과 그 외 국가 분리
japan <- health_df %>% filter(Country == "Japan")
other <- health_df %>% filter(Country != "Japan")

# Spending_USD와 Life_Expectancy 평균 구하기
japan_mean <- c(mean(japan$Spending_USD), mean(japan$Life_Expectancy))
other_mean <- c(mean(other$Spending_USD), mean(other$Life_Expectancy))

# t-test 수행
result_spending <- t.test(japan$Spending_USD, other$Spending_USD)
result_lifeexp <- t.test(japan$Life_Expectancy, other$Life_Expectancy)

# 결과 출력
cat("Spending_USD t-test 결과:\n", "p-value:", result_spending$p.value, "\n\n")
cat("Life_Expectancy t-test 결과:\n", "p-value:", result_lifeexp$p.value, "\n")


# 각 검정의 p-value 값이 0.05보다 작기 때문에 유의미한 차이가 있다고 할 수 있음.

# Spending_USD의 경우, 일본과 다른 나라들 간의 평균 지출금액에는 유의미한 차이가 있음.

# Life_Expectancy의 경우, 일본과 다른 나라들 간의 평균 수명에도 유의미한 차이가 있음.


#-------------------------------------------------------------------------------------------------------------------------------------------


# 왜 일본이랑 다른나라와 기대수명에서 차이가 나는거지? 그래프를 그려보자!!



# 그래프 결과
ggplot(health_df, aes(x=Year, y=Life_Expectancy, color=Country)) + 
  geom_line() + 
  labs(title="Life Expectancy vs. Year by Country", x="Year", y="Life Expectancy", color="Country")


# 다른 나라 모두 수명이 줄었는데 일본만 그대로...(까비...)
# 코로나로 인해 모든 나라는 2020년에 수명이 줄었을 것이라 예상했는데
# 어느정도는 맞는 말(미국, 영국, 독일, 캐나다)이지만 안타깝게도 일본은 코로나로 인한 기대수명에 영향이 없어보임.
# 아니면 일본의 인구가 고령화 되었기 때문일 수도 있음


#-------------------------------------------------------------------------------------------------------------------------------------------