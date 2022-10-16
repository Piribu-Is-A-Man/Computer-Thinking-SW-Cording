import random as rd

numlist=[]

for i in range(3):
    numlist.append(rd.randrange(0,101,5))

print('0에서 100 이하의 정수 중에서 5의 배수')
print(numlist)