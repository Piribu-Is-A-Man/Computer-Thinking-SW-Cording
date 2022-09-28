s1 = {10,20,30,40}
s2 = {30,40,50,60,70}

s1 | s2
#{10,20,30,40,50,60,70}
s1 & s2
#{30,40}
s1 - s2
#{10,20}
s1 ^ s2
#{10,20,50,60,70}
s1.issubset(s2)
#False
s1.issuperset(s2)
#False
s1.isdisjoint(s2)
#False