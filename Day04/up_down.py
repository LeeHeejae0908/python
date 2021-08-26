
import random as r

correct = r.randint(1,100)
cnt = 0

while True:
    answer = int(input('1~100사이의 수를 입력하세요: '))
    if answer == correct:
        print('정답입니다.')
        cnt += 1
        print(cnt,'회')
        break
    elif answer > correct:
        print('DOWN')
        cnt += 1
    else:
        print('UP')
        cnt += 1