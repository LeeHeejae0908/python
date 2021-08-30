
from selenium import webdriver
import time
#뷰티풀 수프 임포트
from bs4 import BeautifulSoup

#웹 드라이버 활성화 및 알라딘 홈페이지 이동
driver = chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/user/Desktop/JAVA_Web/python/crawling/chromedriver.exe', chrome_options=chrome_option)
driver.get('http://www.aladin.co.kr')
time.sleep(1)

#베스트셀러 탭 클릭
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

#selenium으로 현재 페이지의 html 소스코드를 전부 불러오기.
src = driver.page_source
# print(src) 모든 html소스를 가져온 것을 확인.

#뷰티풀 수프 객체 생성.
#뷰티풀 수프 객체를 생성하면서, 셀레늄이 가지고 온 html소스를
#제공하고, 해다 ㅇ소스를 html문법으로 변환하라는 주문
soup = BeautifulSoup(src, 'html.parser')

'''
- 뷰티풀수프를 사용하여 수집하고 싶은 데이터가 들어있는
태그를 부분 추출 할 수 있다.

- find_all() 메서드는 인수값으로 추출하고자 하는 태그의
이름을 적으면 해당 태그만 전부 추출하여 리스트에 담아서 대입한다.
'''

div_list = soup.find_all('div', class_='ss_book_box')
# print('div_list에 들어있는 데이터 수: ', len(div_list))
# print(div_list[0])# 1위 책만 가져온다.

first_book = div_list[0].find_all('li')
# print(first_book) -> li안에 필요한 텍스트가 다 있다.

#text는 태그를 제외한 사용자가 실제로 브라우저에서 확인 가능한
#텍스트만을 추출하여 문자열 형태로 반환
book_title = first_book[0].text
book_author = first_book[1].text
book_price = first_book[2].text

auth_info = book_author.split('|')

print('# 제목: ', book_title)
print('# 작가: ', auth_info[0])
print('# 출판사: ', auth_info[1])
print('#출판일: ', auth_info[2])
print('# 가격: ', book_price)

