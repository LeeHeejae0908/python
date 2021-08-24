
'''
* 정수형 (Integer)
- 수치형 타입 중 정수형(int)는 양수, 음수의 정수값을 표현
소수점 이하 자리는 표현할 수 없다.

- 다른 언어는 저장 범위가 타입마다 정해져 있지만
파이썬은 메모리가 허용하는 한 무수히 많은 정수를 저장할 수 있다.
'''

num = -4321
print(type(num))

#2진수 (0b), 8진수(0o), 16wlstn(0x)를
#접두어로 붙여서 표현이 가능하다.
a=0b1011
b = 0o77
c = 0xAC00

# 정수를 다른 진법으로 변경하려면
# 2진수 변환함수bin(), 8진수 oct(), 16진수 hex()
print(bin(33))
print(oct(0b111001)) #2진수->8진수
print(hex(8923))