def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def calc_sum(end):
    sum = 0
    for n in range(end):
        sum += n
    return sum

def info():
    print('모듈 임포트 연습')

inch = 2.54
yard = 0.91
lb = 0.45

'''
- 배포의 목적으로 만든 모듈이라면
테스트 코드를 작성해서 다른 사용자들에게
모듈 사용법을 간단히 알려주면 좋다

처음부터 import를 목적으로 설계된 모듈의 테스트 코드 작성시에는
다음과 같은 문법 하에서 테스트를 실행한다.

ex) if __name__ == '__main__':
        test code..

- __name__ 이라는 숨겨진 변수에는
현재 실행중인 모듈의 이름이 저장되게 되는데, 
현재 모듈에서 실행할 때는 이름이 main으로 저장된다.
다른 모듈에서 실행할 때는 이름이 모듈 이름으로 저장된다.
'''
print('__name__: ', __name__)# 현재모듈에서는 main
# 다른 모듈에서실행 -> calculator

if __name__ == '__main__':
    print('1~100까지 누적합: ',calc_sum(100))
    info()
    print(sub(100, 15))
    print('이렇게쓰세요')