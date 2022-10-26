f1=open('we_will_rock.txt','r')
f2=open('we_will_rock_upper.txt','w')

for i in range(6):
    s=f1.readline()
    s_upper=s.upper()
    f2.write(s_upper)