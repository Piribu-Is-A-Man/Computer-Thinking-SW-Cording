#5.	사용자로부터 5개의 수를 입력받은 후 
# 다음과 같이 입력된 값들의 합, 평균, 최댓값, 최솟값을 출력하는 프로그램을 작성하시오. 
# 이때 반드시 입력된 값들은 리스트에 넣어서 sum(), min(), max() 함수를 사용하도록 하시오

numlist=[]

print("5개의 수를 입력하세요 :")
for i in range(5):
    numlist.append(int(input()))

print("합 :",sum(numlist))
print("평균 :",sum(numlist)/len(numlist))
print("최댓값 :",max(numlist))
print("최솟값 :",min(numlist))
