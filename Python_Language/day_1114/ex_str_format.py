# --------------------------------------------------
# 문자열 포맷팅 => 문자열에 형식지정
# - 방법1) %연산자 포맷팅  " %d %f %s " %(v1, v2, v3)
# - 방법2) f포맷팅        f" {v1} {v2}"
# - 방법3) fromat메서드   " {}  {} ".format(v1, v2)
# - 포맷기호 => 공백정렬칸수 (예: *^10, *>10.3)
# --------------------------------------------------

# 문자열 포맷팅에서 %기호 사용법 ---------------------
msg="내년에 경제성장률이 %.1f%%입니다." %1.4

msg1=f"내년에 경제성장률이 {1.4321:10}%입니다."

msg2="내년에 경제성장률이 {:10}%입니다.".format(1.432)

print(msg)
print(msg1)
print(msg2)


# format() 메서드 ------------------------------------
year=2022
month=11
day=14

msg="오늘은{}년{}월{}일입니다.".format(year, month, day)
msg1="오늘은{0}년{1}월{2}일입니다.".format(year, month, day)
msg2="오늘은{2}년{0}월{1}일입니다.".format(year, month, day)
msg3="오늘은{y}년{m}월{d}일입니다.".format(d=day, y=year, m=month)
msg4="오늘은{}년{m}월{}일입니다.".format(year,day, m=month)
msg5="오늘은{:10}년{}월{}일입니다.".format(year, month, day)
msg6="오늘은{:*<10}년{:-^10}월{:%>10}일입니다.".format(year, month, day)
print(msg)
print(msg5)
print(msg6)







