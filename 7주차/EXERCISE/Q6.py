import datetime as dt

today=dt.datetime.today()
love=dt.datetime(2019,2,24)
gap=today-love

def ddayprint(n):
    dgap=today+dt.timedelta(days=n)
    print('{}일 기념일 : {}년 {}월 {}일'.format(n,dgap.year,dgap.month,dgap.day))

print('오늘은 {}년 {}월 {}일입니다.'.format(today.year,today.month,today.day))
print('춘향이와 몽룡이의 연애 시작일 : {}년 {}월 {}일'.format(love.year,love.month,love.day))
print('연애 시작일로부터 경과한 날짜 : {}일'.format(gap.days))
ddayprint(100)
ddayprint(200)
ddayprint(500)
ddayprint(1000)
