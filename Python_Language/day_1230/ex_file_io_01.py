#-------------------------------------------------------------------------------
#파일 입력과 출력 (I/O)
#스트림(Stream): - 흐름, 데이터의 흐름
#               - 종류 : 입력 스트림, 출력 스트림
#-------------------------------------------------------------------------------
# with ~ as 구문
# - close 기능을 자동으로 실행
#-------------------------------------------------------------------------------
FILE_NAME='new_year.txt'


#파일 쓰기(wirte)=====================================================
#mode - w :덮어쓰기
#     - a :추가
#     - x :이미 존재하는 파일 있으면 오류발생, 없을때만 생성해서 씀
#====================================================================
with open(FILE_NAME, mode='w', encoding='utf-8')as f:
    f.write("새해 복 많이 받으세요~~~2023 검은 토끼")



#파일 읽기(read)=======================================================
#mode - r : 읽기
#======================================================================
with open(FILE_NAME, mode='r', encoding='utf-8')as f:
    print(f.read())


# 파일 복사(copy)=======================================================
# 조건 : 파일명 끝부분에 숫자 추가
# 예시 : data.txt => data_1.txt, data_2.txt, ....
#======================================================================

def copyFile(filename):
    # 파일명 만들기
    _filename = filename.replace('.txt', '_1.txt')
    print(f'_filename : {_filename}')

    #파일 읽어서 새 파일에 쓰기 

    # 방법1
    # with open(filename, mode='r', encoding='utf-8')as f:
    #     data=f.read()
    
    # with open(_filename,mode='w', encoding='utf-8')as f:
    #     f.write(data)


    # 방법 2
    with open(filename, mode='r', encoding='utf-8')as f1:
        with open(_filename, mode='w', encoding='utf-8')as f2:
            f2.write(f1.read())
    
    
    _filename2=_filename.replace('_1.', '_2.')
    with open(filename, mode='r', encoding='utf-8')as f1:
        with open(_filename, mode='w', encoding='utf-8')as f2:
            lines=f1.readlines()
            for idx in range(1, len(lines)+1):
                f2.write(f'[{idx}]'+lines[idx-1])

            
            



copyFile(FILE_NAME)








# def my(*args):
#     my_copy = args[0]

#     if my_copy == "copy":
#         f = open("1.txt", "rt")
#         g = open("2.txt", "wt")
#         while True:
#             text = f.read(1)
#             g.write(text)
#             if len(text) == 0:
#                 break
#         f.close()
#         g.close()

# my("copy")



