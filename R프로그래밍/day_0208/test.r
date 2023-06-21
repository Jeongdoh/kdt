print('hellow')
print('hellow')
print('hellow')
print('hellow')
print('hellow')
print('hellow')
print('hellow')

1
2
3
4

# 기초계산
1+1;2+2;3+3
print("------------------")
3+5
8-3
3*8
12/4
5**2
5^2
11%%4
18%/%3
print("------------------")
2>5
2>=6
4==4
5!=5
3|4
3&4
print("------------------")
4>3&&3==3
4<3&2==2
!FALSE
print("------------------")
a<-1
b=3
ab<-a+b
ab
print("------------------")
Abc<-1
a.b.c<-3

r=4
circle=r*pi^2
circle

class=3500
n=30
average=class/n
average

x<-'char'
mode(x)

x<-5
is.character(x);is.numeric(x);is.double(x)


# 정수형 변환 코드
real<-3.5
as.integer(real)

intg<-3
is.integer(intg)

intg2<-as.integer(3)
is.integer(intg2)


# 벡터
vec<-c(1,2,3,4,5)
vec


num<-c(1,2,3)

ch<-c('red','blue','yellow')

lo<-c(T,F,F,T)

num2<-c(1,2,'red','blue')

lo2<-c(T,F,T,1,3)

lo3<-c(T,F,'abc')

x<-c(1,2,3)
y<-c(1,2,3,4)
x+y
x-y
x*y
x/y

A<-T; B<-F; C<-c(T,T);
D<-c(F,T)
A & B
A && B
C & D
C && D

A<-T; B<-F; C<-c(T,T);D<-c(F,T)
A | B
A || B
C | D
C || D


a<-c(1,2);b<-c(2,2);d<-c(3,4)
a<b
a<=b
a<d
a<=b
a>b
a>=b

A<-c(T,T); B<-c(F,T); C<-c(T,T); D<-c(T,F)
A==B
C==D
all(A==B)
all(A==C)
any(A==B)
any(A==C)



# 수학 관련 함수
log(10)
log(10,base=x)
log10(10)

exp(1);exp(2)
sin(30);sin(pi/2)
x<-c(1,3,2,4,10);max(x)

var(x)
sum(x-mean(x)^2)/(length(x)-1)

x<-c(1,5,3,2,4);sort(x)#sort(x,descreasing=T)
order(x)

x[order(x)]

weight=c(55,65,50,60,45)
height=c(1.68,1.70,1.60,1.65,1.62)

mean(weight)
sd(weight)

x<-1:100
x<-seq(1,100,1)
x
# 첫째 인수 : 시작숫자
# 두번째 인수 : 마지막 숫자
# 세번째 인수 : 단위
x<-seq(1,100,2)
x


x<-1:10
y<-3.3:8
x;y;

x<-100:1
x


rep(c(1,2),times=3)
rep(c(1,2),each=3)



x<-c('0','21','12','16')
x

as.integer(x)
sort(x)

as.character(x)
x

y<-seq(0,30,10)
y

x<y & x<=y

a=rep(c(T,F),5)
a


vec<-vector()
vec<-1:10
vec2<-c('abc','def')
vec3<-c(T,F,F,T)

names(vec2)<-c('first','second')

vec4<-vector()
vec4<-1:vec4[2]<-5;vec4



x1<-matrix(1:10,nrow=5,ncol=2,byrow=T)
x2<-matrix(1:10,5,2,byrow=F)
cbind(x1,x2)
rbind(x1,x2)


A=matrix(1:12,4,3)
rownames(A)<-c('n1','n2','n3','n4')
colnames(A)<-c('x1','x2','x3')

rname<-c('n1','n2','n3','n4')
cname<-c('x1','x2','x3')
B<-matrix(1:12,4,3,dimnames=list(rname,cname))


A<-matrix(1:12,4,3)
A[1,2];A[2,3]

A[1,]
A[,2]

A[c(1,3),]
A[,1:2]
A[,-3]




A<-matrix(1:12,4,3);B<-matrix(1,4,3)
A+B;A-B

A<-matrix(1:6,2,3);B<-matrix(1,3,2)
A%*%B #3*3행렬

A<-matrix(1:4,2,2)
solve(A)


#전치행렬
A<-matrix(1:4,2,2)
A


t(A)
solve(A)


