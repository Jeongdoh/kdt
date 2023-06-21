#-----------------------------------------------------------
#   덕 타이핑(Duck Typing)
# - 동적 타이핑(Dynamic Typing) : 데이터가 저장되어야 타입이 결정됨
# - 동적 타이핑 방식 중 하나
#   객체의 속성과 메서드를 보고 동일 타입 여부 결정
#-----------------------------------------------------------
class A:
    # 클래스 속성
    LOC = '대구'



    # 인스턴스 즉 객체 생성 및 초기화
    def __init__(self,num):
        self.num=num


    # 인스턴스 메서드 즉 객체 메서드
    def play(self, item):
        print(f'{item}하며 놀고있다. ')


class B:
    # 클래스 속성
    LOC = '부산'



    # 인스턴스 즉 객체 생성 및 초기화
    def __init__(self,num):
        self.num=num


    # 인스턴스 메서드 즉 객체 메서드
    def movie(self, item):
        print(f'{item}아바타2 존잼이에요 ')



class C:

    # 인스턴스 즉 객체 생성 및 초기화
    def __init__(self,num):
        self.num=num


    # 인스턴스 메서드 즉 객체 메서드
    def movie(self, item):
        print(f'{item}아바타2 재미있어요. ')


# 함수들---------------------------------------------------------------
def printMsg(obj):
    print(f'{obj.LOC} 출력합니다. ')

def doingNow(obj):
    obj.movie('아바타')


# 객체생성 및 사용
aa=A(2022)
bb=B(2023)
cc=C(2025)

# 다른 타입의 인스턴스 즉, 객체지만 동일한 속성이 존재하는 경루
# 동일한 함수 사용 가능
printMsg(aa)
printMsg(bb)
#printMsg(cc) 없어서 오류 발생함


# 다른 타입의 인스턴스 즉, 객체지만 동일한 메서드가 존재하는 경루
# 동일한 함수 사용 가능
#doingNow(aa)        # 없어서 오류 발생함
doingNow(bb)
doingNow(cc)