import random as rd

r=rd.randrange(1,7)
j=rd.randrange(1,7)

print('로미오의 주사위 숫자는 {}입니다.'.format(r))
print('줄리엣의 주사위 숫자는 {}입니다.'.format(j))

if(r>j):
    print('로미오가 이겼습니다.')
elif(j>r):
    print('줄리엣이 이겼습니다.')
else:
    print('비겼습니다.')