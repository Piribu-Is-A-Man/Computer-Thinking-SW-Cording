n=int(input('1에서 9까지의 수를 입력하세요:'))

while(1):
    if(n>0 and n<10):
        break
    else:
        n=int(input('1에서 9까지의 수를 다시 입력하세요:'))

for i in range(1,10):
    print(n,'*',i,'=',n*i)