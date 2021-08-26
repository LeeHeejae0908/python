
# import math
# print(math.factorial(6))
from math import factorial, gcd

print(factorial(6))
print(factorial(5))

print(gcd(12,18))

#임포트할 모듈을 별칭을 지정해서 사용하기
import statistics as st

li = [34, 55, 12, 33, 55, 66, 99]
print('평균: ', st.mean(li))
print('분산: ', st.variance(li))
print('표준편차: ', st.stdev(li))

#위에서 알려준 두가지 개념을 합쳐서도 사용이 가능하다
from math import factorial as fac

print(fac(10))