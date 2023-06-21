#--------------------------------------------------------------
# 선형회귀 구현
# -> 회귀계수 기울기, 절편
#--------------------------------------------------------------
# 데이터 준비----------------------------------------------------

score<-c(52,66,72,83,91,97)
hour<-c(1,2,3,4,5,6)
shDF<-data.frame(score=score,hour=hour)

# 데이터 분포확인---------------------------------------------
# 선형성 확인
plot(score,hour,main=Score)





shapiro.test(shDF$hour)
shapiro.test(shDF$score)

qqplot(shDF$hour,shDF$score)

# 데이터를 만족하는 직선 생성-----------------------------------
# 1차 함수 y=slope*x+intercept
# - 기울기 =
#--------------------------------------------------------------
sMean<-mean(shDF$score)
hMean<-mean(shDF$hour)


# 기울기
slope<-sum((shDF$score-sMean)*(shDF$hour-hMean))/sum((shDF$score-sMean)^2)

# 절편
intercept<-hMean-(sMean*slope)
intercept

#직선식 : 1차 함수 y= slope*x + intercept
sMean<-mean(shDF$score)
hMean<-mean(shDF$hour)

















