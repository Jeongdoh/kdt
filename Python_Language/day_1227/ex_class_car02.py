#----------------------------------------------------------------
#클래스명 : Car
#   클래스 변수 -Car 클래스의 모든 인스턴스가 공유하는 변수
#             maker
#   인스턴스 변수 - 인스턴스마다 가지는 속성
#         name, model, color, price,food, number
#  시스템 메서드
#       __init__() : 인스턴스 생성시 속성 저장
#   메서드
#       def drive()
#       def eat()
#       def changeDir()
#----------------------------------------------------------------
class Car:
    Maker='HD'

    #생성자 메서드 -시스템에서 자동 호출, 즉 callback
    def __init__(self,name,model,color,price,food,wheel,number):
        # 인스턴스 변수들/속성들,필드들
        self.name=name
        self.model=model
        self.color=color
        self.price=price
        self.food=food
        self.wheel=wheel
        self.number=number

# 소멸자 메서드 - 시스템에서 자동으로 호출 즉 callback
# def __del__(self):
#     pass


    #메서드----------------------------------------------------------------------
    def drive(self,loc):
        print(f'{self.number} 자동차가 {loc}달리고 있다.')

    def eat(self):
        print(f'{self.number} 자동차가 {self.food}보충 중이다.')

    def changeDir(self,dir):
        print(f'{self.color} 자동차가 {dir}보충 중이다.')

    def displayInfo(self):
        print(f'번호 : {self.number}')
        print(f'모델 : {self.model}')
        print(f'브랜드 : {self.Maker}')


#------------------------------------------------------------------------------------
#인스턴스와 클래스
#------------------------------------------------------------------------------------
myCar=Car('소나타','승용차','블랙',34000,'휘발유',4,'12가1212')

print(myCar.Maker,Car.Maker)

print('myCar.__dict__:', myCar.__dict__) # 인스턴스의 현재 속성값--> 속성 : 값
print('myCar.__class__:', myCar.__class__) # 인스턴스를 생성한 클래스 정보


for item in Car.__dict__.items():
    print(item)

# print('Car.__dict__:', Car.__dict__)    #


