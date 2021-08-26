
# for~ else 문을 이용한 범위  안의 모든 소수 출력\
#for문 내부에서 중간에 반복문의 종료없이 지정된 범위까지
#모두 반복이 된 후에 else문이 실행되는 구조
#존재유무 등 논리값을 통해서 확인하던 문제를
#for ~ else 문을 통해 확인하는 것이 가능하다(flag)

n1, n2 = map(int, input('정수 2개를 입력하세요').split())

if n1> n2:
    n1, n2 = n2, n1




 
cnt = 0# 소수의 개수를 저장할 변수
for i in range(n1, n2+1):
    for j in range(2,1):
        if i % j ==0:
            flag = True
            break
    else: # for 문에서 break가 한번도 동작하지 않으면 else문이 실행됨
        print(i, end=' ')
        cnt += 1

print('소수의 개수: ', cnt,'개')