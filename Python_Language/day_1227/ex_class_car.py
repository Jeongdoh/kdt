#자동차
#브랜드
#색상
#바디
#휠
#종류


class car:
    leg=4

    def __init__(self,brand,color,body,wheel,type):
        self.brand=brand
        self.color=color
        self.body=body
        self.wheel=wheel
        self.type=type

    def engine(self, vv):
        print(f'{self.brand}는 {vv}기통이다.')


myCar=car('samsung','white','aluminum','chrome','suv')
yourCar=car('benz','black','steel','chrome','van')
dadCar=car('ssangyong','silver','aluminum','chrome','suv')

print(myCar.body,myCar.brand,myCar.color,myCar.leg)
print(yourCar.brand,yourCar.color,yourCar.type,yourCar.leg)
print(dadCar.brand,dadCar.body,dadCar.type,yourCar.leg)

myCar.engine('v3')
yourCar.engine('v6')
dadCar.engine('v6')