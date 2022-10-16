import random as rd

numlist=[]

def lotto():
    for i in range(1,46):
        numlist.append(i)
    rd.shuffle(numlist)
    lotto=numlist[:6]
    lotto=sorted(lotto)
    print('로또번호 :',lotto)

lotto()