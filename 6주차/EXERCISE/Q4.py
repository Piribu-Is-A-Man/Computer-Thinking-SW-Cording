def findnum(a,b):
    numlist=[]
    for i in range(b,a-1,-1):
        numlist+=[i]

    #리스트에서 가장 큰수를 기준으로 최소공배수 찾아나가기
    answer=numlist[0]


    for i in range(1,len(numlist)):
        for j in range(1,1000):
            if(j%numlist[i]==0 and j%answer==0):
                answer=j
                break
    return answer


a=int(input('범위의 시작 정수 : '))
b=int(input('범위의 마지막 정수 : '))

print('{}에서 {}까지의 정수들의 최소 공배수는 : {}'.format(a,b,findnum(a,b)))