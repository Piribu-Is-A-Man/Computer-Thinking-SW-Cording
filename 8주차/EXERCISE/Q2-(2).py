f1=open('number1to10.txt','r')
f2=open('numberby10.txt','r')

f3=open('merge.txt','w')
for i in range(10):
    f3.write('{} : {}\n'.format(f1.readline().rstrip(),f2.readline().rstrip()))
f1.close()
f2.close()
f3.close()