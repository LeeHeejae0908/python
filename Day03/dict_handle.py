
'''
* 사전 내부 데이터 관리

- 사전은 변경 가능한 자료형이어서 실행 중에 데이터의
추가, 삭제, 수정 등의 편집을 자유롭게 진행할 수 있다.
'''

#데이터 추가(append처럼 동작)
#사전 내부에 존재하지 않는 키를 사용하여 데이터를 대입하면
#데이터가 key:value 로 사전에 저장된다.
eng_kor = {'studend':'학생', 'apple':'사과', 'book':'책'}

eng_kor['banana'] = '바나나'
print(eng_kor)

'''
* 사전의 데이터를 수정하기
- 사전 내부에 이미 존재하는 key를 사용하여 새로운 데이터를
대입하면 해당 key값에 맵핑되어있는 value가 수정된다.
'''
eng_kor['book'] = '서적'
print(eng_kor)

'''
-사전의 key목록과 value목록을 따로따로 추출하고 싶다면
사전의 메서드 keys(), values()를 사용한다
'''
print('-'*40)
print(eng_kor.keys())
print(eng_kor.values())

#사전의 반복문 처리
# for in 뒤에 사전 데이터를 적으면 key만 반복순회한다.
for k in eng_kor:
    print(k, ':', eng_kor[k])

'''
* 사전의 데이터 삭제(내장함수 del)
del(사전이름[key])
key를 입력하면 같이 맵핑된 value값도 함께 삭제된다.
'''
del(eng_kor['studend'])
print(eng_kor)

#빈 사전 만들기
d = {}
d2 = dict()