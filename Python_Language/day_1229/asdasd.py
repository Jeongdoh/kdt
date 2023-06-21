class calc:
    def start(self):
        self.ans = input("1숫자 입력: ")

        if self.ans.isdecimal(): 
            self.ans = int(self.ans)
        else: 
            self.ans = float(self.ans)

        self.fp = open("history.txt", mode='w', encoding="utf-8")

        while True:
            self.op = input("2연산자 입력: ").strip()

            if self.op == '=': 
                break
            self.num = input("3숫자 입력: ")
            self.fp.write(str(self.ans))

            if self.num.isdecimal(): 
                self.num = int(self.num)
            else: 
                self.num = float(self.num)
            oper = self.c()
        
        self.fp.close()

        self.data = open("history.txt", mode='r', encoding='utf-8')
        self.his = self.data.read()
        self.data.close()
        print(self.his)

    def c(self):
        if self.op == '+':
            self.ans += self.num
            self.fp.write(f" + {str(self.num)} = {str(self.ans)}\n")

        elif self.op == '-':
            self.ans -= self.num
            self.fp.write(f" - {str(self.num)} = {str(self.ans)}\n")

        elif self.op == '*':
            self.ans *= self.num
            self.fp.write(f" * {str(self.num)} = {str(self.ans)}\n")

        elif self.op == '/':
            if self.num != 0:
                self.ans = self.ans / self.num
                self.fp.write(f" / {str(self.num)} = {str(self.ans)}\n")
            else:
                self.fp.write("Error")

my = calc()
my.start()