#det(행렬)함수
A<-matrix(1:4,2,2)
det(A)

#고유값, 고유벡터
A<-matrix(1:4,2,2)
eigen(A)


#리스트
lst1=list(a=1:10, b=matrix(1:4,2,2))
lst1


lst2<-list()
lst2[[1]]<-matrix(1:10,5,2)
lst2[[2]]<-lst1


lst1[1]
lst1[[1]]
lst2[[1]]
lst2[[1]][[3]]
lst1[[2]][1,1]



#factor(요인)

#levels
#order=
#(levels 및 order를 생략하면 default로 처리됨)
grade<-c('A','A','B','C','B','B')
f2.grade<-factor(grade,order=T)

lev<-c('C','B','A')
f3.grade<-factor(grade,levels=lev,order=T)


levels(f2.grade)
levels(f3.grade)


x1=1:4
x2=c('kim','lee','jung','park')
dat=data.frame(x1,x2)
dat
dat2=data.frame(num=x1,name=x2)
dat2


dat2$num
dat$name
dat3=data.frame(x1,x2,stringAsFactors=F)

dat[,1];dat[,2]
dat[1,];dat[2,]
dat[2,1];dat[3,2];dat3[3,2]


# 배열

x1=array(1:24,dim=c(4,3,2))
x1
x2=array(1:32,dim=c(2,2,4,2))
x2

x1[,,1]
x1[,,2]
x2[,,3,1]

# 데이터프레임 행렬

d=data.frame(a=1:10,b=rep("A,10"),c=rep(T,10))
d
m1=as.matrix(d)
m1
m2=as.matrix(d[,1])
m3=as.matrix(d[,c(1,3)])
m4=as.matrix(d[,2:3])
d1=as.data.frame(m1,strinAsFactors=T)
d2=as.data.frame(m2,strinAsFactors=F)
d3=as.data.frame(m3,strinAsFactors=F)
d4=as.data.frame(m4,strinAsFactors=F)

# 논리값
x=1:100
sum1=sum(x[13:100])
x=c(1:5,10:20,30:45,2:5,11:30)
x>12
sum2=sum(x[x>12])
sum3=sum(x[x>10 & x<20])



# 1. 등차수열 1,3,5,... 를 1부터 30까지 생성하여 x에 저장하시오.
x=seq(1,30,2)
x
# 2. ‘A’,’B’,’C’의 값을 10번 반복하여 30개의 원소를 갖는 문자열 벡터 y를 생성하시오.
y=rep(c('A','B','C'),times=10)
y
# 3. 0,1을 각각 15번 씩 반복하여 길이 30인 벡터 z를 생성하고 이를 문자형으로 변환하여 z1에 저장하시오.
z=rep(c(0,1),times=15)
z

z1=as.character(z)
z1
# 4. 1번의 x를 이용하여 6 x 5 의 행렬을 생성하고 xmat 변수에 저장 하시오. (행기준으로 채움)
xmat=matrix(x,nrow=6,ncol=5,byrow=T)
xmat
# 5. 1,2,3의 결과를 각각 성분으로 갖는 리스트 생성하시오.
lst=list(x,y,z1)
lst

# 6. x,y,z1을 변수로 갖는 데이터프레임을 생성하고 dat로 저장하시오. (문자열 요인화 방지)
dat=data.frame(x,y,z1)
dat
# 7. 6의 dat 중에서 첫번째와 두번째 변수를 선택하여 행렬로 변환하시오.
as.matrix(dat[-3])
# 8. 6의 dat 중에서 첫번째와 세번째 변수를 선택하여 행렬로 변환하시오.
as.matrix(dat[-2])

# 9. 1의 x 벡터에서 10보다 크고 20보다 작은 원소의 합을 구하시오.
sum(x[x>10&x<20])

# 10. 4의 xmat에서 행의 합, 열의 평균, 열의 분산 값을 각각 계산하시오.
sum(xmat[1,])
sum(xmat[2,])
sum(xmat[3,])
sum(xmat[4,])
sum(xmat[5,])
sum(xmat[6,])
mean(xmat[,1])
mean(xmat[,2])
mean(xmat[,3])
mean(xmat[,4])
mean(xmat[,5])
var(xmat[,1])
var(xmat[,2])
var(xmat[,3])
var(xmat[,4])
var(xmat[,5])
