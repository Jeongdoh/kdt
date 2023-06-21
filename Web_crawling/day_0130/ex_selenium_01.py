# from selenium import webdriver
# from time import sleep	

# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://www.google.com')
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)	#	HTML	소스 가져오기
# driver.implicitly_wait(time_to_wait=5)
# driver.close() #	하나의 탭만 종료
# driver.quit()




# from selenium import webdriver

# driver = webdriver.Chrome('chromedriver.exe')
# #driver	= webdriver.Chrome('C:\\workspace\\chromedriver')

# driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
# driver.implicitly_wait(5)

# # find_element_by_class_name('클래스이름'):	하나의 클래스 이름 검색
# name = driver.find_element_by_class_name('green')
# print(name.text)

# print('-' * 20)
# # find_elements_by_class_name('클래스이름'):	해당 클래스 이름을 모두 검색
# nameList = driver.find_elements_by_class_name('green')
# for	name in nameList:
#     print(name.text)

# driver.quit()


# #네이버 로그인
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://nid.naver.com/nidlogin.login')
# driver.implicitly_wait(3)

# #	id,	비밀번호 전달
# #	<input>의 이름이 id를 검색
# driver.find_element_by_name('id').send_keys('y2kjd')
# driver.find_element_by_name('pw').send_keys('cookiejd14!^^')
# driver.find_element_by_xpath('//*[@id="log.login"]').click()



# #Selenium API #3: 구글 검색어 입력 예제
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://google.com')
# driver.implicitly_wait(3)
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('빅데이터')
# search_box.submit()  # 검색어를 전달


# #프레임 이동 예제
# from bs4 import	BeautifulSoup #	크롤링을 하기 위해
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')# 본인의 webdriver 경로
# driver.get('https://blog.naver.com/swf1004/221631056531')
# driver.switch_to.frame('mainFrame')	# 해당 iframe으로 이동

# html = driver.page_source #페이지 소스를 html 변수에 저장
# soup = BeautifulSoup(html,	'html.parser') # beutifulsoup과 연동
# whole_border =	soup.find('div',	{'id':	'whole-border'})
# results	= whole_border.find_all('div', {'class': 'se-module'})
# result1=[]
# for	result	in	results:
#     print(result.text.replace('\n',	''))
#     result1.append(result.text)



# #커피빈 코리아 홈페이지 자동 실행
# from bs4 import	BeautifulSoup
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://www.coffeebeankorea.com/store/store.asp')
# driver.execute_script('storePop2(1)')
# #함수 호출 결과 페이지를 별도로 저장 후 BeautifulSoup과 연동
# html = driver.page_source #	page_source: 해당 웹페이지의 소스가 저장됨
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) # HTML 소스를 보기 좋게 출력



# #예제 코드1: #1
# from	bs4	import	BeautifulSoup
# from	selenium	import	webdriver
# driver	=	webdriver.Chrome('chromedriver.exe')
# driver.get('https://www.coffeebeankorea.com/store/store.asp')
# driver.execute_script('storePop2(1)')
# #	현재의 html	소스를 저장
# html = driver.page_source
# soup = BeautifulSoup(html,	'html.parser')
# #print(soup.prettify())	# HTML 소스를 보기 좋게 출력
# store_names = soup.select('div.store_txt >	p.name >	span')
# store_name_list =	[]
# for	name in store_names:
#     store_name_list.append(name.get_text())

# print('매장 개수: ', len(store_name_list))
# print(store_name_list)

# store_addresses =	soup.select('p.address >	span')
# store_address_list =	[]

# for	addr in	store_addresses:
#     print(addr.get_text())
# driver.quit()	#	web	driver	종료


# #자바스크립트 실행
# for	i in range(1, 380):
#     driver.get(coffeebean_url)
#     time.sleep(1)	#	웹페이지를 연결할 동안 1초 대기
#     driver.execute_script('storePop2(%d)' % i)	#	각 지점의 번호를 전달
#     time.sleep(1)


# #지점 정보 가져오기
# soup	=	BeautifulSoup(html,	'html.parser')
# #	매장 이름 검색
# store_name =	soup.select_one('div.store_txt >	h2').text
# print('매장이름:	',	store_name)
# store_info =	soup.select("div.store_txt >	table.store_table >	tbody >	tr	>	td")
# store_address_list =	list(store_info[2])
# store_addr =	store_address_list[0]	#	매장 주소
# store_phone =	store_info[3].text	#	매장 전화번호


#동적 웹페이지 크롤링 예제 코드 #1
from bs4 import	BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
def	coffeebean_store(store_list):
    coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome('chromedriver.exe')

    for	i in range(1, 380):
        driver.get(coffeebean_url)
        time.sleep(1) #	웹페이지를 연결할 동안 1초 대기
        driver.execute_script('storePop2(%d)'	%	i)
        time.sleep(1)
        try:
            html = driver.page_source
            soup = BeautifulSoup(html,	'html.parser')
            store_name =	soup.select_one('div.store_txt >	h2').text	#	매장 이름
            store_info =	soup.select("div.store_txt >	table.store_table >	tbody >	tr	>	td")
            store_address_list =	list(store_info[2])
            store_addr =	store_address_list[0]	#	매장 주소
            store_phone =	store_info[3].text	#	매장 전화번호
            print('{}	{}  {}	{}'.format(i+1,	store_name,	store_addr,	store_phone))
            store_list.append([store_name,	store_addr,	store_phone])
        except:
            continue

#동적 웹페이지 크롤링 예제 코드 #4
def	main():
    store_info = []
    coffeebean_store(store_info)
    #	DataFrame으로 변경
    coffeebean_table =	pd.DataFrame(store_info, columns=('매장이름',	'주소',	'전화번호'))
    print(coffeebean_table.head())
    #	DataFrame을 csv파일로 저장 (utf-8로 인코딩)
    coffeebean_table.to_csv('coffeebean_branches.csv', encoding='utf-8',	mode='w',	index=True)
main()
