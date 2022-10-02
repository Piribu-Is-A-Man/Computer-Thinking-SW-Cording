#221002
#4주차까지의 개념을 배운 후 코딩

#factorial

num=int(input())
fac=1
for i in range(0,num):
    fac=fac*(i+1)

print(num,'! = ',fac)
