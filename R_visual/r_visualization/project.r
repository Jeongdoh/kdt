library("ggplot2")


con_df <- read.csv("day_0227\\ex_shiny\\app_lay\\cancer.csv")
head(con_df)


dang_df<-read.csv("day_0227\\ex_shiny\\app_lay\\dang.csv")
dang_df



apply(con_df[,7:8],1,sum)
con_df["19~29세"]=apply(con_df[,7:8],1,sum)
con_df["30~39세"]=apply(con_df[,9:10],1,sum)
con_df["40~49세"]=apply(con_df[,11:12],1,sum)
con_df["50~59세"]=apply(con_df[,13:14],1,sum)
con_df["60~69세"]=apply(con_df[,15:16],1,sum)
con_df["70세이상"]=apply(con_df[,17:21],1,sum)

con_df<-con_df[,c(1,2,22:27)]
con_df
dang_df
colnames(con_df)
colnames(dang_df)






# 데이터프레임 합치기
merged_df <- merge(con_df, dang_df, by = c("성별", "시점"))

# 회귀분석 실행
lm_result <- lm(성별 ~ ., data = merged_df)

# 회귀분석 결과 출력
summary(lm_result)




cancer_20_df <- data.frame(cbind(con_df$"성별",con_df$"19~29세",dang_df$"X19.29세"))
cancer_20_df

cancer_30_df <- data.frame(cbind(con_df$"성별",con_df$"30~39세",dang_df$"X30.39세"))
cancer_30_df

cancer_40_df <- data.frame(cbind(con_df$"성별",con_df$"40~49세",dang_df$"X40.49세"))
cancer_40_df

cancer_50_df <- data.frame(cbind(con_df$"성별",con_df$"50~59세",dang_df$"X50.59세"))
cancer_50_df

cancer_60_df <- data.frame(cbind(con_df$"성별",con_df$"60~69세",dang_df$"X60.69세"))
cancer_60_df

cancer_70_df <- data.frame(cbind(con_df$"성별",con_df$"70세이상",dang_df$"X70세이상"))
cancer_70_df



cancer_20_df$X1<-as.integer(cancer_20_df$X1)
cancer_20_df$X2<-as.integer(cancer_20_df$X2)
cancer_20_df$X3<-as.integer(cancer_20_df$X3)


cancer_30_df$X1<-as.integer(cancer_30_df$X1)
cancer_30_df$X2<-as.integer(cancer_30_df$X2)
cancer_30_df$X3<-as.integer(cancer_30_df$X3)

cancer_40_df$X1<-as.integer(cancer_40_df$X1)
cancer_40_df$X2<-as.integer(cancer_40_df$X2)
cancer_40_df$X3<-as.integer(cancer_40_df$X3)

cancer_50_df$X1<-as.integer(cancer_50_df$X1)
cancer_50_df$X2<-as.integer(cancer_50_df$X2)
cancer_50_df$X3<-as.integer(cancer_50_df$X3)

cancer_60_df$X1<-as.integer(cancer_60_df$X1)
cancer_60_df$X2<-as.integer(cancer_60_df$X2)
cancer_60_df$X3<-as.integer(cancer_60_df$X3)

cancer_70_df$X1<-as.integer(cancer_70_df$X1)
cancer_70_df$X2<-as.integer(cancer_70_df$X2)
cancer_70_df$X3<-as.integer(cancer_70_df$X3)


str(cancer_20_df)




cancer_20_df
cancer_30_df
cancer_40_df
cancer_50_df
cancer_60_df
cancer_70_df





cancer_20_man<-cancer_20_df[1:10,]
cancer_20_woman<-cancer_20_df[11:20,]
cancer_20_man

cancer_30_man<-cancer_30_df[1:10,]
cancer_30_woman<-cancer_30_df[11:20,]


cancer_40_man<-cancer_40_df[1:10,]
cancer_40_woman<-cancer_40_df[11:20,]


cancer_50_man<-cancer_50_df[1:10,]
cancer_50_woman<-cancer_50_df[11:20,]


