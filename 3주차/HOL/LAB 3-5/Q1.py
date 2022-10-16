speed=int(input('자동차의 속도를 입력하세요(단위 : km/h ): '))

if(speed>=100):
    print('고속')
elif(speed>=60):
    print('중속')
else:
    print('저속')