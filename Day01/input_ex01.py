

'''
* 표준 입력함수 input()

- 함수 괄호 안에 사용자에게 질문할 내용을 문자열 형태로 작성

- input()과 함께 항상 변수를 선언해서 입력값을 받아주어야 하며
입력받은 데이터의 타입은 str로 저장된다.
'''

nick = input('밤에 성시경이 두명이면?')
print(nick)

#입력값이 만약 정수, 실수라면
#input함수 자체를 int(), float()함수로 감싸주면 된다.
#input함수의 리턴값이 문자열이라고 했으니까, 변환함수로 변환

price= int(input('음식의 가격'))
people = int(input('사람 수:'))

print('지불할 가격: ',price*people, '원')
