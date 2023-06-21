#외부데이터 파일 로딩--------------------------------
popdata<-read.csv("day_0214/data/2010_population.csv", header = F)

popdata
#데이터 확인------------------------------------------------------
# (1) 구조 및 정보 출력 -> str()
str(popdata)

# (2)행과 컬럼 갯수 출력 -> dim()
dim(popdata)


# (3) 행 갯수 & 컬럼 갯수 출력 -> 행 갯수 : nrow(), 컬럼 갯수 : ncol()
nrow(popdata); ncol(popdata)

# (4-1)컬럼명 출력 -> colnames()
colnames(popdata)


# (4-2)컬럼명 지정 -> colnames()=
colnames(popdata)=c("성별","연령","가구주관계","교육","남아출생수","여아출생수")
head(popdata)



