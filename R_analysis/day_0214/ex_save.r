#-----------------------------------------------------------------
# 이산적 데이터 자료를 표현
# -> 각 데이터 (값)dp vygus >> table()
# -> 막대 그래프 표현
#-----------------------------------------------------------------

#외부데이터 가져오기(로딩)-----------------------------------------
file_name='day_0214/data/2010_population.csv'
popdata<-read.csv(file_name,header = F)
str(popdata)

#데이터 백업 -> save(데이터, 파일경로)
savePath='day_0214/data/2010_population.RData'
save(popdata,file=savePath)

# 코드(숫자) 범주형 데이터를 문자형으로 형변환
#factor(데이터, levels, labels)
popdata$V1<-factor(popdata$V1,levels=c(1:2),labels=c('남자','여자')) 
str(popdata)
popdata$V3<-factor(popdata$V3,levels=c(1:14),labels=c('가구주','가구주의 배우자','자녀','자녀의 배우자',
'가구주의 부모','배우자의 부모','손자녀',
'그 배우자','증손자녀','그 배우자','조부모',
'형제자매','그 배우자','형제자매의 자녀',
'그 배우자','부모의 형제자매','그 배우자',
'기타 친인척','그외같이사는사람'))

popdata$V4<-factor(popdata$V4,levels=c(1:8),labels=c('가구주','가구주의 배우자','자녀','자녀의 배우자',
'안 받았음','초등학교','중학교',
'고등학교','대학-4년제 미만','대학-4년제 이상','석사과정',
'박사과정'))

str(popdata)

save.image('data.RData')
