#---------------------------------------------------------------------------
# 예외 처리(exception handling)
# 실행중 발생되는 오류로 프로그램이 중단되는 것을 막아주기 위한 방법
#---------------------------------------------------------------------------
num1=10
try:
    num2=int(input('숫자입력'))
    print(f'{num1}/{num2}={num1/num2}')

except Exception as e :
    print(f'error : {e}')

finally:
    print(f'항상 실행')
# except ZeroDivisionError as e:
#     print('error : ', e)
#     #pass    # 오류 무시

# except ValueError as e2:
#     print('error : ', e2)

print("end---------------------------------------------------")

FILE='a.txt'

try:
    fp=open(FILE, mode='w',encoding='utf-8')
    fp.write(12345)     # 일부러 str입력
except FileExistsError as e:
    print('이미 존재하는 파일입니다.')
except FileNotFoundError as e:
    print('존재하지 않는 파일입니다.')
except Exception as e:
    print('오류발생 : ', e)
finally:
    if fp: fp.close()
    print("파일닫기")



