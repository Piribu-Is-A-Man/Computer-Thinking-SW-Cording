f=open("numbers.txt","r")

for i in range(4):
    s=f.readline().rstrip()
    print(s)