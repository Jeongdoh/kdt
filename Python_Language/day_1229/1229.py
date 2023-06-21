class Calculator:
   
    def __init__(self):
        pass

    def add(self):
        result = self.first + self.second
        print(result)

    def sub(self):
        result = self.first - self.second
        print(result)

    def mul(self):
        result = self.first * self.second
        print(result)

    def div(self):
        result = self.first / self.second
        print(result)




    while True:

        # switch = 1
        first = []
        second = []

        a = (input("(1) 숫자를 입력하세요. : "))
        

        if len(a)>1:
            for num1 in a:
                first.append(int(num1))
                pass


        cal = input("(2)계산 방식을 입력하세요. : ")

        if cal == "+":
            b = (input("(2) 숫자를 입력하세요. : "))
            second.append(int(b))
            print(add)
            break
        elif cal == "-":
            b = (input("(2) 숫자를 입력하세요. : "))
            second.append(int(b))
            print(sub)
            break
        elif cal == "*":
            b = (input("(2) 숫자를 입력하세요. : "))
            second.append(int(b))
            print(mul)
            break
        elif cal == "/":
            b = (input("(2) 숫자를 입력하세요. : "))
            second.append(int(b))
            print(div)
            break