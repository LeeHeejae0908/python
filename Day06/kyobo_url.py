
from selenium import webdriver
import time
#뷰티풀 수프 임포트
from bs4 import BeautifulSoup
import traceback
import codecs
from datetime import datetime


d = datetime.today()
file_path = f'F:/test/교보문고 1~20위_{d.year}_{d.month}_{d.day}기준.html'

with codecs.open(file_path, 'w', encoding='utf-8') as f:

    driver = chrome_option = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:/Users/user/Desktop/JAVA_Web/python/crawling/chromedriver.exe', chrome_options=chrome_option)
    driver.get('http://www.kyobobook.co.kr')
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="header"]/div[3]/ul[2]/li[1]/a').click()

    src = driver.page_source

    soup = BeautifulSoup(src, 'html.parser')

    div_list = soup.find_all('div', class_='detail')

    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n')
    f.write('<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Document</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')

    rank = 1
    for n in div_list:
        book_info = n.find_all('div', class_='title')
        book_title = book_info[0]
         

        f.write(f'순위: {rank} <br>')
        f.write(f'<a>{book_title}<a/>')
        f.write('<hr>')
        rank += 1
    
    f.write('</body>\n')
    f.write('</html>\n')
