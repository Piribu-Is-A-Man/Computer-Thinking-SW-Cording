import math as m

for i in range(0,190,10):
    n=m.radians(i)
    print('sin({:3}) = {:7.4f}, cos({:3}) = {:7.4f}, tan({:3}) = {:7.4f}'.format(i,m.sin(n),i,m.cos(n),i,m.tan(n)))