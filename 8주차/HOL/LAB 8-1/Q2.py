try:
    a=[10,20,30]
    print(a[3])
except Exception as e:
    print('error :',e)
#error : list index out of range

try:
    print(int('20%'))
except Exception as e:
    print('error :',e)
#error : invalid literal for int() with base 10: '20%' 

try:
    a=100+'200'
except Exception as e:
    print('error :',e)
#error : unsupported operand type(s) for +: 'int' and 'str'