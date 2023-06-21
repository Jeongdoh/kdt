#-----------------------------------------------------------------------------------
# 다중상속 살펴보기
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class A:

    def __init__(self, aa):
        print('A.__init__()')
        self.aa=aa
        
    def play(self):
        print(f'A.play() - {self.aa}하며 놀고있다.')

class B:

    def __init__(self, bb):
        print('B.__init__()')
        self.bb=bb
        # self.number=number

    def play(self):
        print(f'B.play() - {self.bb} 신나 신나')


class C(A,B):

    pass


class D(B, A):
    pass


class E(C):
    pass



# c1=C('영화')
# c1.play()


# d1=D('게임')
# d1.play()


d2=E('aaa')
d2.play()