

from selenium import webdriver
import time
#뷰티풀 수프 임포트
from bs4 import BeautifulSoup
import traceback
import codecs
from datetime import datetime

'''
*표준 모듈 codecs

- 웹이나 다른 프로그램의 텍스트 데이터와
파이썬 내부의 텍스트 데이터의 인코딩 방식이 서로 다를 경우
내장함수 open()이 제대로 인코딩을 적용할 수가 없어서
에러가 발생한다.(UnicodeEncoderError)

- 파일 입출력시 인코딩 코덱을 변경하고 싶다면
codecs모듈을 사용한다.
'''

d = datetime.today()
file_path = f'F:/test/알라딘 1~400위_{d.year}_{d.month}_{d.day}기준.txt'

'''
# with문을 사용하면 with 블록을 벗어나는 순간
객체가 자동으로 해제된다(자바의try with resource와 비슷)
# with 작성시 사용할 객체의 이름을 as 뒤에 작성한다.
'''
    
with codecs.open(file_path, mode='w', encoding='utf-8') as f:

    #웹 드라이버 활성화 및 알라딘 홈페이지 이동
    driver = chrome_option = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:/Users/user/Desktop/JAVA_Web/python/crawling/chromedriver.exe', chrome_options=chrome_option)
    driver.get('http://www.aladin.co.kr')
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

    rank = 1
    for n in range(2,10):
        driver.find_element_by_xpath(f'//*[@id="newbg_body"]/div[3]/ul/li[{n}]').click()

        src = driver.page_source

        soup = BeautifulSoup(src, 'html.parser')

            
        div_list = soup.find_all('div', class_='ss_book_box')


        for div in div_list:
            book_info = div.find_all('li')
            if book_info[0].text[0] != '[':
                book_title = book_info[0].text
                book_author = book_info[1].text
                book_price = book_info[2].text
            else:
                book_title = book_info[1].text
                book_author = book_info[2].text
                book_price = book_info[3].text

            auth_info = book_author.split('|')

            f.write(f'#순위: {rank}위 \n')
            f.write('# 제목: ' + book_title +'\n')
            f.write('# 작가: ' + auth_info[0] + '\n')
            f.write('# 출판사: ' + auth_info[1] + '\n')
            f.write('#출판일: ' + auth_info[2] +'\n')
            f.write('# 가격: ' + book_price +'\n')
            f.write('-'*40 + '\n')
            rank +=1

