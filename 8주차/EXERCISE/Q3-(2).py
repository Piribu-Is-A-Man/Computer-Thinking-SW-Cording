try:
    f=open('my_hello.txt','w')
except(PermissionError):
    print('이미 존재하는 파일을 읽을수가 없습니다.')
