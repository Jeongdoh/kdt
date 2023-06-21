# -----------------------------------------------
# dict 데이터 타입 전용 메서드
# -----------------------------------------------
jumsu={'kor':[98,99,78], 'art':[100,92,99]}

# 키만 알고 싶어요~ 메서드=> dict.keys() ---------
# 키만 보여주는 형식으로 view 객체
jumsuKeys=jumsu.keys()

print(f'type : {type(jumsuKeys)}, {jumsuKeys}')
#print(f'jumsuKeys[0] => {jumsuKeys[0] }')


# 값만 알고 싶어요~ 메서드=> dict.values() ---------
jumsuValues=jumsu.values()
print(f'type : {type(jumsuValues)}, {jumsuValues}')

# 키-값을 묶어서 보여주는 메서드=> dict.items() -----
# (카, 값) 튜플로 묶어줌 
jumsuItems=jumsu.items()
print(f'type : {type(jumsuItems)}, {jumsuItems}')

# 과목별 최고점수, 최저점수, 합계 알고 싶어요~
# jumsu={'kor':[98,99,78], 'art':[100,92,99]}

# (1) 국어과목의 최고점수/최저점수/합계
korJumsu=jumsu['kor']
print(f'korJumsu : {korJumsu}')

print(f'합계 : {sum(korJumsu)},최고 : {max(korJumsu)}, 최저 : {min(korJumsu)}')

# (2) 아트과목의 최고점수/최저점수/합계
artJumsu=jumsu['art']
print(f'artJumsu : {artJumsu}')

print(f'합계 : {sum(artJumsu)},최고 : {max(artJumsu)}, 최저 : {min(artJumsu)}')
