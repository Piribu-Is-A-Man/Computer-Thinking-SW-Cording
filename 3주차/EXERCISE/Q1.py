a,b,c=map(int,input('세 정수를 입력하시오 : ').split(' '))

if(b<a and b<c):
    a,b=b,a
elif(c<a and c<b):
    a,c=c,a

if(a>c and a>b):
    a,c=c,a
elif(b>a and b>c):
    b,c=c,b

print(a,b,c)