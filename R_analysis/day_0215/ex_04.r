# 내부 데이터 iris--------------------------------------
# 데이터에 기본 정보 출력
str(iris)
colnames(iris)


# 결측치 체크 &처리
sum(is.na(iris))


# 꽃받침 너비에 대한 이상치 체크
sepal<-iris$Sepal.Length
sepal
sum(is.na(iris$Sepal.Length))

mean(sepal)
median(sepal)
min(sepal)
max(sepal)

S<-quantile(distData, probs = seq(0, 1, 0.25), na.rm = FALSE)
S


