
'''
*키워드 인수(keyword argument)

- 인수의 개수가 많아지면 인수의 순서를 파악하기 어렵고
함수를 호출할 때 전달할 값의 위치를 헷갈릴 가능성이 높아진다.


-파이썬에서는 순서와 무관하게 인수를 전달할 수 있는 방법을 제공하여 인수의 이름을 직접 지정하여 값을 전달하는
 키워드 인수 방식을 사용한다.
'''
def calc_stepsum(begin, end, step):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum
# 일반적인 함수 호출(위치인수 -> positional argumnet)
calc_stepsum(3,7,1)

#키워드 인수 사용(순서 상관x)
calc_stepsum(end=7, step=1 , begin=3)

print(calc_stepsum(end=7, step=1, begin=3))
print(calc_stepsum(step=1, begin=3, end=7))

#위치인수와 키워드 인수의 혼합 사용
print(calc_stepsum(3, step=1, end=7))
# print(calc_stepsum(end=7, 3, 1))(X)
# print(calc_stepsum(3,1,end=7))(X)
# print(calc_stepsum(3, end=7, 1))(X)

print(3,6,9, sep='->', end='!')
# print(sep='->', end='!', 3,6,9)(X)