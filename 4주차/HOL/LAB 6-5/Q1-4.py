#1번문제
fruits_dic = {'apple':6000, 'melon':3000, 'banana':5000, 'orange':4000}

print(list(fruits_dic.keys()))

#2번문제
print(list(fruits_dic.values()))

#3번문제
print("fruits_dic 딕셔너리의 항목의 개수 : ",len(fruits_dic.keys()))

#4번문제
if('apple'in fruits_dic):
    print("apple is in fruits_dic.")
else:
    print("apple is not in fruits_dic.")

if('mango'in fruits_dic):
    print("mango is in fruits_dic.")
else:
    print("mango is not in fruits_dic.")
    