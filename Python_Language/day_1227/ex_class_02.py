#---------------------------------------------------------------------------------------
# 강아지                             class Dog:
# 이름                                  name='메리'
# 성별                                  gender='여자'        속성, 필드, 멤버변수
# 몸무게  => 속성, 특징, 외형 ==> 변수    weight=3.4          (attibute, field)
# 색상                                  color='흰색'
# 앉아                                  def sit(): 코드
# 기다려                                def wait(): 코드        메서드(method)
# 짖는다   => 동사           ==> 함수    def bark(): 코드       멤버함수/메서드
# 꼬리친다                               def tale(): 코드
# :
#----------------------------------------------------------------------------------------

# 사용자 정의 클래스 ----------------------------------
class Dog:
    # Dog클래스로 생성된 모든 인스턴스가 함께 사용
    # 클래스 변수
    legs=4
    
    #생성자 메서드 : 힙 (메모리)에 생성되는 객체 초기화, 데이터 저장
    # 인스턴스 마다 고유의 속성 = 인스턴스 변수
    # 콜백함수 - 시스템에서 호출하는 함수
    def __init__(self,name,weight,color) :
        print('Dog __init__()')
        self.name=name           #'Merry'
        self.weight=weight       #3.4
        self.color=color         #'white'
        #self.legs=4             # 모든 Dog이 같은 데이터

    #사용자 메서드
    def bark(self):
        print(f'{self.name}가 짖는다.')


    def tail(self):
        print(f'{self.name}이 반갑다고 꼬리친다.')


    def eat(self, *food):
        print(f'{self.name}가 {food}를 먹는다')


# 객체생성------------------------------------------------------------------
# 변수명=클래스명()
myDog=Dog('Merry',4,'white')
kimDog=Dog('똘똘이',10,'검은색')
broDog=Dog('레오',8,'얼룩이')

#객체(인스턴스) 속성 사용-----------------------------------------------------
# 읽기 => 변수명.속성명
print(myDog.name,myDog.weight)
print('클래스 변수 사용',myDog.legs, Dog.legs)

# 값 변경
# 쓰기=> 변수명.속성명=새로운 값
myDog.weight=5.2
print(myDog.weight)

print(kimDog.weight)

#객체(인스턴스)메서드 사용----------------------------------------------------
#변수명.메서드명()
myDog.bark()

kimDog.bark()

kimDog.eat('간식')