
'''
- 서로 다른 정수가 담긴 두 개의 리스트를 비교하여
li 안에 있는 정수가 li2에도 담겨있다면 그 정수를 배제하라
서로 겹치지 않는 정수만 담긴 새로은 리스트를 생성해보아라
'''

li = [1,2,3,4,5,6,7]
li2 = [1,3,8,4,5,7,101]

# li3 = (set(li)|set(li2))-(set(li)&set(li2))
li3 = set(li) ^ set(li2)
li3 = list(li3)
print(li3)
