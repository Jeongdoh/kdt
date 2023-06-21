import pandas as pd
from	wordcloud import	WordCloud
from	konlpy.tag import	Okt
from	collections	import	Counter
import	matplotlib.pyplot as	plt
import	platform
from konlpy.tag import Okt


word_list=[]

# 1번 농업 빅데이터 활용 사례
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('농업 빅데이터 활용 사례')
search_box.submit() # 검색어를 전달

#목표url설정 (빅데이터와 인공지능 활용..디지털농업 혁명이 시작됐다.)
target1 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target1
target1[2].click()
print('-' * 20)

#	find_elements_by_class_name('클래스이름'):	해당 클래스 이름을 모두 검색
gisa1 = driver.find_elements_by_class_name('news_detail')

list1=[]
for	idx in	gisa1:
    print(idx.text)
    a=idx.text.replace('\n','').replace('\n\n','').replace('\t','').split(' ')
    for i in a:
        list1.append(i)
        for j in list1:
            if j != ' ':
                word_list.append(j)
driver.back()


# 2번 농업 빅데이터 활용 사례
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('농업 빅데이터 활용 사례')
search_box.submit() #	검색어를 전달

#목표url설정 (빅데이터로 알아보는 디지털농업)
target2 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target2
target2[4].click()
print('-' * 20)

list2=[]
gisa2 = driver.find_elements_by_class_name('ctsType1')
for	idx in	gisa2:
    print(idx.text)
    b=idx.text.replace('\n','').replace('\n\n','').replace('\t','').split(' ')
    for i in b:
        list2.append(i)
        for j in list2:
            if j != ' ':
                word_list.append(j)
driver.back()




#기사 3번 농업 빅데이터 활용 사례
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('농업 빅데이터 활용 사례')
search_box.submit() #	검색어를 전달

#목표url설정 (미래를 꿈꾸는 스마트 농업’, 빅데이터 농업활용서 시작)
target3 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target3
target3[0].click()
print('-' * 20)

list3=[]
gisa3 = driver.find_elements_by_id('article-view-content-div')
for	idx in	gisa3:
    print(idx.text)
    c=idx.text.replace('\n','').replace('\n\n','').replace('\t','').split(' ')
    for i in c:
        list3.append(i)
        for j in list3:
            if j != ' ':
                word_list.append(j)
driver.back()





#기사 4번 클라이밋 코퍼레이션
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('클라이밋 코퍼레이션')
search_box.submit() #	검색어를 전달

#목표url설정 (디지털 농업분야의 선두주자, 클라이밋 코퍼레이션)
target4 = driver.find_element_by_class_name('iUh30.qLRx3b.tjvcx')
target4
target4.click()
print('-' * 20)

list4=[]
gisa4 = driver.find_elements_by_id('article-view-content-div')
for	idx in	gisa4:
    print(idx.text)
    d=idx.text.replace('\n','').replace('\n\n','').replace('\t','').split(' ')
    for i in d:
        list4.append(i)
        for j in list4:
            if j != ' ':
                word_list.append(j)
driver.back()


#기사 5번 스마트팜 최적환경설정 안내서비스
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('--')
search_box.submit() #	검색어를 전달

#목표url설정 ([K-농업기술] 스마트팜 최적환경 알려주는 똑똑한 서비스)
target5 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target5
target5[2].click()
print('-' * 20)

list5=[]
gisa5 = driver.find_elements_by_class_name('article_content')
for	idx in	gisa5:
    print(idx.text)
    e=idx.text.replace('\n','').replace('\n\n','').replace('\t','').split(' ')
    for i in e:
        list5.append(i)
        for j in list5:
            if j != ' ':
                word_list.append(j)
driver.back()

print(word_list)





#csv 파일 만드는 방법
farm_wordCloud = pd.DataFrame(word_list)
farm_wordCloud.to_csv('./farm_wordCloud.csv', encoding='utf-8', mode='w', index=True)


# text = open('farm_wordCloud.csv', encoding='utf-8').read()




okt = Okt()	# Open Korean Text 객체 생성
#	okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag =	[]
noun_adj_list =	[]
for i in word_list:
    a=okt.pos(i)
    for	word, tag in a:
        if	tag	in ['Noun']:
            if word not in ['것','등','수']:
                noun_adj_list.append(word)
len(noun_adj_list)

# # 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(40)
print(tags)


#예제: 단어 분석 및 Word Cloud 생성 #2
#	WordCloud를 생성
#	한글을 분석하기위해 font를 한글로 지정해주어야 된다.	
#	macOS는 .otf ,	window는 .ttf 파일의 위치를 지정 (ex.	'/Font/GodoM.otf')
if	platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

wc = WordCloud(font_path=path,	background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

# 생성된 WordCloud를 test.jpg로 보낸다.
#cloud.to_file('test.jpg')

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

print(len(noun_adj_list))