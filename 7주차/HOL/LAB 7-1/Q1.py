from datetime import datetime

time=datetime.now()

print('오늘의 날짜 : {}년 {}월 {}'.format(time.year,time.month,time.day))
if(time.hour>12):
    print('현재시간 : 오후 {}시 {}분 {}초'.format(time.hour%12,time.minute,time.second))
else:
    print('현재시간 : 오전 {}시 {}분 {}초'.format(time.hour%12,time.minute,time.second))