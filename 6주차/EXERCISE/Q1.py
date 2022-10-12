def mean_of_n(nums):
    result = (sum(nums)/len(nums))
    return result

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

nums=list(map(int,input('정수를 여러 개 입력하시오 : ').split(' ')))

print('평균값은 {}'.format(mean_of_n(nums)))
print('최댓값은 {}'.format(max_of_n(nums)))
print('최솟값은 {}'.format(min_of_n(nums)))