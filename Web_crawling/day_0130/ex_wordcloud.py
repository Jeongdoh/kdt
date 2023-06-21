#Okt 간단 예제 #1
from konlpy.tag import Okt
okt = Okt()	# Open Korean Text (과거 트위터 형태소 분석기)
text = "마음에 꽂힌 칼한자루 보다 마음에 꽂힌 꽃한송이가 더 아파서 잠이 오지 않는다"
# pos(text): 문장의 각 품사를 태깅
# norm=True: 문장을 정규화,	stem=True:	어간을 추출
okt_tags = okt.pos(text, norm=True, stem=True)
print(okt_tags)
# nouns(text): 명사만 리턴
okt_nouns = okt.nouns(text)
print(okt_nouns)


#Okt 예제 #2
from konlpy.tag import Okt
text = '나랏말이 중국과 달라 한자와 서로 통하지 아니하므로,	\
우매한 백성들이 말하고 싶은 것이 있어도 마침내 제 뜻을 잘 표현하지 못하는 사람이 많다.\
내 이를 딱하게 여기어 새로 스물여덟 자를 만들었으니,	\
사람들로 하여금 쉬 익히어 날마다 쓰는 데 편하게 할 뿐이다.'
okt = Okt()
# morphs(text):	텍스트를 형태소 단위로 나눔
okt_morphs = okt.morphs(text)
print('morphs():\n', okt_morphs)
#	명사만 추출
okt_nouns =	okt.nouns(text)
print('nouns():\n',	okt_nouns)
#	phrases(text): 어절 추출
okt_phrases = okt.phrases(text)
print('phrases():\n', okt_phrases)
#	pos(text): 품사를 태깅
okt_pos = okt.pos(text)
print('pos():\n', okt_pos)



#예제: 단어 분석 및 Word Cloud 생성 #1
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as	plt
import platform
text = open('test.txt',	encoding='utf-8').read()
okt = Okt()	# Open Korean Text 객체 생성
#	okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag =	[]
sentences_tag =	okt.pos(text)
noun_adj_list =	[]
#	tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for	word, tag in sentences_tag:
    if	tag	in ['Noun' , 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)
# 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(40)
print(tags)


#예제: 단어 분석 및 Word Cloud 생성 #2
#	WordCloud를 생성
#	한글을 분석하기위해 font를 한글로 지정해주어야 된다.	
#	macOS는 .otf ,	window는 .ttf 파일의 위치를 지정 (ex.	'/Font/GodoM.otf')
if	platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':	# Mac OS
    path = r'/System/Library/Fonts/AppleGothic'
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



#네이버 뉴스 타이틀 Word Cloud 예제 #1
from	bs4	import	BeautifulSoup
import	requests
from	konlpy.tag import	Okt
from	collections	import	Counter
from	wordcloud import	WordCloud
import	matplotlib.pyplot as	plt
import	time
import	re
import	platform

def	get_titles(start_num, end_num, search_word, title_list):
#	start_num ~	end_num까지 크롤링
    while	1:
        if	start_num >	end_num:
            break							
        url =	'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(search_word,	start_num)								
        req	=	requests.get(url)
        time.sleep(1)

        if	req.ok:
            soup	=	BeautifulSoup(req.text,	'html.parser')								
            #	뉴스제목 뽑아오기
            list_news =	soup.find('ul',	{'class' : 'list_news'})
            #li_list =	list_news.find_all('li', {'id':	re.compile('sp_nws.*')})
            li_bxs = list_news.find_all('li', {'class': 'bx'})
            for	li_bx in li_bxs:
                news_title = li_bx.find('a', {'class':'news_tit'})																
                title_list.append(news_title['title'])
        start_num += 10
    print(title_list)


#네이버 뉴스 타이틀 Word Cloud 예제 #2
def	make_wordcloud(word_count,	title_list):
    okt =	Okt()
    sentences_tag =	[]
    #	형태소 분석하여 리스트에 넣기
    for	sentence	in	title_list:
        morph	=	okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-'	*	30)

    print(sentences_tag)
    print('\n'	*	3)

    noun_adj_list =	[]
    #	명사와 형용사만 구분하여 이스트에 넣기
    for	sentence1	in	sentences_tag:
        for	word,	tag	in	sentence1:
            if	tag	in	['Noun', 'Adjective']:
                noun_adj_list.append(word)
    #	형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print(tags)


#네이버 뉴스 타이틀 Word Cloud 예제 #3
#	wordCloud생성
#	한글꺠지는 문제 해결하기위해 font_path 지정
    if	platform.system()	==	'Windows':
        path	=	r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system()	==	'Darwin':		#	Mac	OS
        path	=	r'/System/Library/Fonts/AppleGothic'
    else:
        path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    wc =	WordCloud(font_path=path,	background_color='white',	width=800,	height=600)
    print(dict(tags))
    cloud	=	wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10,	8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()
if	__name__	==	'__main__':
    search_word =	"빅데이터"		#	검색어 지정
    title_list =	[]
    #	1~200번게시글 까지 크롤링
    get_titles(1,	20,	search_word,	title_list)
    #	단어 30개까지 wordcloud로 출력
    make_wordcloud(20,	title_list)














