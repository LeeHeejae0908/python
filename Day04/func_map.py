
'''
* 내장함수 map

-map()은 첫번째 인수로 자료형을 지정하고, 두번째 인수로 
리스트를 지정하면 해당 리스트 내부 요소값을 일괄적으로
첫번째 인수로 지정한 타입으로 변경한 데이터를 반환한다
'''
# 3개의 숫자중 최대 값을 판별하여 리턴하는 함수를 정의
def max_of_three(n1, n2, n3):
    if n1 > n2:
        if n1> n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:
            return n3

# n1 = int(input('정수1: '))
# n2 = int(input('정수2: '))
# n3 = int(input('정수3: '))

n1, n2, n3 = map(int, input('정수 3개를 공백으로 구분해서 입력하세요: ').split())

print('최대값: ',max_of_three(n1, n2, n3))

def multi_triple(number):
    return number**3

# multi_triple(2)
# multi_triple(4)
# multi_triple(6)
# multi_triple(8)
# multi_triple(10)

li = [2,4,6,8,10]

# map(함수, 리스트)-> 리스트 내부 요소를 함수로 전달
# 여러개의 데이터를 한번에 다른 형태로 변환하기 위해 사용
#map(int, li) -> list내부의 모든 데이터를 int()로 전달

#li안에 있는 데이터들을 모두 multi_triple 함수로 잔달해서
#값을 변환하기 위해 사용
result = list(map(multi_triple, li))
print(result)