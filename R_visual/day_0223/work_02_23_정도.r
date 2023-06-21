# 1. 아래 데이터를 활용하여 분석해 주세요. - heightweight.csv iris.csv
# - 전처리 - 데이터 기술통계
hw_df<-read.csv("day_0223\\data\\height_weight.csv")
iris_df<-read.csv("day_0223\\data\\iris.csv")

source("utils\\util.r")

displayInfo(hw_df)


hw_df

checkNa(hw_df)
checkMode(hw_df)


hw_df.cor<-cor(hw_df[-5])
hw_df.cor


find_outliers()
#bmi=몸무게/(키*키)=?


# - 선형관계






# - 단순회귀분석






# - 다중회귀분석






# - 다항회귀분석

































