#you're given a list [1,2,3,7,8,9].
#And you need to transform it into [1,2,3,4,5,6,7,8,9].
#Write down your python code to make it

#방법1 : 처음과 끝자리만 따서 새로 리스트 만들기
list=[1,2,3,7,8,9]
newlist=[]
n=list[len(list)-1]
for i in range(list[0],n+1):
    newlist.append(i)
list=newlist
print(list)

#방법2 : insert()활용
list=[1,2,3,7,8,9]
while(list[len(list)-1]!=len(list)):
    for i in range(1,len(list)+1):
        if(i!=list[i-1]):
            list.insert(i-1,i)
print(list)



