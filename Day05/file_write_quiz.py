'''
* 사용자의 입력을 파일(***.txt)에 저장하는 프로그램을 작성
(단 , 프로그램을 다시 실행하더라도 파일명이 동일하다면
기존 작성한 내용을 그대로 유지하고
새로 입력된 내용이 추가되어야 한다.
파일명도 마지막에 입력받아서 작성)
'''
'''
while True:
    text = input('>')
    
    break
if text == '그만':
        
    fileName = input('파일명을 입력: ')
    
    try:
        file_path = 'F:/test/',fileName,'.txt'
        f = open(file_path, 'a')
        f.write(text)
        print('파일저장 성공')
        
    except:
        print('파일 저장 실패')
    finally:
        f.close
'''
print('저장할 내용을 입력(\'그만\'이라고 입력시 종료)')
user_input = ''
while True:
    temp = input('>')
    if temp == '그만':
        break
    user_input += temp + '\n'
f_name = input('파일명을 입력: ')
f_path = f'F:/test/{f_name}.txt'

try:
    f = open(f_path, 'a')
    f.write(user_input)
    print('파일저장 성공')
except:
    print('파일저장 실패')
finally:
    f.close
