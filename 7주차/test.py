#과제1 내가 태어난 년도로부터 10000일 지난 날짜가 언제인지
import datetime

birth=datetime.datetime(1997,7,3)
answer=birth+datetime.timedelta(days=10000)

print('생일로 부터 10000일 지난 후 ? {}년 {}월 {}일'.format(answer.year,answer.month,answer.day))

#과제2 유명한 파이썬 패키지 5개 찾아서 word로 만들기

#과제 DiceGame:A와 B가 주사위를 던져 누가 이겼는지(이길때까지)
import random as rd

def dicegame():
    while(1):
        a=rd.randrange(1,7)
        b=rd.randrange(1,7)
        if(a>b):
            print('a : {}, b : {}로 a 승리!'.format(a,b))
            return a
        elif(b>a):
            print('a : {}, b : {}로 b 승리!'.format(a,b))
            return b
        else:
            print('a : {}, b : {}로 비겨서 재경기!'.format(a,b))
            continue

dicegame()