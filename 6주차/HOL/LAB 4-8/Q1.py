def multiplies(n,m):
    result=()
    for i in range(m):
        result=result+((i+1)*n,)
    return result

r1,r2,r3,r4=multiplies(3,4)
print(r1,r2,r3,r4)
r1,r2,r3,r4,r5=multiplies(2,5)
print(r1,r2,r3,r4,r5)