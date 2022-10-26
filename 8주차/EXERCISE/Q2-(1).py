try:
    f1=open("number1to10.txt","r")
except Exception as e:
    print('error :',e)
else:
    f2=open("numberby10.txt","w")
    for i in range(10):
        num=int(f1.readline())
        f2.write(str(num*10))
        f2.write('\n')
    f1.close()
    f2.close()
