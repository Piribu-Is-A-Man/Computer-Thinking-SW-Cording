n=int(input('숫자를 입력하세요 : '))

for i in range(2,n):
    if(n%i==0):
        print(n,'는 소수가 아닙니다.')
        break
    else:
        if(i==n-1):
            print(n,'는 소수입니다.')
