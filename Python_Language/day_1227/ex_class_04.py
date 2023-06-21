# ----------------------------------------------------------------------
# 사람데이터 타입 ==> 동사무소에서 우리 동네 주민 관리 프로그램
# 속성/성질/외모... ==> Jumin
# - 이름
# - 성별
# - 생년월일        비공개
# - 주소            비공개
# - 나이            비공개
# - 전화번호        비공개
# - 주민번호        비공개
# - 생애주기
#
# 기능/역할/행동...
# - 필수 정보확인
# - 기본정보 확인
# ----------------------------------------------------------------------
class Jumin:
    # 클래스 변수 - 모든 인스턴스 함께 사용--------------------------------
    __DONG='행복동'                 # 비공개, 하지만 클래스 내에서는 사용 가능

    #생성자 메서드
    def __init__(self, name, birth, gender, addr, age, phone, juminNum, lifeCycle):
        self.name=name
        self.__birth=birth
        self.gender=gender
        self.__addr=addr
        self.__age=age
        self.__phone=phone
        self.__juminNum=juminNum
        self.lifeCycle=lifeCycle


    # Get/Set 메서드 => 비공개 속성 접근 여부 메서드
    # 전화번호, 주소는 변경될 수 있음 => set메서드 필요
    def set__phone(self,phone):
        self.__phone=phone

    def set__addr(self,addr):
        self.__addr=addr


    # 비공개 메서드

    # 일반 메서드=> 인스턴스 메서드
    def allInfo(self):
        print(f'-----[개인정보 상세]-----')
        print(f'-이 름 : {self.name}')
        print(f'-주 소 : {self.__addr}')
        print(f'-주 민 번 호 : {self.__juminNum}')


    def allInfo(self):
        print(f'-----[개인정보]-----')
        print(f'-이 름 : {self.name}')
        print(f'-성 별 : {self.gender}')
        print(f'-생 애 주 기 : {self.lifeCycle}')


a=Jumin('서하윤','2020년01월30일','남','의정부',2,'010-1111-2222','200130-4025685','유아기')
a.allInfo()
