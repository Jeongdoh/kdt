# 벡터

v2 <- c(T, F, 3, 3.14)
v2
v3 <- c(T, F, 3, "3.14")
v3
v <- c(10, 20, 30, 40, 50, 60, 70)
v[-1]
library(palmerpenguins)
summary(penguins[, c(1, 2, 7)])


#내장 함수

#수학 관련
# 함수정의                    출력값
# abs(x)                      절대값
# sqrt(x)                     제곱근
# log(x), log10(x)    자연로그, 밑이 10인 로그
# exp(x)              자연 상수 𝑒의 거듭제곱
# sin(x), cos(x), tan(x)      삼각 함수
# ceiling(x), floor(x)        천장값, 바닥값
# round(x, digits = n)        반올림수

#통계 관련
# 함수정의                        출력값
# sum(x)                          합계
# mean(x)                         평균
# var(x)                          분산
# sd(x)                           표준편차
# median(x)                       중앙값
# quantile(x, probs)              분위값
# min(x), max(x)              최솟값, 최댓값
# range(x)                        범위값

#사용자 정의 함수
func1 <- function (x, y, z) {
       return (x + 2 * y + 3 * z)

}

func1(1,2,3)



#데이터 프레임: data.frame
#R에서 2차원 테이블 형태로 데이터셋을 저장하는 가장 기본적인 자료구조
# 인덱싱 할때는 data[행,열] 로 구분해서 빼오면 됨

# 데이터 객체의 자료형 확인과 변환:
# • is.xxx() 함수: 데이터 구조의 자료형 확인
# • as.xxx() 함수: 데이터 구조의 자료형 변환
# • 행렬은 데이터 프레임으로 자료형 변환이 가능함

v1 <- 1:7
v2 <- c('홍길동', '전우치', '주니온', '아사달', '아사녀', '연오랑', '세오녀')
v3 <- factor(c('M', 'M', 'M', 'M', 'F', 'M', 'F'))
df <- data.frame(no = v1, name = v2, sex = v3)
str(df)
head(df)


#벡터에 포함된 결측치를 다른 값으로 대체하기
x <- c(45, NA, 87, 63, 55, NA, 72, 61, 59, 68)
is.na(x)
x[is.na(x)]
x[!is.na(x)]
x[is.na(x)] <- mean(x, na.rm = T)
x

# complete.cases() 함수: 데이터 프레임에서 결측치가 포함된 관측값(행) 확인
airquality
str(airquality)
df <- airquality
complete.cases(df)
df[complete.cases(df), ]
df[!complete.cases(df), ]
# 결측치에 관련된 정보 확인: 결측치의 개수와 비율
sum(is.na(df$Ozone))
sum(is.na(df$Solar.R))
sum(is.na(df$Solar.R) & is.na(df$Ozone))

sum(!complete.cases(df))
mean(!complete.cases(df))

#na.omit() 함수: 데이터 프레임에서 결측치를 제거
df <- na.omit(airquality)
str(df)

#mice 패키지의 mice() 함수: 결측치를 여러 가지 통계적 방법으로 대체(imputation)
result <- mice(airquality, method="mean", m = 2, maxit = 2)
result$imp$Ozone
result$imp$Solar.R


#boxplot() 함수: 데이터셋에 이상치가 존재하는 지를 시각화
df <- data.frame(state.x77)
boxplot(df$Income, pch = 19, col = "orange", border = "brown")

#boxplot.stats() 함수를 이용한 이상치에 대한 상세 확인
boxplot.stats(df$Income)




#  기술적 통계: descriptive statistics
# - 수집한 데이터의 특성을 수치로 요약하거나 시각적으로 표현하는 통계분석 방법
# - 평균, 표준편차, 교차표, 히스토그램, 막대그래프 등


#  추론적 통계: inferential statistics
# - 수집한 표본집단으로부터 모집단의 특성을 추정하기 위한 통계분석 방법
# - 가설검정, 평균검정, 분산분석, 카이제곱검정, 회귀분석 등



# 변수(변량): variable or variate
# - 변수: 관찰, 측정, 실험, 또는 조사의 대상이 되는 수량
# - 관측값(observations): 변수(변량)에 대한 관측을 통해 얻는 값


# 변수의 종류:
# - 연속형(continuous): 수치로 표현할 수 있는 변량. 예) 키, 몸무게
# - 범주형(categorical): 범주로 표현할 수 있는 변량. 예) 성별, 혈액형


# 변수의 구분:
# - 독립변수(independent): 종속변수에 영향을 주는 변수. 예) 부모의 키
# - 종속변수(dependent): 독립변수로부터 영향을 받는 변수. 예) 자녀의 키


#1. 데이터 불러오기

# CSV 파일 불러오기
data <- read.csv("data.csv", header = TRUE, stringsAsFactors = FALSE)


#2. 기술통계량 계산하기
# 평균 계산하기
mean(data$col1)

# 중앙값 계산하기
median(data$col1)

# 분산 계산하기
var(data$col1)

# 표준편차 계산하기
sd(data$col1)

# 최소값 계산하기
min(data$col1)

# 최대값 계산하기
max(data$col1)

# 사분위수 계산하기
quantile(data$col1)


#3. 가설 검정하기
# 단일표본 t-검정
t.test(data$col1, mu = 0)

# 독립표본 t-검정
t.test(data$col1 ~ data$col2)

# 대응표본 t-검정
t.test(data$col1, data$col2, paired = TRUE)

