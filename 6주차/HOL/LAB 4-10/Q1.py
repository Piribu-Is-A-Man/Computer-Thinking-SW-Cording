def sum_nums(*numbers):
    print(len(numbers),'개의 인자',numbers)
    result=0
    for n in numbers:
        result+=n
    print('합계 :',result,', 평균 :',result/len(numbers))
    return result

sum_nums(10,20,30)
sum_nums(10,20,30,40,50)

