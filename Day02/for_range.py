
'''
* 내장함수 range()

- 순차적으로 증가하는 정수의 자료형을 만들 때
대괄호 안에 데이터들을 콤마로 일일이 나열하는 것은
한계가 있기 때문에, range함수를 사용하여 보다 쉽게 순차형 반복 범외를 생성할 수 있다.

ex) range(begin, end, step)
begin은 값이 포함되지만(이상), end는 갑이 포함되지 않는다.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

list2 = list(range(1, 11, 1))
print(list2)





num = int(input('정수1: '))
count = 0 #소수의 개수를 기억할 변수

for n in range(1, num+1): #end미만이니까 +1
    cnt = 0 #나누어떨어진 횟수
    for i in range(1,n+1):
        if n % i ==0:
            cnt +=1
    #for문 끝나고 나서
    if cnt == 2:
        count +=1
        print(n, end=' ') 

print('\n 소수들의 개수: ', count, '개')       