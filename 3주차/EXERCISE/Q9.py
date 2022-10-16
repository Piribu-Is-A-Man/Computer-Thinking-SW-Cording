n=int(input('숫자를 입력하세요 : '))

for i in range(1,n+1):
    st=''
    for j in range(n-i):
        st+=' '
    for j in range(i):
        st+='*'
    print(st)