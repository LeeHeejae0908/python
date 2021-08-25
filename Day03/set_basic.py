
'''
*집합 (set)

- 집합은 여러 값들의 모임이며, 저장순서가 보장되지 않고
중복값의 저장을 허용하지 않는다

- 집합은 사전과 마찬가지로 {}로 표현하지만 , key:value
쌍이 아닌 데이터가 하나씩 들어간다는 점이 사전과 다르다

- set()함수는 공집합을 만들기도 하며, 다른 컬렉션 자료를
집합 형태로 변환할 수도 있다.
'''

#[] list(), tuple(), {} dict(), set()

names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names))
print(names)

for x in names:
    if x == '박영희':
        print(x)
        break

#내장함수 set()
s = set()
print(type(s))
print(s)

s1 = 'programming'
print(set(s1))
print(list(s1))
print(tuple(s1))

'''
- 집합은 변경 가능한 자료여서 언제든지 데이터를 편집할 수 있다

- 집합에 요소를 추가할 땐 add()메서드를 사용하고
제거할때는 remove()를 사용한다
'''

asia = {'korea', 'china', 'japan'}
print(asia)
asia.add('china')
asia.add('thailand')
asia.remove('japan')

#집합의 결합은 update()메서드를 사용한다
asia2 = {'singapore', 'indonesia', 'korea'}
# print(asia + asia2)(X)
asia.update(asia2)
print(asia)