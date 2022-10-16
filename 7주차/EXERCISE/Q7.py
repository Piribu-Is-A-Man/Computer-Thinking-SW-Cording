import time as t

def sum1to1000000():
    sum=0
    for i in range(1,1000001):
        sum+=i
    return sum

start=t.time()
for j in range(1,101):
    sum1to1000000()
end=t.time()

gap=end-start

print('1에서 1,000,000까지의 합을 100번 반복해서 구하는 시간: {:7.4f}초'.format(gap))
