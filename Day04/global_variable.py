
'''
* 전역 변수(global variable)

- 지역변수가 함수 내부에서만 사용하는 변수라면
전역변수는 프로그램 전체에서 사용하는 공용 변수입니다.

- 파이썬에서는 들여쓰기 없이 선언된 변수를 전역변수로 
취급하며, 전역변수는 함수 내부, 제어문 내부 등
프로그램 어디에서나 사용이 가능하다
'''
sale_rate = 0.2 #전역변수

def calc_price(price):
    print(f'오늘의 할인율: {sale_rate*100}%')

    today_price = price - (price * sale_rate)
    print(f'오늘의 가격: {today_price}')
    print('-'*40)

calc_price(2000)
print(sale_rate)
# print(today_price)(X)