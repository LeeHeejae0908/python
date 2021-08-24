
'''
* 문자열 공백제거 메서드
1. lstrip(): 문자열의 왼쪽 공백만 제거
2. rstrip(): 문자열의 오른쪽 공백만 제거
3. strip(): 문자열의 양쪽 공백만 제거
'''

user_id = input('아이디: ')
print(user_id + '님 안녕하세요')
print(user_id.lstrip() + '님 안녕하세요')
print(user_id.rstrip() + '님 안녕하세요')
print(user_id.strip() + '님 안녕하세요')