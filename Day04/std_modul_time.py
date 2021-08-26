
'''
*표준 모듈 time

-time 모듈은 시간 관련 기능들을 제공한다

- 대표적인 함수는 time()인데, 이 함수는 현재 시간을 
1970년 1월1일 자정을 기준으로 현재까지 경과한
시간을 초 단위로 표현한 유닉스 시간을 반환한다.
'''

import time
print(time.time())

# time함수를 이용한 프로그램 속도 측정 테스트

start = time.time()

sum= 0
for n in range(5000000):
    sum += n
end = time.time()
print(f'프로그램 실행 속도: {end-start:0.4f}초')

'''
- time 모듈의 sleep()함수는 cpu를 지정한 시간만큼
잠재워 아무것도 하지 않고 시간을 끌게 한다.
'''
# time.sleep(5)