# 카이제곱 검정
chisq.test(data$col1, data$col2)

# 분산분석
aov(data$col1 ~ data$col2)

# 상관관계 분석
cor.test(data$col1, data$col2)


#4. 데이터 시각화하기
# 히스토그램
hist(data$col1)

# 박스플롯
boxplot(data$col1)

# 산점도
plot(data$col1, data$col2)



# 통계적 가설 검정은 주어진 데이터를 이용하여 가설을 검정하는 방법으로, 보통 다음과 같은 과정으로 진행됩니다.

# 귀무가설과 대립가설 설정
# 검정 통계량 계산
# 유의수준과 자유도를 이용하여 p-value 계산
# p-value와 유의수준을 비교하여 귀무가설을 기각할지 채택할지 결정
# 다음은 일반적인 가설 검정 방법들입니다.

# 단일 표본 검정 (One-Sample Test)
# 특정 모집단에서 추출된 표본에 대한 가설 검정
# 예시: 한 학급의 평균 키가 170cm인지 아닌지 검정
# 독립 표본 검정 (Independent Samples Test)
# 두 개의 독립적인 모집단에서 추출된 두 개의 표본에 대한 가설 검정
# 예시: 여자와 남자의 평균 키가 차이가 있는지 검정

# 대응 표본 검정 (Paired Samples Test)
# 같은 모집단에서 추출된 두 개의 표본에 대한 가설 검정
# 예시: 같은 학생들이 1학년 때와 2학년 때의 시험 성적 차이가 있는지 검정

# 분산 분석 (Analysis of Variance, ANOVA)
# 두 개 이상의 그룹의 평균값의 차이에 대한 가설 검정
# 예시: A, B, C 세 그룹의 평균 키가 모두 같은지 검정

# 상관 분석 (Correlation Analysis)
# 두 변수 간의 상관 관계를 검정하는 방법
# 예시: 공부 시간과 시험 성적 간의 상관 관계를 검정

# 카이 제곱 검정 (Chi-Square Test)
# 두 개 이상의 범주형 변수 간의 독립성 검정
# 예시: 남녀별로 선호하는 색깔이 같은지 다른지 검정


# 가설검정에서는 검정하고자 하는 가설에 따라 검정 방법이 달라집니다. 각 조건에 맞는 검정 방법들을 설명하겠습니다.

# 모집단의 분산을 알고 있는 경우 (z 검정)
# 대상: 모집단의 분산을 알고 있는 경우
# 가설: 모집단의 평균이 특정한 값과 같다/크다/작다.
# 검정통계량: (표본평균 - 가설에서 주장하는 평균) / (모집단 표준편차 / sqrt(n))
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 모집단의 분산을 모르는 경우 (t 검정)
# 대상: 모집단의 분산을 모르는 경우
# 가설: 모집단의 평균이 특정한 값과 같다/크다/작다.
# 검정통계량: (표본평균 - 가설에서 주장하는 평균) / (표준오차)
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 두 개 이상의 집단을 비교하는 경우 (ANOVA 분석)
# 대상: 두 개 이상의 집단을 비교하는 경우
# 가설: 집단 간의 평균이 모두 같다/다르다.
# 검정통계량: F-통계량
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 두 개의 집단을 비교하는 경우 (t 검정)
# 대상: 두 개의 집단을 비교하는 경우
# 가설: 두 집단의 평균이 같다/다르다.
# 검정통계량: (표본평균1 - 표본평균2) / (sqrt( (표본분산1/n1) + (표본분산2/n2) ))
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 이항 검정
# 대상: 범주형 자료(성공/실패)의 차이를 비교하는 경우
# 가설: 두 집단의 성공 비율이 같다/다르다.
# 검정통계량: z-통계량
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 카이제곱 검정 (Chi-squared test)
# 대상: 범주형 자료(빈도수)를 이용하여 변수 간의 관계를 분석하는 경우
# 가설: 두 변수가 독립인지 아닌지를 검정
# 검정통계량: (예상빈도-실제빈도)^2/예상빈도의 총합, 예상빈도는 각 집단의 행과 열 합계를 기반으로 예측한 값
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 순서형 자료의 검정 (Mann-Whitney U 검정, Wilcoxon signed-rank test)
# 대상: 순서형 자료(서열, 순위)를 이용하여 두 개의 집단을 비교하는 경우
# 가설: 두 집단의 분포가 같은지 아닌지를 검정
# 검정통계량: Mann-Whitney U 검정은 두 집단의 순위 합을 비교하여 계산하고, 
# Wilcoxon signed-rank test는 짝을 이루는 관찰값의 차이를 절대값으로 변환하여 순위를 매긴 후, 
# 양수와 음수 부분의 순위 합을 비교하여 계산한다.
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 단일 모집단에서 비롯된 비율 검정 (One-sample proportion test)
# 대상: 단일 모집단에서 비롯된 범주형 자료의 비율에 대해 검정하는 경우
# 가설: 모집단의 비율이 특정한 값과 같은지 다른지를 검정
# 검정통계량: z-통계량
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.


# 대응표본 t 검정 (Paired-sample t-test)
# 대상: 두 개의 집단을 비교할 때, 짝을 이루는 관찰값이 있는 경우
# 가설: 짝을 이루는 두 집단의 평균이 같은지 다른지를 검정
# 검정통계량: 각 집단에서의 차이의 평균값을 이용하여 t-통계량을 계산한다.
# p-value를 구하여 귀무가설을 기각할지 채택할지 결정한다.



