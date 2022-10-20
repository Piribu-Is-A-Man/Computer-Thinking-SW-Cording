# 6주차: 컴퓨팅사고와 SW코딩
***

### Q1. 사용자로부터 임의의 수를 연속적으로 입력받도록 하시오. <br>이 수들에 대한 평균값, 최댓값, 최솟값을 반환하는 함수 mean_of_n(nums), max_of_n(nums), min_of_n(nums)을 구현하여 다음과 같이 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/6%EC%A3%BC%EC%B0%A8/EXERCISE/Q1.py)

![image](https://user-images.githubusercontent.com/114078946/195338415-cfe26f25-ce43-42b5-9aca-f1eda8f53d07.png)

##### 풀이 및 해설
먼저 문제에서 요구하는 함수들을 먼저 만들어 보겠습니다.


평균값은 입력된 정수의 합을 정수의 갯수로 나누면 되는데 이미 알고있는 sum()함수와 len()함수를 이용하면 쉽게 만들 수 있습니다.
```python
def mean_of_n(nums):
    result = (sum(nums)/len(nums))
    return result
```
위와 같은 형태로 만들어 줄수 있고 최댓값과 최솟값을 반환하는 함수 또한 이미 알고 있는 함수인 min(), max()를 이용해 줍니다.
```python
def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)
```
함수는 완성하였으니 그럼 문제에서 보여준 예시처럼 정수를 입력 받아봅시다.

숫자가 얼마나 입력될지 모르니 공백을 기준으로 리스트화 시켜 받아보려합니다.

```python
nums=list(map(int,input('정수를 여러 개 입력하시오 : ').split(' ')))
```

이렇게 입력받은 정수들을 예제처럼 출력해주기만 하면 됩니다.
```python
print('평균값은 {}'.format(mean_of_n(nums)))
print('최댓값은 {}'.format(max_of_n(nums)))
print('최솟값은 {}'.format(min_of_n(nums)))
```

***
### Q2.직각삼각형의 빗변을 이루는 선분의 양 끝점을 나타내는 두 좌표 (x1, y1), (x2, y2)를 입력받아 직각삼각형의 면적을 구하는 프로그램을 작성하여라. <br>이때 4개의 좌표값을 입력으로 받아 직각삼각형의 면적을 반환하는 area(x1, y1,x2, y2) 함수를 구현하시오.<br> 단, x2>x1이고 y2>y1이다. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/6%EC%A3%BC%EC%B0%A8/EXERCISE/Q2.py)

![image](https://user-images.githubusercontent.com/114078946/195340790-6bc21601-4b44-42b9-8aba-d831e5999874.png)

##### 풀이 및 해설
직각삼각형의 넓이는 (밑변)X(높이)/2 입니다.

x2>x1이고 y2>y1이라는 조건이 주어져 있기 때문에,

빗변의 두 점 좌표가 주어졌다면 (x좌표끼리의 차)*(y좌표끼리의 차)/2를 하면 직각삼각형의 넓이를 구할 수 있습니다.

```python
def area(x1, y1, x2, y2):
    return (x2-x1)*(y2-y1)/2
```
area라는 함수를 정의했고 리턴값으로 넓이를 출력합니다.

이제 빗변의 좌표를 예제처럼 입력받아 직각삼각형의 면적을 출력해 봅니다.

```python
x1=int(input('x1 좌표를 입력하시오 : '))
y1=int(input('y1 좌표를 입력하시오 : '))
x2=int(input('x2 좌표를 입력하시오 : '))
y2=int(input('y2 좌표를 입력하시오 : '))

print('직각삼각형의 면적은 : {}'.format(area(x1,y1,x2,y2)));
```

***

### Q3. 쉼표 단위로 구분된 정수를 임의의 수만큼 입력받은 후 이 숫자들을 오름차순으로 정렬하여 출력하시오. <br>힌트: split( ) 메소드를 사용한다. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/6%EC%A3%BC%EC%B0%A8/EXERCISE/Q3.py)

![image](https://user-images.githubusercontent.com/114078946/195342044-f55ed894-8ce7-4a80-8092-930a2a789ca1.png)

##### 풀이 및 해설

쉼표로 구분이 되었으니 힌트에서 주어진 것 처럼 split() 메소드를 사용합니다.
```python
numlist=list(map(int,input('쉼표로 구분된 정수를 여러 개 입력하시오: ').split(',')))
```
위 코드대로라면 입력받은 정수들이 ,로 구분되어 numlist에 리스트형식으로 저장되었을 겁니다.

문제 예시에서 보인것처럼 출력해봅니다.

```python
print('입력된 정수의 리스트:',numlist)
```
예제에서 보여진 것처럼 리스트 형식으로 출력되었습니다.

마지막으로 정렬은 내장 함수를 활용해 해보겠습니다.

```python
sortedlist=sorted(numlist)
print('정렬된 정수의 리스트:',sortedlist)
```
정렬된 정수의 리스트가 출력됩니다.

***

### Q4.	두 개의 정수 a, b를 입력으로 받는다. 이때 a < b라는 조건이 항상 지켜진다고 하자. <br>여러분이 작성할 코드는 a에서 b까지(a, b 포함) 범위의 모든 정수의 배수이면서 가장 작은 값을 갖는 값을 찾는 것이다. <br>예를 들어 2, 4가 입력되면 2, 3, 4 모두의 배수이면서 가장 작은 값이 되는 12가 답이 된다. <br>12는 2의 배수, 3의 배수, 4의 배수이다. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/6%EC%A3%BC%EC%B0%A8/EXERCISE/Q4.py)

![image](https://user-images.githubusercontent.com/114078946/195343066-f1741759-e762-43e3-a69e-31c72310c3e5.png)

##### 풀이 및 해설

먼저 문제 예시에서 보여진것처럼 시작 정수와 마지막 정수를 입력 받습니다.

```python
a=int(input('범위의 시작 정수 : '))
b=int(input('범위의 마지막 정수 : '))
```

문제에서 원하는 것은 a에서 b까지의 정수들의 최소 공배수이므로, 큰 수 들부터 비교해 가는것이 더 유리합니다.

2와3의 최소공배수인 6을 찾고 또 4와 6의 최소 공배수를 찾는 것보다,

3과4의 최소공배수인 12를 찾고 2와 12인 공배수를 찾는게 더 편리할 것 같다 생각이 들었습니다.

정리가 잘 되게 함수를 정의해줍니다.

```python
def findnum(a,b):
    numlist=[]
    for i in range(b,a-1,-1):
        numlist+=[i]

    #리스트에서 가장 큰수를 기준으로 최소공배수 찾아나가기
    answer=numlist[0]

    for i in range(1,len(numlist)):
        for j in range(1,1000):
            if(j%numlist[i]==0 and j%answer==0):
                answer=j
                break
    return answer
```
먼저 a,b사이의 숫자를 numlist에 역순(큰수부터 작은수)으로 정렬합니다.

첫번째 for문은 numlist에 있는 숫자들을 하나하나 꺼내주는 역할을 하고

두번째 for문은 1000미만의 숫자중에 최소 공배수를 찾아주는 역할을 합니다.

위 함수로 찾은 최소공배수인 answer값이 리턴됩니다.

이제 예제처럼 출력만 해주면 됩니다.

```python
print('{}에서 {}까지의 정수들의 최소 공배수는 : {}'.format(a,b,findnum(a,b)))
```

***

### Q5.	분자가 1인 분수를 단위 분수라고 한다. 1보다 작은 소수값이 주어졌을 때 이 소수값에 가장 가까운 단위 분수를 찾는 함수 def unit_fraction(frac)을 구현하자. <br>예를 들어 0.27이 주어지면 1/3은 0.33333….이고 1/4는 0.25이며 1/5는 0.2이므로 1/4가 가장 가까운 단위분수이다. 이렇게 가장 가까운 단위분수를 찾아 출력하고 이 단위분수를 소수값으로 표현한 결과도 같이 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/6%EC%A3%BC%EC%B0%A8/EXERCISE/Q5.py)

![image](https://user-images.githubusercontent.com/114078946/195344550-cbfd297f-38f0-4bf5-ac2a-90e58f00d4cc.png)

##### 풀이 및 해설

주어진 소숫값에 가장 가까운 단위분수는 달리 생각하면 두수의 차의 절대값이 가장 작은 경우라고 볼수 있습니다.

즉, |(주어진 소숫값)-(단위분수)| 가 최솟값일 때 단위분수가 우리가 원하는 값이라 볼 수 있습니다.

위 내용대로 unit_faction을 정의해보겠습니다.

```python
def unit_fraction(frac):
    i=1
    searchnum=abs(1-frac)
    while (1):
        i+=1
        nextsearchnum=abs(1/i-frac)
        if(searchnum<nextsearchnum):
            return i-1
        searchnum=nextsearchnum
```

값이 큰 단위분수 부터 비교해가며 frac을 뺀 절대값이 가장 작을경우는

이후 단위분수와 주어진 소숫값의 차의 절대값보다 이전 단위분수와 주어진 소숫값의 차의 절대값이 작을 때 입니다.

말이 어렵긴 한데 |(주어진 소숫값)-(단위분수)|가 점점 작아지다 다시 커지는 부분, 즉 변곡점이 우리가 찾는 값이라 볼 수 있습니다.

위 함수대로 찾았다면 이제 출력만 해주면 됩니다.

```python
frac=float(input('1보다 작고 0보다 큰 소수를 입력하세요:'))
print('가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.'.format(unit_fraction(frac),1/unit_fraction(frac)))
```

***

작성날짜 221012







