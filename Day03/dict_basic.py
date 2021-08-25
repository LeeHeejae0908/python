
'''
* 사전(Dictionary)

- 사전은 키와 
'''

students = {'멍멍이':'김철수', '야옹이':'박영희', '짹짹이':'홍길동'}
print(type(students))
print(len(students))
print(students)

'''
- 사전에 사용되는 key값은 중복값을 가질 수 없고 변경도 안된다.
- 그러나 value값은 중복을 허용하며 데이터를 자유롭게 편집할 수도 있다.
- 사전 내부에 저장된 데이터를 검색할 때는 인덱스 대신
key를 사용한다.(시퀀스 자료가 아니다.)
'''
print(students['멍멍이'])
print(students['야옹이'])
print(students['짹짹이'])
# print(students['메롱이'])(x)

#in 키워드를 사용하여 key의 존재유무를 알 수 있다.
print('멍멍이' in students)
print('메롱이' in students)