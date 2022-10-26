import random as rd

def makeRandInt30():
    f=open('randint30.txt','w')
    for i in range(30):
        f.write('{} '.format(rd.randint(1,10)))
    f.close()

def readtxt():
    f=open('randint30.txt','r')
    nums=f.read()
    a=list(map(int,nums.split()))
    
    for i in range(1,11):
        print('{} : {}개'.format(i,nums.count(str(i))))


makeRandInt30()
readtxt()