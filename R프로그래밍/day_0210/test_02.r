x=vector()
for(i in 1:5){
    x[i]=i
}

x




for(i in 1:9){
    cat('3* ',i,'=', 3*i,end='\n')
}




for(i in 1:5){
    cat(rep('*',i),end='\n')
}



x<-c(1,2,3,4,5)
sum=0
for(i in 1:5){
    sum<-sum+x[i]/length(x)
 }
sum

# 분산
x<-c(1,2,3,4,5)
mean_x=mean(x)

sum=0
for(i in 1:length(x)){
    sum=sum+(x[i]-mean_x)**2
}
sum/(length(x)-1)

var(x)

# 실습문제 : x<-c(1,2,3,4,5)가 주어질 때, mean() 함수를 쓰지 않고, 
#for문과 if 조건문을 사용하여 x의 홀수에 대한 평균을 구하시오.

x<-c(1,2,3,4,5)
sum=0
for(i in 1:5){
    if(i%%2==1)
    sum<-sum+x[i]
 }
sum/3


#실습문제 : 4행 5열을 가지는 빈 매트릭스를 생성하고, 
# for문 안에 for문을 한번 더 작성하여
# xmat<-matrix(1:20,4,5)와 같은 결과를 가지는 매트릭스를 생성하고 출력하라

xmat=matrix(1:20,4,5)
xmat

xmat=matrix(nrow=4,ncol=5)
xmat

for (i in 1:nrow(xmat)){
    for (j in 1:ncol(xmat)){
        xmat[i,j]=i+(nrow(xmat)*(j-1))
    }
}
xmat


#• 주어진 조건을 만족할 때까지만 반복하는 구문
i =1
while(i <= 5) {
cat(rep('*',i),'\n')
i = i + 1
} 

#• break 문이 포함된 반복문을 빠져 나오는 명령어

s = 0
for ( i in 1:10) {
s = s+i
if (i>=5) {break}
}

i=-1
while(i<=10){
    cat(i,'\n')
    i=i+1
    if (i==9){
        cat('발사')
        break
    }
}

#next 문
s = 0
for ( i in 1:10) { 
if (i%%2==1) {next} 
s = s+i
}
s

# 실습문제
x<-c(1,5,2,3,8)
a=0
l=0
for(i in 1:length(x)){
    if (x[i]%%2==1){next}
    sum=(sum+x[i])
    l=l-1
}
sum/l



#구구단 에제
googoo81 <- function(x) {
cat('\n')
for(i in 1:9) {
cat(x, ' * ',i, ' = ', x*i, '\n')
}
cat('\n')
}
googoo81(5)


#함수의 인수는 default로 설정이 가능하며 default 설정된 인수 들은 생략이 가능
a <- c(1,3,5,6)
mean.k <- function(x,k){
return(mean(x^k))
}
mean.k(a,2)
mean.k(a) # 인수를 집어넣지 않아 에러가 발생
mean.k2 <- function(x,k=3){
return(mean(x^k))
}
mean.k2(a,2)
mean.k2(a) 


#여러 인수를 입력 받는 경우, 인수의 이름을 생략 시 순서대로 입력
a <- c(1,3,5,6) 
m.k <- function(x,k,t){
return(mean((x-t)^k))
}
m.k(a,2,1) 
m.k(a,1,2) 
m.k(a,k=2,t=1)
m.k(a,t=2,k=1)


#함수의 리턴값(반환값)은 하나의 객체만 허용

# 자료를 입력받아 평균, 분산, 표준화된 자료를 반환하고자 할 때,
a <- c(1,3,5,6) 
std.ftn <- function(x){
return(mean(x),var(x))
}
std.ftn(a) #에러 발생

#여러 값을 반환하고자 할 때, list 또는 data.frame을 이용하여 하 나로 묶어서 반환
a <- c(1,3,5,6) 
std.ftn <- function(x){
return(list(mean=mean(x),var=var(x)))
}
std.ftn(a)


# 지역변수
# • 가장 기본이 되는 변수로 함수의 내부에서 사용 될 때에는 함수가 종료됨과 동시에 변수가 삭제
a <- c(1,3,5)
noact <- function(x){
loc <- 3 
return(loc)
}
noact(a)
loc




#  GlobalEnv (기본작업공간)에서 정의한 변수는 함수에서 참조가 가능
#  함수 내부에서 GlobalEnv의 지역 변수의 값을 바꾸어 사용할 수 있으나 GlobalEnv에 존재하는 변수의
# 값은 변하지 않음

a <- c(1,3,5)
noact <- function(x){
a[1] <- 3 
return(a)
}
noact(a)
a


# 전역변수
# • 특별히 여러 함수에서 접근하여 값을 변경할 필요가 있을 때 정의 하며 함수에서 값의 변경 및 접근이 가능하다. 
# 함수가 종료해도 사라지지 않음
 #전역변수를 설정 하는 방법: 변수 이름 <<- 값

a <- c(1,3,5)
noact <- function(x){
a[1] <- 3
glb<<- c(1,2)
return(a)
}
noact(a)
A
glb


# 전역변수
# • 함수 내부에서 GlobalEnv 내의 변수의 일부의 값을 변경하고자 할 때, <<- 연산자를 사용

a <- c(1,3,5)
noact <- function(x,type=1){
if(type==1){a[1] <- 3}
if(type==2){a[1] <<- 3}
return(a)
}
noact(10)
a
noact(5,2)
a


# bmi지수 함수 만들기
weight=c(55,65,50,60,45)
height=c(1.68,1.70,1.60,1.65,1.62)

bmi=function(weight,height){
    res=weight/(height**2)
    return(res)
}
bmi(weight,height)
bmi(90,1.77)
