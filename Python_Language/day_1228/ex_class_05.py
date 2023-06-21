#---------------------------------------------------------------
#(1) 어떤 클래스            ==> 클래스 클래스명
#(2) 특징/성격/외형/속성     ==> 변수(attribute), 필드(field)
#(3) 기능/역할/행동         ==>클래스 전용 함수 메서드(Method)
#---------------------------------------------------------------
# 휴대폰 클래스
#---------------------------------------------------------------
# 전화
# 앱, 배터리, 번호, 문자보내기, 브랜드 제조사
# 사진, 음악, 네비게이션, 날씨,
# 웹서핑하다 전화 사진찍다
# 폴더 형태 크기
#---------------------------------------------------------------
class phone:
    # 인스턴스 속성 생성 및 초기화
    def __init__(self, maker, number, color):
        print(' __init__() ')
        self.maker=maker
        self.color=color
        self.number=number

    # 인스턴스 메서드
    def calling(self, phoneNumber):
        print(f'{phoneNumber}에 전화를 겁니다.')

    def mms(self, message):
        print(f'{self.number}가 {message}를 전송합니다. ')


#클래스로 인스턴스 즉 객체 생성-----------------------------------
#클래스명() 생성자 메서드(constructor method)
#메모리 힙에 객체 생성

# myphone=phone()


# create object, create phone instance------------------------
# variable=classname()
myphone=phone('samsung','010-2222-3333','pink')

hisphone=phone('samsung','010-1111-3456','black')


shephone=phone('samsung','010-2355-2345','white')

momphone=phone('samsung','010-5647-6786','blue')
momphone.color='red'
momphone.number='010-6235-9875'