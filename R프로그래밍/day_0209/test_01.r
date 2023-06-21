x_mat=matrix(rnorm(100),20,5)
apply(x_mat,2,mean)
apply(x_mat,1,sum)
apply(x_mat,2,var)
apply(x_mat,1,var)

set.seed(123)
rnorm(100)

myname="jung do"
paste("My name is",myname, sep=" ")
file_id=1533
paste("Dataset_",file_id,".txt",sep="")

# 문자열 다루는 함수들
#nchar 예시
test=c("abcdefg","AFFY1245820")
nchar(test)

#substr 예시
f_name="AFFY1245820"
substr(f_name,5,7)

#현재 작업폴더
getwd()

#작업폴더 위치 설정
setwd("C:/Users/y2kjd/Desktop")

#
getwd()

#
dir()

#에딧파일 만들어서 저장
dat=data.frame()# 비어있는 데이터프레임
dat=edit(dat)
dat


#scan 함수를 이용한 자료입력
x=scan(file="input_noh.txt",what=numeric())
x
x=scan(file="input_noh.txt",what=character())
x
x=scan(file="input_noh.txt")
x


#read.table 함수를 이용한 자료의 입력
dat=read.table(file="input_noh.txt")
dat
dat2=read.table(file="input_noh.txt",header=T)
dat2


#read_csv
dat=read.csv(file='test3.txt')
dat

#문자열의 요인자동변환 방지:stringsAsFactors=F  옵션
dat2=read.csv(file="test3.txt",stringsAsFactors=F)
dat2


#파일만들어서 내보내기
write.csv(dat2,'jungdoh.csv')

#실습
dat=read.csv(file='개인정보.txt')
dat

#키 몸무게 뽑기
dat_info=dat[,c(2,3)]
dat_info

stat_info=c('평균','중앙값','분산')
stat_info

mean_info=apply(dat_info,2,mean)
mean_info=as.vector(c('평균',mean_info))
mean_info

dat[6,]=mean_info
dat[6,]

dat[7,]=median_info
dat[7,]

var_info=apply(dat_info,2,var)
var_info=as.vector(c('분산',var_info))
var_info

median_info=apply(dat_info,2,median)
median_info=as.vector(c('중앙값',median_info))
median_info

dat[8,]=var_info

dat

write.csv(dat,'작업완료.csv')


#cat함수를 이용한 화면 출력 및 파일 출력
x=1:10
cat(x,file="x.txt",sep="\n")
cat(x,sep="\t")
cat("\n",1,"st element of x=",x[1])


#write.table함수를 이용한 파일출력
x1=1:20
x2=rep(c("A","B","B","A"),5)
x3=rep(c(T,F),each=10)
dat=cbind(x1,x2,x3)
write.table(dat,file="test1.txt",row.names = T,col.names = T,quote = T,sep="/t")
write.table(dat,file="test2.txt",row.names = F,col.names = F,quote = F,sep="/n")
write.table(dat,file="test3.txt",sep=",")


#header or tail
dat=read.csv(file='test3.txt')
head(dat,20)
tail(dat,10)

#length or dim
length(dat[,1])
dim(dat)
dim(dat)[1]
dim(dat)[2]
#nrow(dat);nco(dat)


# 결측치 확인
x=matrix(c(NA,1,3,NA,NA,2),3,2)
is.na(x)
sum(is.na(x))

#결측치 위치확인
which(is.na(x))
which(is.na(x),arr.ind=T)
which(is.na(x),T)


#if조건문
#예제1
x=1:5
y=-2:2

if(any(x>0)) {print(x)}
if(any(y<0)) {print(abs(y))}
if(any(y<0)) {
    print(abs(y))
    cat("\n y contains negative values")
    }

#예제2
if(pi>3) {cat('\n expr(T)')}else{cat('\n expr(F)')}
if(pi<3) {cat('\n expr(T)')}else{cat('\n expr(F)')}

x=1:5
if(length(x)==5){
    if(sum(x)==15){cat('\n Vector x length=',length(x),',sum=',sum(x))}
    else{cat('\n Vector x length !=',length(x))}
}


#예제3
ax^2+bx+c

a=1;b=2;c=3

d=b^2-4*a*c
print(d)
if(d>0){
rt=c((b-sqrt(D))/(2*a),(-b+sqrt(D))/(2*a))
        }else if(d==0){
    rt=-b/(2*a)
    }else{
cat('\n No roots')
    }


#예제4
#시험점수를 매겨, 50점 이상이면 pass, 아니면 fail
x=c(10,3,6,9)
y=c(1,5,4,12)
ifelse(x>y,x,y)
score=c(80,75,40,98)
grade=ifelse(score>=50,"pass","fail")
data.frame(score,grade)

#여러ifelse문
y=2:2
ifelse(y>=0,y,-y)
abs(y)

tmp=c(3,-1,1,-2,0)
sn=ifelse(tmp>0,'pos',ifelse(tmp<0,'neg','zero'))
data.frame(tmp,sn)


#switch문

x=c(1,3,2,5,2)
i=4
switch(i,mean(x),median(x),sd(x),var(x))

type='mean'
switch(type,mean=mean(x),sd=sd(x),var=var(x))





x=c(1,3,2,5,2)

if (sum(x)>=5) {
    ('sum(x) is greater than 5')
} else if (sum(x)<5) {
        ('sum(x) is less than 5')
} else if (sum(x)==5) {
        ('sum(x) is equal to 5')
}


y=ifelse(x>3,x-3,x)
y


i=1
switch(i,x+y,x-y,x*y)

if (i==1){
    (x+y)
} else if (i==2) {
   (x-y)
} else {
   (x*y)
}


score=65

ifelse (score>=90,'A',
ifelse(score>=75,'B',
ifelse(score>=50,'C','D')))




type='sqrt';'square';'log'
if (type=='squrt'){
    print(sqrt(score))
} else if (type=='square') {
   print(score**2)
} else if (type=='log') {
   print(log(score))
}


type='log'
switch(type,sqrt=sqrt(score),square=score**2,log=log(score))


