'''
*points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt.라는 파일에 
쓰는 프로그램을 작성
'''
import traceback as trace

file_path = 'F:/test/points.txt'
result_path = 'F:/test/result.txt'
total = 0
avg = 0
try:
    f = open(file_path, 'r')
    text = f.readline().split(' ') 
    print(text)
    for n in text:
        print(n)
        points = [int(n)]
        
        for p in points:
            total += p
            avg = total/10
    print(total, avg)
    
   
except:
    print('파일 로드 실패')
    print(trace.format_exc())
finally:
    f.close
        

try:
    f = open(result_path, 'a')
    text = f'총점: {total}, 평균: {avg}'
    f.write(text)
    print('파일 저장 성공')
except:
    print('파일저장 실패')
    print(trace.format_exc())
finally:
    f.close