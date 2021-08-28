
'''
* 다중 예외 처리

- 하나의 try 블록에서 여러 상황의 예외를 예외별로 다르게
처리하고 싶다면 다중 예외처리를 사용합니다.

- 다중 예외처리를 할 때는 except 뒤에 발생하는 예외의
이름을 적어줍니다.

# 자주 발생하는 예외의 이름
1. NameError: 정의되지 않은 변수나 함수, 클래스를
사용할 때 발생합니다.

2. ValueError: 주로 형 변환시 발생하며, 내부 값의 형태가
잘못되었을 때 발생합니다.

3. ZeroDivisionError: 숫자를 0으로 나누었을 때 발생합니다.

4. IndexError, KeyError: 존재하지 않는 인덱스나 키를 사용하여
시퀀스, 딕셔너리를 조회했을 때 발생합니다.

5. TypeError: 연산 수행 시 피연산자의 데이터 타입이 올바르지
않을 경우 발생합니다.
'''
# NameError
# print(apple)
# insert(10)

#ValueError
# int('3.14')

# Index, KeyError
s = 'hello'
# print(s[6])
d = {}
# print(d['멍멍이']) (x)

# TypeError
# print(10 ** '메롱')

s = input('정수: ')

try:
    point = int(s) # ValueError 가능성
    print(150 / point) # ZeroDivisionError 가능성
    print(s[point]) # IndexError 가능성

except ValueError:
    print('정수로만 입력하세요!')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱스 범위를 벗어났습니다!')

'''
* finally 키워드는 예외 발생 여부와 상관없이
항상 실행해야 하는 코드가 있을 경우 사용하는 예외처리 방식입니다.
'''

pets = ['거북이', '강아지', '고양이']

for x in range(4):
    try:
        print(pets[x], '키우고 싶다~')
    except:
        print('애완동물의 정보가 없습니다.')
    finally:
        print('아무튼 출력되는 문장입니다.')
        print('-' * 40)