cancer_60_man<-cancer_60_df[1:10,]
cancer_60_woman<-cancer_60_df[11:20,]


cancer_70_man<-cancer_70_df[1:10,]
cancer_70_woman<-cancer_70_df[11:20,]

cancer_man<-c(cancer_20_man,cancer_30_man,cancer_40_man,cancer_50_man,cancer_60_man,cancer_70_man)
cancer_man<-data.frame(cancer_man)
cancer_man

cancer_woman<-c(cancer_20_woman,cancer_30_woman,cancer_40_woman,cancer_50_woman,cancer_60_woman,cancer_70_woman)
cancer_woman<-data.frame(cancer_woman)
cancer_woman




# 20~70대 남,녀 별 췌장암과 당뇨병의 상관계수 구하기

cor(cancer_man$X2,cancer_man$X3)
cor(cancer_woman$X2,cancer_woman$X3)

cor(cancer_man$X2.1,cancer_man$X3.1)
cor(cancer_woman$X2.1,cancer_woman$X3.1)

cor(cancer_man$X2.2,cancer_man$X3.2)
cor(cancer_woman$X2.2,cancer_woman$X3.2)

cor(cancer_man$X2.3,cancer_man$X3.3)
cor(cancer_woman$X2.3,cancer_woman$X3.3)

cor(cancer_man$X2.4,cancer_man$X3.4)
cor(cancer_woman$X2.4,cancer_woman$X3.4)

cor(cancer_man$X2.5,cancer_man$X3.5)
cor(cancer_woman$X2.5,cancer_woman$X3.5)



# 각각의 결과는 두 변수 간의 선형 상관관계를 나타냄.
# 상관계수는 -1과 1 사이의 값을 가지며, 0에 가까울수록 두 변수 간에 상관관계가 적다는 것을 의미,
# 절댓값이 1에 가까울수록 강한 상관관계를 나타냄.

# 첫 번째 결과에서는 남성의 X2.3과 X3.3 변수 간에 0.424의 양의 상관관계가 있음을 나타냄,

# 두 번째 결과에서는 여성의 X2.3과 X3.3 변수 간에도 약한 양의 상관관계가 있음을 나타냄.

# 세 번째 결과에서는 남성의 X2.4와 X3.4 변수 간에 강한 양의 상관관계가 있음을 나타냄,

# 네 번째 결과에서는 여성의 X2.4와 X3.4 변수 간에도 강한 양의 상관관계가 있음을 나타냄.

# 다섯 번째 결과에서는 남성의 X2.5와 X3.5 변수 간에도 강한 양의 상관관계가 있음을 나타냄,

# 여섯 번째 결과에서는 여성의 X2.5와 X3.5 변수 간에도 강한 양의 상관관계가 있음을 나타냄.




# 가설 (췌장암 : , 당뇨병 : X3  당뇨병이 있므면 췌장암의 발병률이 높다.)
# 회귀분석 결과의 p값은 해당 계수가 0일 때, 
# 귀무가설(null hypothesis)이 기각될 수 있는 유의수준(significance level)을 나타내며,
#  0.05 이하인 경우에는 유의한 결과라고 볼 수 있음.



# 20대 남 회귀분석
model2 <- lm(cancer_man$X2 ~ cancer_man$X3, data = cancer_man)
# 회귀분석 결과 출력
summary(model2)
# Residual standard error: 1.896 on 8 degrees of freedom
# Multiple R-squared:  0.2101,    Adjusted R-squared:  0.1114
# F-statistic: 2.128 on 1 and 8 DF,  p-value: 0.1827


# 20대 여 회귀분석
model22 <- lm(cancer_woman$X2 ~ cancer_woman$X3)
# 회귀분석 결과 출력
summary(model22)
# Residual standard error: 9.761 on 8 degrees of freedom
# Multiple R-squared:  0.2283,    Adjusted R-squared:  0.1318
# F-statistic: 2.367 on 1 and 8 DF,  p-value: 0.1625


