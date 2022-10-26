
try:
    f=open("greet.txt","w")
except Exception as e:
    print('error :',e)
else:
    f.write('Hi, everyone.\n')
    f.write('Welcome to Python.')
    f.close()
