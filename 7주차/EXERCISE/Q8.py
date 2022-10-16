import math as m
import time as t

def fac():
    facto=1
    for i in range(1,1001):
        facto+=i
    return facto

def oddpow3():
    sum=0
    for i in range(1,1000,2):
        sum+=pow(i,3)
    return sum

def sumsin():
    sum=0
    for i in range(1,361):
        sum+=m.sin(m.radians(i))
    return sum

start=t.time()
for i in range(100):
    fac()
end=t.time()
print('1000!을 100번 반복해서 구하는 시간: {:7.4f}초'.format(end-start))

start=t.time()
for i in range(100):
    oddpow3()
end=t.time()

print('1에서 1000까지 홀수의 세제곱 더하기 결과: {}'.format(oddpow3()))
print('1에서 1000까지 홀수의 세제곱 더하기를 100번 반복하는 시간: {:7.4f}초'.format(end-start))

start=t.time()
for i in range(100):
    sumsin()
end=t.time()

print('1에서 360도까지의 sin값의 합: {}'.format(sumsin()))
print('1에서 360도까지의 sin값 더하기를 100번 반복하는 시간: {:7.4f}초'.format(end-start))