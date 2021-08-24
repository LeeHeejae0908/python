
ssn = input('주민등록번호를 입력하세요: ')
# 921013-1234567


year = int(ssn[:2])
month = ssn[2:4]
day = ssn[4:6]

print('주민등록번호 앞자리: ', ssn[:6])
print('주민등록번호 뒷자리: ', ssn[7:])

gender = ''
if ssn[7]=='1' or ssn[7] == '3':
        gender = '남자'
elif ssn[7] == '2' or ssn[7] == '4':
        gender = '여자'

by = 0
if ssn[7] == '1' or ssn[7] == '2':
        by = 1900 + year
else:
        by = 2000 + year

age = 2021-by
print(f'{by}년 {month}월 {day}일 {age}세 {gender} ')