a=[1,2,3,4,5]
b=['첫','두','세','네','다섯']
print('a =',a)
try:
    num=int(input('a의 요소를 하나 선택하시오 : '))
    print(num,'은(는)',b[num-1],'번째 요소입니다.')
except(ValueError):
    print('오류 : 입력 값이 정수나 실수가 아님')