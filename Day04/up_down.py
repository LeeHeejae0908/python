
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

'''
count = 0 # 몇 번 만에 정답을 맞췄는지를 파악할 변수
count_down = 6 # 정답 기회가 몇 번 남았는지를 파악할 변수

print('[UP & DOWN 게임 - 1~100 사이의 숫자 중 어떤 숫자가 들어있을까요?]')

while True:
    print('-' * 40)
    num = int(input('숫자를 입력하세요: '))
    count += 1
    count_down -= 1

    if num == secret:
        print(f'정답입니다!!! {count}번 만에 맞추셨네요~')
        if count_down > 0:
            print('이겼습니다!')
        else:
            print('졌습니다!')
        break
    elif num < secret:
        print('UP!!!')
    else:
        print('DOWN!!!')
    
    if count_down > 0:
        print(f'정답 기회 {count_down}번 남음!')
    else:
        print('정답 기회 모두 소진! 계속 문제를 풀어주세요.')
'''