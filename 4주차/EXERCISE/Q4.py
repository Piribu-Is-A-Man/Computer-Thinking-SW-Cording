n_list=[10,20,30,50,60]
print("리스트 원소들: ",n_list)
max = n_list[0]
for i in range(5):
    if(n_list[i]>max):
        max=n_list[i]
print("리스트 원소들 중 최댓값: ",max)