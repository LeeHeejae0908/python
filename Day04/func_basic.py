
'''
* 함수 (function)

- 함수는 지속적으로 사용되는 코드블록에 이름을 붙여놓은 형태

- 함수는 한번 정의해 두면 지정된 함수 이름을 통해 
언제든지 해당 코드블록을 실행할 수 있다.

- 함수를 정의할 때는 def라는 키워드를 사용한다

- 정의해 놓은 함수를 사용하는 것을 호출(call)이라고 한다

- 파이썬에서는 함수를 호출하려면 반드시 호출문보다 상단부에
함수를 먼저 정의해야 한다.
'''
# 함수의 정의(1~x까지의 누적합을 구하는 로직0)
def calc_sum(x): 
    sum = 0
    for n in range(1, x+1):
        sum += n
    return sum

# 함수의 호출

print('1부터 100까지의 누적합: ', calc_sum(100))

'''

매개체 역할을 하며, 그렇기 때문에 매개변수(parameter)
'''

def calc_rangesum(x, y):
    if(x > y):
        x,y = y,x
    sum = 0
    for n in range(x, y+1):
        sum += n
    return sum

x = int(input('x: '))
y = int(input('y: '))

print(calc_rangesum(x,y))

'''
* 반환값(return value)

- 반환값이란 함수를 호출한 곳으로 함수의 최종 실행 결과를
전달하는 값

- 인수는 여러개 존재할 수 있지만, 반환값은 언제나
하나만 존재해야한다.

- 모든 함수가 반환값이 있는 것은 아니다
함수 실행 후에 딱히 반환할 값이 없다면 return을 생략할 수 있다.
'''

def add(n1, n2):
    return n1 + n2

result = add(10,5) # result = 15
print(add(add(5,7), add(9,8))) #add(12,17)

# n = int(input('정수: ')) -> n = int('3')

#만약 여러 개의 값을 한번에 return해야 할 때는
#컬렉션 자료형을 사용한다(list, tuple, set)

def operate_all(n1, n2):
    return n1 + n2, n1-n2, n1*n2, n1/n2 #tuple

print(type(operate_all(10,5)))

def multi(n1, n2):
    result = n1 * n2
    print(f'{n1} X {n2} = {n1*n2}')

# abc = multi(9,6)
# print(abc)