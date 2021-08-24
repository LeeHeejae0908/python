
'''
* 리스트의 내부 요소 다루기

- 리스트는 시퀀스 자료형이기 때문에 인덱스를 통한
요소들의 관리가 가능하다
- 리스트를 다룰 때는 문자열과 비슷한 방식을 사용한다.
'''

pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플']

print(pokemon[2])
print(pokemon[1][2])
print(pokemon[4][:2])

#리스트 슬라이싱 -> 리스트 데이터[begin:end:step]

nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[2:5:1])
print(nums[:4])
print(nums[1:7:2])