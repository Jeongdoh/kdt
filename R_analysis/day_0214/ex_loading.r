# 저장한 데이터 로딩-----------------------------
popdata

savePath='day_0214/data/2010_population.RData'
load(savePath)
str(popdata)

#컬럼의 값별 데이터 갯수 -> table(데이터)
table(popdata$V1)
table(popdata$V3)


#범주형 데이터 빈도 표현 >> 막대그래프
barplot(table(popdata$V3))


#남자 자녀수 몇명인지 확인
table(popdata$'남아출생수')
popdata['남아출생수']
plot(table(popdata$'남아출생수'))
