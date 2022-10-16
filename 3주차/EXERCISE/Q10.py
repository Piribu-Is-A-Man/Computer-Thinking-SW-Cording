n=int(input('n을 입력하시오 : '))

for i in range(n):
    if(i%2==0):
        st=''
        for j in range(1,n+1):
            st+=str(n*i+j)+'\t'
        print(st)
    else:
        st=''
        for j in range(0,n):
            st+=str(n*i+n-j)+'\t'
        print(st)