#-----------------------------------------------------------------------------
#- 객체지향언어  ---> 정보은닉(캡술화)
#- 속성/필드    --->  비공개 private
#- 메서드       --->  비공개 private    ==>     공개가능한것만 공개 public
#-----------------------------------------------------------------------------
# bmi 지수 => 키와 몸무게로 계산
#-----------------------------------------------------------------------------
class A:

    #속성 2개 가지는 클래스
    #self는 클래스안에서 만 사용가능
    def __init__(self,weight, height, bmi):
        self.__weight=weight    #비공개: 클래스 안에서는 어디든지 사용, 객체변수명으로는 사용불가
        self.__height=height    #비공개
        self.bmi=bmi            #공개: 클래스, 객체변수명으로 사용가능

    #비공개 속성을 제어할 수 있는 메서드-----------------------------------------------
    #비공개 속성의 값을 읽을 수 있는 메서드 => get속성명()
    #비공개 속성의 값을 변경 할 수 있는 메서드 => set속성명()
    def setweight(self,weight):
        self.__weight=weight

    def getweight(self):
        return self.__weight


    # bmi 계산 값 설정하는 메서드
    # bmi= weight/(height/100)*(height/100)
    def __calcBmi(self):
        self.bmi=self.__weight/((self.__height/100)*(self.__height/100))

    #정보제공 메서드
    def showInfo(self):

        self.__calcBmi()

        print(f' 몸무게 {self.__weight}')
        print(f' 키 {self.__height}')
        print(f' bmi {self.bmi}')

    #몸무게 증감 처리 메서드
    def diet(self,value):
        self.__weight=self.__weight+value
        # 이렇게 써도 됨
        # if value>0:
        #     self.__weight=self.__weight+value
        # else:
        #     self.__weight=self.__weight-value




# 인스턴스 (즉 객체) 생성-----------------------------------------
# 변수=클래스명()
me=A(177.5 , 85, '')

# 인스턴스 속성 확인 ==> 변수명.속성명
print('me.bmi => ', me.bmi)
print('me.weight => ', me.getweight())
me.showInfo()

