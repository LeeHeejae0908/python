
'''
* 예외 일부러 발생시키기

- 프로그래밍을 진행하다보면 일부러 예외를 발생시켜서
코드의 흐름을 전환해야 하는 경우가 발생한다

- 파이썬은 raise라는 명령을 사용해서 오류를 강제로 
발생시킬 수 있다.
'''
def calc_sum(end):
    if end <=0:
        raise ValueError

    total = 0
    for n in range(1, end+1):
        total += n
    return total

try:
    result = calc_sum(100)
    print(result)

    result2 = calc_sum(-120)
    print(result2)
except:
    print('매개값은 양수')