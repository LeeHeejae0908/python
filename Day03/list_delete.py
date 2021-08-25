
'''
* 리스트 내부 요소 삭제

1. remove(): 삭제할 값을 직접 지정하여 삭제
2. 내장함수 del(): 삭제할 요소의 인덱스를 통해 삭제
3. clear(): 리스트 내부요소 전체 삭제
'''

points = [88,99,56,92,100,78]

points.remove(92)
print(points)

del(points[2])
print(points)

points.clear()
print(points)

pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플']

delpo = input('삭제할 포켓몬을 입력하세요: ')

#remove
# pokemon.remove(delpo)

#del
for idx in range(5):
    if delpo == pokemon[idx]:
        del(pokemon[idx])
        break



print(pokemon)

