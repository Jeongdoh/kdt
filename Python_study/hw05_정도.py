# 1. 테니스 공 넣기 (클래스로 구현)
# 테니스 공 케이스에는 최대 5개의 테니스 공을 넣을 수 있음 (1차원 배열 사용).
# 파이썬에서 제공하는 pop() 함수는 사용할 수 없음.
# 1~4번 이외의 메뉴를 선택한 경우 "잘못된 메뉴 선택입니다." 출력함


# 메뉴 구성 (무한 반복: 4번 입력시 프로그램 종료)
# 1. 테니스 공 넣기 함수 구현 (push 함수 구현)
# - 숫자를 1부터 증가시키면서 추가함
# - 공을 넣고 top은 증가함
# - 화면에 현재 케이스의 상황을 출력함 (3번 함수 호출)
# - 공을 더 넣을 공간이 없는 경우(케이스의 최대 용량 이상) "케이스가 꽉 찼습니다." 출력


# 2. 테니스 공 꺼내기 함수 구현 (pop 함수 구현)
# - 테니스 공 케이스에서 하나씩 꺼내고 top은 감소함
# - 화면에 현재 케이스의 상황을 출력함 (3번 함수 호출)
# - 테니스 공 케이스에 공의 개수가 0개 이면(top==-1) "케이스가 비어있습니다." 출력


# 3. 테니스 공 개수 출력
# - 현재 케이스에 남아 있는 공의 개수 출력
# - 위에서 부터(top부터) 공의 정보 출력: 5 4 3 2 1 순서로 출력


# 4. 종료
# - 4번을 입력하면 프로그램 종료

class ball:     # 클래스 ball 생성

    #케이스, 탑 숫자 생성자 함수에 넣어줌
    def __init__(self): 
        self.case=[]
        self.top=0
        return self.start()
    
    #시작하면 메뉴출력되면서 입력받아 해당되는 메뉴가 출력되게 만듦
    def start(self):
        while 1:
            print('-'*30)
            print("메뉴")
            print('-'*30)
            print("1번 : 공넣기")
            print("2번 : 공 꺼내기")
            print("3번 : 공 개수")
            print("4번 : 종료")
            print('-'*30)

            # 메뉴에 해당하는 입력받아옴
            self.menu=int(input("메뉴에 해당하는 숫자를 입력하세요").strip())
            
            # 메뉴1번에 해당하는 푸쉬함수 호출
            if self.menu==1:
                return self.push()

            # 메뉴2번에 해당하는 풀함수 호출
            elif self.menu==2:
                return self.pull()

            #메뉴3번에 해당하는 인벤토리함수 호출
            elif self.menu==3:
                return self.inventory()
            
            #메뉴4번 종료.
            elif self.menu==4:
                print("프로그램 종료")
                break
            
            # 1~4메뉴 외 입력하면 잘못된 입력이라고 출력
            else:
                print("잘못된 입력입니다.")
                return self.start()
    # 푸쉬함수 탑에 +1씩 해주면서 케이스 리스트에 어펜드, 그리고 다시 메뉴화면 출력
    def push(self):
        if len(self.case)==5:
            print("케이스가 꽉 찼습니다.")
            return self.start()

        self.top+=1
        self.case.append(self.top)
        return self.inventory() # 3번 현재상황 함수 호출

    # 케이스에서 빼주는 함수, 케이스 끝에서부터 빼줘야함, 0이되면 케이스가 비었다고 알려주고 다시 메뉴로 돌아감 
    def pull(self):
        if len(self.case)==0:
            print("케이스가 비었습니다.")
            return self.start()

        self.top-=1
        del self.case[-1]
        return self.inventory() # 3번 현재상황 함수 호출


    # 현 케이스 상황을 알려주는 함수, 끝에서부터 5,4,3,2,1 형식으로 빼주기위해 [::-1]해줌
    def inventory(self):
        print(f"{self.case[::-1]}")
        return self.start() # 



# 문제점 1. numpy array로 문제를 풀지못함.
# 문제점 2. 공 꺼내기하고 나면 케이스가 비었다고 해야하는데 이상하게 출력됨.
# 문제점 3. 숫자형을 입력하면 else처리되지만 문자형을 입력하면 에러 출력...아마 int로 입력받아서 그런 것 같음..

myBall=ball()
