# ------------------------------------------
# 함수와 변수 관계
# 함수는 클래스 입니다.!!!
# ------------------------------------------
def addTwo(a,b):
    return a+b

# 함수의 타입 -------------------------------
print( type(addTwo) , type(len) )

myfunc=addTwo

print(myfunc(3,4), addTwo(3,4))
print(id(myfunc), id(addTwo))