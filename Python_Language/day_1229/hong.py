class saveDate:

    def __init__(self):
        pass

    def add(x, y):
        FILE_NAME = "history.txt"
        fp = open(FILE_NAME, mode='a', encoding='utf-8')
        fp.write(str(x))
        fp.write("+")
        fp.write(str(y))
        fp.write(" = ")
        fp.write(str(x+y))
        fp.write("\n")
        fp.close()
        return x+y

    def sub(x, y):
        FILE_NAME = "history.txt"
        fp = open(FILE_NAME, mode='a', encoding='utf-8')
        fp.write(str(x))
        fp.write("-")
        fp.write(str(y))
        fp.write(" = ")
        fp.write(str(x-y))
        fp.write("\n")
        fp.close()
        return x-y

    def mul(x, y):
        FILE_NAME = "history.txt"
        fp = open(FILE_NAME, mode='a', encoding='utf-8')
        fp.write(str(x))
        fp.write("*")
        fp.write(str(y))
        fp.write(" = ")
        fp.write(str(x*y))
        fp.write("\n")
        fp.close()
        return x * y

    def div(x, y):
        FILE_NAME = "history.txt"
        fp = open(FILE_NAME, mode='a', encoding='utf-8')
        fp.write(str(x))
        fp.write("/")
        fp.write(str(y))
        fp.write(" = ")
        fp.write(str(x/y))
        fp.write("\n")
        fp.close()

        return x/y

    oper = 1
    num = []
    while oper != "=":
        if len(num) >= 1:  # 연산되는 부분
            num1 = int(input("데이터를 입력해주세요.").strip())
            if oper == "+":
                num[0] = add(num[0], num1)
                print(num[0])
            elif oper == '-':
                num[0] = sub(num[0], num1)
                print(num[0])
            elif oper == '*':
                num[0] = mul(num[0], num1)
                print(num[0])
            elif oper == '/':
                if num1 == 0:
                    print("0으로 나눌 수 없습니다")
                    break
                else:
                    num[0] = div(num[0], num1)
                    print(num[0])

            elif oper == "=":
                print(f'결과값 : {num[0]}')
                break
            oper = input("연산자를 입력해주세요.").strip()
        else:
            num1 = int(input("데이터를 입력해주세요.").strip())
            oper = input("연산자를 입력해주세요.").strip()
            num.append(num1)

    print(f'결과값 {num[0]}')
    FILE_NAME = "history.txt"
    fp = open(FILE_NAME, mode='a', encoding='utf-8')
    fp.write("결과값 :  ")
    fp.write(str(num[0]))
    fp.write("\n")
    fp.close()