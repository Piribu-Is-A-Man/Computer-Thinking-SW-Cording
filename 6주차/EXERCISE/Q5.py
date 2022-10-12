def unit_fraction(frac):
    i=1
    searchnum=abs(1-frac)
    while (1):
        i+=1
        nextsearchnum=abs(1/i-frac)
        if(searchnum<nextsearchnum):
            return i-1
        searchnum=nextsearchnum

frac=float(input('1보다 작고 0보다 큰 소수를 입력하세요:'))
print('가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.'.format(unit_fraction(frac),1/unit_fraction(frac)))