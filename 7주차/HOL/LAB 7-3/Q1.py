import datetime as dt

answer=dt.datetime.now()+dt.timedelta(days=1000)

print('오늘 날짜로부터 1,000일 후 ? {}년 {}월 {}일'.format(answer.year,answer.month,answer.day))

