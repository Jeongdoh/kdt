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