f=open('numbers.txt','w')
for i in range(100,500,100):
    f.write('{}\n'.format(i))
f.close()