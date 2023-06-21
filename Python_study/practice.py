class fourcla:

    def setdata(self,first,second):
        self.first=first
        self.second=second
        

    def add(self):
        result=self.first+self.second
        return result

a=fourcla()
a.setdata(4,5)
print(a.add())