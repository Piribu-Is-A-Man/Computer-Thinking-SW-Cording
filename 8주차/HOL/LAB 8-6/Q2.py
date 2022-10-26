f=open('we_will_rock.txt','r')

s=[]

for i in range(6):
    s.append(f.readline())
    
for i in range(5,-1,-1):
    print(s[i].rstrip())