# 30대 남 회귀분석
model3 <- lm(cancer_man$X2.1~cancer_man$X3.1)
# 회귀분석 결과 출력
summary(model3)
# Residual standard error: 9.696 on 8 degrees of freedom
# Multiple R-squared:  0.0004318, Adjusted R-squared:  -0.1245
# F-statistic: 0.003456 on 1 and 8 DF,  p-value: 0.9546


# 30대 여 회귀분석
model33 <- lm(cancer_woman$X2.1~cancer_woman$X3.1)
# 회귀분석 결과 출력
summary(model33)
# Residual standard error: 14.19 on 8 degrees of freedom
# Multiple R-squared:  0.08481,   Adjusted R-squared:  -0.02959
# F-statistic: 0.7413 on 1 and 8 DF,  p-value: 0.4143


# 40대 남 회귀분석
model4 <- lm(cancer_man$X2.2~cancer_man$X3.2)
# 회귀분석 결과 출력
summary(model4)
# Residual standard error: 12.45 on 8 degrees of freedom
# Multiple R-squared:  0.0471,    Adjusted R-squared:  -0.07201
# F-statistic: 0.3955 on 1 and 8 DF,  p-value: 0.547

# 40대 여 회귀분석
model44 <- lm(cancer_woman$X2.2~cancer_woman$X3.2)
# 회귀분석 결과 출력
summary(model44)
# Residual standard error: 14.77 on 8 degrees of freedom
# Multiple R-squared:  0.201,     Adjusted R-squared:  0.1011
# F-statistic: 2.013 on 1 and 8 DF,  p-value: 0.1937


# 50대 남 회귀분석
model5 <- lm(cancer_man$X2.3~cancer_man$X3.3)
# 회귀분석 결과 출력
summary(model5)
# Residual standard error: 59.49 on 8 degrees of freedom
# Multiple R-squared:  0.1799,    Adjusted R-squared:  0.07738
# F-statistic: 1.755 on 1 and 8 DF,  p-value: 0.2219


# 50대 여 회귀분석
model55 <- lm(cancer_woman$X2.3~cancer_woman$X3.3)
# 회귀분석 결과 출력
summary(model55)
# Residual standard error: 55.98 on 8 degrees of freedom
# Multiple R-squared:  0.05384,   Adjusted R-squared:  -0.06443
# F-statistic: 0.4552 on 1 and 8 DF,  p-value: 0.5189


# 60대 남 회귀분석
model6 <- lm(cancer_man$X2.4~cancer_man$X3.4)
# 회귀분석 결과 출력
summary(model6)
# Residual standard error: 111 on 8 degrees of freedom
# Multiple R-squared:  0.6214,    Adjusted R-squared:  0.5741
# F-statistic: 13.13 on 1 and 8 DF,  p-value: 0.006745


# 60대 여 회귀분석
model66 <- lm(cancer_woman$X2.4~cancer_woman$X3.4)
# 회귀분석 결과 출력
summary(model66)
# Residual standard error: 105.9 on 8 degrees of freedom
# Multiple R-squared:   0.59,     Adjusted R-squared:  0.5388
# F-statistic: 11.51 on 1 and 8 DF,  p-value: 0.009454


# 70대 남 회귀분석
model7 <- lm(cancer_man$X2.5~cancer_man$X3.5)
# 회귀분석 결과 출력
summary(model7)
# Residual standard error: 202.5 on 8 degrees of freedom
# Multiple R-squared:  0.5713,    Adjusted R-squared:  0.5177
# F-statistic: 10.66 on 1 and 8 DF,  p-value: 0.01144

# 70대 여 회귀분석
model77 <- lm(cancer_woman$X2.5~cancer_woman$X3.5)
# 회귀분석 결과 출력
summary(model77)
# Residual standard error: 279 on 8 degrees of freedom
# Multiple R-squared:  0.5165,    Adjusted R-squared:  0.4561
# F-statistic: 8.548 on 1 and 8 DF,  p-value: 0.01918



