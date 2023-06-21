#----------------------------------------------------------------
# 시각화 관련 패키지
# ggplot, tidyverse
#----------------------------------------------------------------
#install.packages("tidyverse")
library(tidyverse)

library(ggplot2)


#----------------------------------------------------------------
# 시각화 실습
#----------------------------------------------------------------
# 내장 데이터 셋 mpg
str(mpg)
mpg

colnames(mpg)
# mpg데이터 시각화 => 그래프---------------------------------------
# ggplot() : plot 객체 초기화
# geom_point(): 데이터 표시해주는 함수
#               - x,y 좌표설정
#               - color 포인트 색상
#               - size 포인트 크기
#               - alpha 포인트 투명도
ggplot(data=mpg) + 
geom_point(mapping = aes(x=displ, y=hwy,color=class, size=class, alpha=0.2, shape=class))

# 제공되는 색상------------------------------------------------------
colors()[1:10]

# 화면 분할 후 그래프 출력--------------------------------------------
mpgPlot<-ggplot(data=mpg)
mpgPlot+geom_point(mapping = aes(x=displ,y=hwy))+facet_wrap(~class, nrow = 2)













