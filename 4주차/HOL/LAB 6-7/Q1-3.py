#1번문제
t_person = ('홍길동',2019001, 179)
person=(t_person[0],t_person[1],t_person[2])
print(person)

#2번문제
# person[0]=2019003 
# TypeError: 'tuple' object does not support item assignment

#3번문제
person=list(t_person)
person[1]=2020003
print("학번 변동 후 person = ",tuple(person))
