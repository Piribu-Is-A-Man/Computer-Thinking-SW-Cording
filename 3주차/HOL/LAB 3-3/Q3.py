adult=int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))
marry=int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0): '))
if(adult==1):
    if(marry==1):
        print('당신은 결혼한 성인입니다.')
    else:
        print('당신은 결혼하지 않은 성인입니다.')
else:
    if(marry==1):
        print('당신은 결혼한 미성년자입니다.')
    else:
        print('당신은 결혼하지 않은 미성년자입니다.')