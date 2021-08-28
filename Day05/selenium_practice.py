
'''
네이버로 접속 뉴스스탠드 쪽에 있는 파란색 '네이버 뉴스' 
클릭

상단에 있는 메뉴 중 정치, 경제, 사회, 생활/문화, 세계, IT/과학
탭을 돌아다니면서 헤드라인 뉴스 4개씩 클릭
뒤로가기는 driver.back()

XPath를 따다보면 규칙을 발견할수있다
반복문을 이용해서 클릭명령
'''
from selenium import webdriver
import time

chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/user/Desktop/JAVA_Web/python/crawling/chromedriver.exe', chrome_options=chrome_option)

#물리 드라이버로 사이트 이동명령
driver.get('https://www.naver.com')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)

for n in range(3,9):
    driver.find_element_by_xpath(f'//*[@id="lnb"]/ul/li[{n}]/a').click()
    time.sleep(1)
    if n == 3:
        for a in range(1,5):
            driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{a}]/div[1]/ul/li[1]/div/a').click()        
            time.sleep(1)
            driver.back()
           
        driver.back()
    else:
        for a in range(1,5):
            driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{a}]/div[2]/ul/li[1]/div/a').click()
            time.sleep(1)
            driver.back()
            



