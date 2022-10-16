import datetime

today=datetime.date.today()


print('오늘은 {}년 {}월 {}일 입니다.'.format(today.year,today.month,today.day))

xmas=datetime.datetime(2022,12,25)
timegap=xmas-datetime.datetime.now()
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(timegap.days,timegap.seconds//3600))