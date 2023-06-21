#작업폴더 위치 설정
getwd()
setwd("C:/Users/y2kjd/Desktop")

#11. titanic_data.csv 로 부터 자료를 읽어서 raw_data로 저장하시오.

raw_data=read.csv(file='titanic_data.csv')

#12. head 함수를 사용하여 입력된 raw_data를 확인하시오. 
head(raw_data)


# 13. raw_data의 자료의 차원을 구하시오. 
dim(raw_data)

# 14. raw_data의 첫번째 열에서 성별(Sex)을 추출하고 gender.txt로 저장하시오.
gender=raw_data[5]
gender
 write.csv(gender,'gender.csv')

# 15. raw_data의 2~10 열의 변수를 선택하여 새로운 객체에 저장하고 sub_data.txt로 저장하시오. 
# (구분은 _을 이용할 것) 
sub_data=raw_data[2:11]
write.table(sub_data,'sub_data.csv',sep='_')

# 16. raw_data의 31~100의 행과 2~10 사이의 짝수 열을 선택하여 새로운 객체에 저장하고 sub_data2.csv로 저장하시오.
# (구분을 comma 사용)
sub_data2=raw_data[31:100,seq(2,10,2)]
sub_data2
write.table(sub_data2,'sub_data2.csv',sep=',')
write.csv(sub_data2,'sub_data2.csv') # sep=기본값이 comma임

# 17. raw_data에서 결측값의 갯수를 구하시오. 
sum(is.na(raw_data))

nrow(which(is.na(raw_data),T)) # 정답

# 18. raw_data에서 결측값의 위치를 1차원 인덱스로 찾으시오. 
which(is.na(raw_data))

# 19. raw_data에서 결측값의 위치를 2차원 인덱스로 찾으시오. 
which(is.na(raw_data),arr.ind = T) 

# 20. raw_data의 Age변수의 결측값의 위치를 index 변수에 저장하고 이를 이용하여 모든 결측 값을 20으로 변경하시오.
index=is.na(raw_data[6])
index
raw_data[index,6]=20
#index=ifelse(is.na(index),20,index)
sum(is.na(raw_data[6]))

# 21. If 조건문을 활용하여, raw_data의 Age 변수를 활용하여 10이상 20미만, 20이상 30미만 … 60이상 70미만, 그 외로
# 출력하는 r프로그램을 작성하시오.
#ifelse(,,ifelse())

age=raw_data[6]
age

ifelse(age>=70,"70대 이상",
ifelse(age>=60,"60대",
ifelse(age>=50,"50대",
ifelse(age>=40,"40대",
ifelse(age>=30,"30대",
ifelse(age>=20,"20대",
ifelse(age>=10,"10대",
ifelse(age<=10,"10대미만",''))))))))


# ifelse((raw_data$Age>=10) & (raw_data$Age<20),'10이상 20미만',
# ifelse((raw_data$Age>=20) & (raw_data$Age<30),'20이상 30미만',
# ifelse((raw_data$Age>=30) & (raw_data$Age<40),'30이상 40미만',
# ifelse((raw_data$Age>=40) & (raw_data$Age<50),'40이상 50미만',
# ifelse((raw_data$Age>=50) & (raw_data$Age<60),'50이상 60미만',
# ifelse((raw_data$Age>=60) & (raw_data$Age<70),'60이상 70미만','그외'))))))




# 22. If 조건문을 활용하여 raw_data의 Cabin 변수에서 결측값이 들어간 위치에 ‘DELETE’라는 값으로 변경하시오.
index1=is.na(raw_data[11])
raw_data[index1,11]='DELETE'
raw_data[11]
ifelse(raw_data[11]=="",'DELETE',raw_data$Cabin)
