# 이상치 체크 기능 함수-------------------------------------
# 과제 => 여러개

# IQR 방법으로 이상치 찾기
find_outliers <- function(data, coef=1.5) {
  q1 <- quantile(data, 0.25)
  q3 <- quantile(data, 0.75)
  iqr <- q3 - q1
  lower <- q1 - coef*iqr
  upper <- q3 + coef*iqr
  outliers <- data[data < lower | data > upper]
  return(outliers)
}

# 예제 데이터
#x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100)

# 이상치 찾기
find_outliers(data)
# [1] 100

# IQR (Interquartile Range) 방법.
# IQR은 데이터의 중간값을 중심으로 데이터를 4분위로 나누어서,
# 1사분위와 3사분위 사이의 범위를 계산하는 방법.
# 이 방법에서 이상치는 범위를 벗어나는 값으로 정의됨.
# 예를 들어, IQR 방법에서는 아래와 같이 이상치를 찾을 수 있음.






# Z-score 방법으로 이상치 찾기
find_outliers_zscore <- function(data, threshold=2.5) {
  z <- abs(scale(data))
  outliers <- data[z > threshold]
  return(outliers)
}

# 예제 데이터
#x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100)

# 이상치 찾기
find_outliers_zscore(data)
# [1] 100

# Z-score 방법은 데이터의 평균과 표준편차를 사용하여 이상치를 정의하는 방법.
# 이상치는 일반적으로 Z-score가 2.5 이상이거나 -2.5 이하인 값으로 정의.
# Z-score가 크다는 것은 해당 데이터가 다른 데이터들과 크게 다른 값을 가진다는 것을 의미함.





# DBSCAN 방법으로 이상치 찾기
library(dbscan)

find_outliers_dbscan <- function(data, eps=1, minPts=3) {
  dbscan_obj <- dbscan(scale(data), eps=eps, minPts=minPts)
  outliers <- data[dbscan_obj$cluster==-1]
  return(outliers)
}

# 예제 데이터
#x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100)

# 이상치 찾기
find_outliers_dbscan(data)
# [1] 100

# DBSCAN (Density-Based Spatial Clustering of Applications with Noise) 방법은 
# 데이터를 밀도 기반으로 클러스터링하여 이상치를 찾는 방법. 

# DBSCAN은 데이터의 밀도가 높은 지역을 클러스터로 인식하고, 그렇지 않은 지점들은 이상치로 판단. 
# DBSCAN 방법은 클러스터링 알고리즘으로, 비정상적으로 밀도가 낮은 데이터들을 노이즈로 판단.