#--------------------------------------------------------------------------------------
# 사용자 정의 클래스 / 커스텀 클래스
#--------------------------------------------------------------------------------------
# 만들고자 하는 프로젝트(프로그램) 에서 사용할 데이터를 저장하는 타입
#--------------------------------------------------------------------------------------
# 학생 정보를 저장하고 출력
#=> 학교, 이름, 학년
# school=''
# name=''
# grade=''

# school1=''
# name1=''
# grade1=''

# school2=''
# name2=''
# grade2=''



# def study(subject):
#     print(f'{subject}공부합니다')

# def test(subject):
#     print(f'{subject}공부합니다')

# def eat(food):
#     print(f'{food}공부합니다')
# ^ 이걸 하나의 데이터 타입으로 묶는 것이 클래스 => 다음에 사용이 용이하다.

class Student:
    # 클래스 변수 - 모든 인스턴스 공유
    #            - 인스턴스, 즉 객체 생성 없이 사용
    #            - 사용법 : 클래스명.클래스변수명
    school='대구중'
    name='홍길동'
    grade='1'
    schoolnum='111'
    num=0
    
    
    #인스턴스, 즉 객체 생성 및 초기화 메서드 => 생성자 메서드(constructor method)
    #새로운 메모리 공간에 생성 ==== self에 담겨있음
    def __init__(self, school, name, grade, schoolnum, num):
        self.school=school
        self.name=name
        self.grade=grade
        self.schoolnum=schoolnum
        self.num=num
        

    def play(self):
        print(self.name)
        print(Student.school)
        Student.study('미술')
        self.aa()


    def aa(self):
        pass






    # 클래스 메서드 - 인스턴스, 즉 객체 생성 없이 사용
    #              - 사용법 : 클래스명.클래스메서드명

    def study(subject):
        print(Student.school)
        print(f'{subject}공부합니다')

    def test(subject):
        print(f'{subject}공부합니다')

    def eat(food):
        print(f'{food}공부합니다')

# ==> 클래스 속성 및 메서드 사용
st1=Student('대구중', '홍길동',1,1,1)
st1.play()
st1.test('국어')
Student.test('happy')


# print(f'Student.school', Student.school)
# Student.school='제주고등학교'
# Student.study('국어')