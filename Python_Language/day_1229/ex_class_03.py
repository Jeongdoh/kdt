#---------------------------------------------------------------------
#상속 
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#   선생님을 나타내는 데이터 타입 => 클래스
# - 속성/ 필드
# 교과서, 시험
# - 메서드
# 가르치다
# 시험을 출제하다
#---------------------------------------------------------------------
class Teach:

    school='영진고'

    def __init__(self,book,test):
        self.book=book
        self.test=test

    def teaching(self,subject=''):
        self.subject=subject
        print(f'{self.book}책으로 {self.subject}를 가르치고 {self.test}를 시험문제를 낸다')

    def collectTest(self,colT=''):
        self.colT=colT
        print(f'{self.book}책으로 {self.colT}를 만든다')

a1=Teach('국사','고조선 역사')
a1.teaching('단군신화')
a1.colT('국사문제')






#---------------------------------------------------------------------
#   학생을 나타내는 데이터 타입 => 클래스
# - 속성/ 필드
# 교과서, 시험
# - 메서드
# 공부하다
# 놀다
# 시험을 친다
#---------------------------------------------------------------------
class student(Teach):

    def __init__(self, book, test):
        super().__init__(book, test)


    def teaching(self,subject=''):
        self.subject=subject
        print(f'{self.book}책으로 {self.subject}를 배우고 {self.test}를 시험봤다')

    def collectTest(self,colT=''):
        self.colT=colT







#---------------------------------------------------------------------
#상속 
#---------------------------------------------------------------------
class person:

    def __init__(self,school,cr,name,age,grade):
        self.school=school
        self.cr=cr
        self.name=name
        self.age=age
        self.grade=grade

    def printInfo(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'학교 : {self.school}')
        print(f'학년 : {self.grade}')
        print(f'반 : {self.cr}')


#---------------------------------------------------------------------
#   선생님을 나타내는 데이터 타입 => 클래스
# - 속성/ 필드
# 이름, 성별, 나이, 과목, 클래스 
# - 메서드
# 가르치다
#---------------------------------------------------------------------
class Teacher(person):

    def __init__(self,name,gender,age,subject,cr,school,grade):
        super().__init__(school,cr,name,age,grade)
        self.gender=gender
        self.subject=subject


    def teaching(self):
        print(f'{self.gender}성별의 {self.name}선생님이 {self.cr}반에서 {self.subject}과목을 수업하신다')






#---------------------------------------------------------------------
#   학생을 나타내는 데이터 타입 => 클래스
# - 속성/ 필드
# 학교, 학년, 반, 이름, 나이
# - 메서드
# 공부하다
# 시험을 친다
#---------------------------------------------------------------------

class Student:

    def __init__(self,school,grade,cr,name,age):
        super().__init__(school,cr,name,age,grade)
        self.school=school
        self.grade=grade
        self.cr=cr
        self.name=name
        self.age=age

    def study(self,subject):
        print(f'{self.name}가 {subject}과목을 공부하고 있다..')
