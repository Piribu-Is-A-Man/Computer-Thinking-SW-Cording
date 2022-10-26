try:
    print(10*(30/0))
except(ZeroDivisionError):
    print('0으론 나눌수 없습니다')

try:
    x=int(input('정수 x를 입력하세요: '))
except(ValueError):
    print('올바른 정수값을 입력해주세요')

try:
    import sys
    
    f=open('myfile.txt')
    s=f.readLine()
except Exception as e:
    print('error :',e)