# 마방진의 행의 길이를 입력
n = int(input("홀수차 배열의 크기를 입력하세요: "))

# n*n 크기의 빈 배열 생성
arr = [[0]*n for i in range(n)]

r = 0
c = n//2

# 맨윗행 중간열에 1 배치
arr[r][c] = 1

# 2부터 n*n까지 배치.
for i in range(2, n*n+1):

    # 위치가 비어있을때
    if arr[n-1 if r-1<0 else r-1][0 if c+1>n-1 else c+1] == 0:
        r = n-1 if r-1<0 else r-1
        c = 0 if c+1>n-1 else c+1
        arr[r][c] = i

    # 위치가 차있을때
    else:
        r = 0 if r+1>n-1 else r+1
        arr[r][c] = i

for l in arr:
    print(*l)
