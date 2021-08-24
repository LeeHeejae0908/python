
'''
 반복문(loop)

  반복문은 
'''

#while문에 필요한 3요소: 제어변수(begin), 조건식(end) 증감식

i = 1
total = 0

while i <=10:
    total += i
    i += 1 #파이썬은 증감연산자가 없다.

print('1부터 10까지의 누적합', total)


x = int(input('정수1'))
y = int(input('정수2'))

# if x > y:
#     temp = x
#     x = y
#     y = temp

if x > y:
    x, y = y, x

z = 0

while x <= y:
    z += x
    x += 1
print(x, '부터', y,'까지의 누적합계: ', z)
