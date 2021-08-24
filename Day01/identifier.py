
'''
*식별자(identifier)

1.식별자: 사용자 정의로 데이터에 이름을 붙인 것.
2. 모듈, 패키지, 변수, 함수, 클래스 등의 이름을 식별자 라고 한다.
3. 식별자 이름은 중복해서 지정할 수 없다.

'''


# 식별자 이름을 숫자로 지정하거나 숫자로 시작하면 안된다.
# 7= 777(x)
# 7number = 7(x)

number7 = 7
num7ber = 7

# 식별자 이름에 공백 포함 안됨
#my birth day = 19940908(x)
my_birth_day = 19940908

#키워드를 식별자로 지정할 수 없다.(if, while)
#if = '만약에(x)

If = '만약에' #별로

#print()와 같은 내장함수의 이름을 식별자로 사용할 수는 있다.
# 더이상 함수의 기능을 사용할 수 없다.
print = '출력하다'
# print(print)(X)

#한글 한자 등 영어 이외의 문자도 가능하긴 하지만
#사용을 권장하지 않음
야옹이='고양이' #별로
print(야옹이)