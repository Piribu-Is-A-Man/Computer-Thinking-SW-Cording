import random as rd

num=rd.randrange(1,21)

count=0
while(1):
    searchnum=int(input('1~20까지의 숫자를 입력하세요 : '))

    if(searchnum<num):
        print('{}보다 큽니다!'.format(searchnum))
        count+=1
        continue
    elif(searchnum>num):
        print('{}보다 작습니다!'.format(searchnum))
        count+=1
        continue
    else:
        print('정답입니다!')
        count+=1
        break

if(count<3):
    print('{}번 만에 맞춘 당신은 천재!'.format(count))
elif(3<=count and count<7):
    print('{}번 만에 맞추셨네요. 잘 했어요^^'.format(count))
else:
    print('{}번 만에 맞추다니 쩝쩝...'.format(count))