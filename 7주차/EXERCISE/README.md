# 7주차: 컴퓨팅사고와 SW코딩 예제문제
***

### Q1.	로미오와 줄리엣 두 사람이 주사위를 던져서 높은 숫자가 나오면 이기는 게임을 만들어보자. 로미오와 줄리엣의 주사위는 모두 다음과 같이 random 모듈의 randrange( )를 통해서 생성한 난수를 바탕으로 한다. 출력 결과는 다음과 같이 로미오가 이기거나, 줄리엣이 이기거나, 비기는 결과가 나와야 한다. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q1.py)

![image](https://user-images.githubusercontent.com/114078946/196027787-30b2f2b7-aae4-498b-81d0-2782d405489f.png)

##### 풀이 및 해설

random 모듈을 이용해 일단 로미오와 줄리엣의 주사위값을 정해줍니다.

randrange의 인자는 range랑 똑같이 생각하면 되기에 1,7을 넣으면 됩니다.

```python
import random as rd

r=rd.randrange(1,7)
j=rd.randrange(1,7)

print('로미오의 주사위 숫자는 {}입니다.'.format(r))
print('줄리엣의 주사위 숫자는 {}입니다.'.format(j))
```
위와 같이 로미오와 줄리엣 주사위 값을 줬다면 이제 비교만 해서 누가 이겼는지, 또는 비겼는지 확인만 하면 됩니다.

```python
if(r>j):
    print('로미오가 이겼습니다.')
elif(j>r):
    print('줄리엣이 이겼습니다.')
else:
    print('비겼습니다.')
```

***

### Q2.	랜덤 숫자 맞추기 게임 프로그램을 작성하라. 먼저 랜덤하게 1~20까지의 숫자 x를 하나 생성시키고 사용자는 숫자를 하나씩 입력하면서 생성된 숫자 x와 비교해 큰지 작은지를 보고 숫자를 맞춰가는 게임이다. 컴퓨터는 사용자가 입력한 숫자가 정답보다 큰지 작은지를 알려주어야 한다. 그리고 사용자가 시도를 할 때 마다 시도한 횟수가 n에 저장되도록 한다. 만일 입력한 숫자와 x가 일치하면 “정답입니다!”라는 메시지를 출력한다. 이때 3번 이하로 입력하여 숫자를 맞추면 “n번 만에 맞춘 당신은 천재!”, 3번 이상 6번 이하로 입력하여 숫자를 맞추면 “n번 만에 맞추셨네요. 잘 했어요^^”, 7번 이상으로 숫자를 입력하여 맞추면 “n번 만에 맞추다니 쩝쩝…”이라고 출력하라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q2.py)

![image](https://user-images.githubusercontent.com/114078946/196027947-8e805829-edc0-4f87-87dc-dbd9692658d2.png)

##### 풀이 및 해설

먼저 random 모듈을 불러온뒤 1~20사이 값을 저장해줍니다.

```python
import random as rd

num=rd.randrange(1,21)
```

그리고 답을 찾을때까지 계속해서 반복해야 하니 while을 사용해주고, 정답을 찾을때까지 횟수를 기록하면서 반복해야합니다.

```python
count=0
while(1):
    searchnum=int(input('1~20까지의 숫자를 입력하세요 : '))

    if(searchnum<num):
        print('{}보다 큽니다!'.format(searchnum))
        count+=1
        continue
    elif(searchnum>num):
        print('{}보다 작습니다!'.format(searchnum))
        count+=1
        continue
    else:
        print('정답입니다!')
        count+=1
        break
```

이제 정답을 찾은경우 while이 끝나게 되고, 몇번만에 찾았는지 count를 통해 출력하면 됩니다.
```python
if(count<3):
    print('{}번 만에 맞춘 당신은 천재!'.format(count))
elif(3<=count and count<7):
    print('{}번 만에 맞추셨네요. 잘 했어요^^'.format(count))
else:
    print('{}번 만에 맞추다니 쩝쩝...'.format(count))
```

***

### Q6.	춘향이와 몽룡이는 2019년 2월 24일 발렌타인데이에 연애를 시작했다. 오늘은 두사람의 연애 시작일로부터 며칠이 경과하였는가? Datetime 모듈을 사용하고 오늘날짜 date.today()를 통해 받아와서 오늘날짜, 연애를 시작한 날짜와 경과한 날짜, 기념일을 다음과 같이 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q6.py)

![image](https://user-images.githubusercontent.com/114078946/196028086-e24880fb-bfbe-43ff-83cd-3fc30de2eddd.png)

##### 풀이 및 해설

먼저 datetime 모듈을 불러와 오늘 날짜와 춘향이와 몽룡이의 연애 시작일 값을 저장해줍니다.

또 gap을 (오늘 날짜)와 (연애 시작일)의 차로 저장해줍니다. 

그리고 아래와 같이 출력해줍니다.

```python
import datetime as dt

today=dt.datetime.today()
love=dt.datetime(2019,2,24)
gap=today-love

print('오늘은 {}년 {}월 {}일입니다.'.format(today.year,today.month,today.day))
print('춘향이와 몽룡이의 연애 시작일 : {}년 {}월 {}일'.format(love.year,love.month,love.day))
print('연애 시작일로부터 경과한 날짜 : {}일'.format(gap.days))
```

이제 기념일을 출력해주면 되는데 실행결과 예시에서 오늘 날짜를 기준으로 기념일을 챙겼기에 저도 그렇게 해줍니다.

먼저 기념일을 출력하는 함수를 만들어서 반복을 줄여줍니다.

그리고 함수를 통해 100일, 200일, 500일, 1000일 기념일을 출력해주면 됩니다.

```python
def ddayprint(n):
    dgap=today+dt.timedelta(days=n)
    print('{}일 기념일 : {}년 {}월 {}일'.format(n,dgap.year,dgap.month,dgap.day))

ddayprint(100)
ddayprint(200)
ddayprint(500)
ddayprint(1000)
```

***

### Q7.	1부터 1,000,000까지 정수의 합을 구하여 반환하는 함수 sum1to1000000()을 작성하고 함수를 100번 호출하여 함수 수행 시간을 다음과 같이 초단위로 구하여 출력하여라. (소수점 4자리까지 표현할 것.) [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q7.py)

![image](https://user-images.githubusercontent.com/114078946/196028687-46c97619-04f2-431f-ba60-041b4067eeaf.png)

함수 수행 시간을 구하려면 time 모듈을 불러와야 합니다.

time 모듈을 불러온뒤 함수 호출 전후로 start, end로 값을 저장한 뒤, 차가 함수 수행 시간이 됩니다.

먼저 함수 sum1to1000000()을 선언합니다.

```python
def sum1to1000000():
    sum=0
    for i in range(1,1000001):
        sum+=i
    return sum
```

이후 time 모듈을 불러오고 함수 수행 시간을 구해주면 됩니다.

```python
import time as t

start=t.time()
for j in range(1,101):
    sum1to1000000()
end=t.time()

gap=end-start

print('1에서 1,000,000까지의 합을 100번 반복해서 구하는 시간: {:7.4f}초'.format(gap))
```

***

### Q8.	다음과 같은 함수를 작성하고 100번 반복하여 함수 수행 시간을 다음과 같이 초단위로 구하여 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q8.py)

#### (1)	1000 팩토리얼을 구하는 함수

![image](https://user-images.githubusercontent.com/114078946/196028780-d71f3d52-e516-496d-abe4-10fca2114014.png)

##### 풀이 및 해설

일단 함수 동작 시간을 구해야 하니 미리 time모듈을 불러 놓고, 팩토리얼 함수를 선언합시다.

하면서 알아차린 사실이지만 **1000번 넘게 재귀되는 함수로 만들면 오류**가 뜨니

이번은 재귀함수 형태로 만들지 말고 선언해주도록 했습니다.

```python
import math as m
import time as t

def fac():
    facto=1
    for i in range(1,1001):
        facto+=i
    return facto
```

이제 선언한 함수가 100번 반복되는 동안 걸리는 시간만 구해주면 됩니다.

```python
start=t.time()
for i in range(100):
    fac()
end=t.time()
print('1000!을 100번 반복해서 구하는 시간: {:7.4f}초'.format(end-start))
```

#### (2)	1에서 1000까지의 모든 홀수를 세제곱하여 더한 값을 반환하는 함수

![image](https://user-images.githubusercontent.com/114078946/196028799-d1192439-b2e0-4a24-9b66-e8c248db4188.png)

##### 풀이 및 해설

위 문제와 큰 차이 없지만 math모듈을 이용해 세제곱을 쉽게 구할 수 있습니다.

```python
def oddpow3():
    sum=0
    for i in range(1,1000,2):
        sum+=pow(i,3)
    return sum

start=t.time()
for i in range(100):
    oddpow3()
end=t.time()

print('1에서 1000까지 홀수의 세제곱 더하기 결과: {}'.format(oddpow3()))
print('1에서 1000까지 홀수의 세제곱 더하기를 100번 반복하는 시간: {:7.4f}초'.format(end-start))

```

#### (3)	1도에서 360도까지의 sin값을 1도 단위로 구하여 그 합을 반환하는 함수

![image](https://user-images.githubusercontent.com/114078946/196028803-7623a38b-1874-46e5-9312-a1efe9d64a75.png)

##### 풀이 및 해설

sin안에 들어가는 값을 radians로 변환해주는 것을 for문으로 반복해주는 함수만 만들어주면 됩니다.

```python
def sumsin():
    sum=0
    for i in range(1,361):
        sum+=m.sin(m.radians(i))
    return sum

start=t.time()
for i in range(100):
    sumsin()
end=t.time()

print('1에서 360도까지의 sin값의 합: {}'.format(sumsin()))
print('1에서 360도까지의 sin값 더하기를 100번 반복하는 시간: {:7.4f}초'.format(end-start))
```

***

### Q9.	0부터 1,000,000까지의 임의의 정수를 10개 연속적으로 출력하는 의사난수 함수 myRand()를 생성하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q9.py)

![image](https://user-images.githubusercontent.com/114078946/196029055-21d9177d-b336-4526-8908-8121a0eb7fcf.png)

##### 풀이 및 해설

모듈 random 과 randrange()를 이용하면 쉽게 구할 수 있습니다.

randrange는 for문에서 자주 쓰던 range와 사용방법이 같습니다.

활용해서 아래 코드처럼 만드면 됩니다.

```python
import random as rd

def myRand():
    for i in range(10):
        rdn=rd.randrange(1,1000001)
        print(rdn)

myRand()
```

***

### Q10.	math 모듈을 사용하여 0도에서 180도까지 10도 단위로 sin, cos, tan 값을 구하여 다음과 같이 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/7%EC%A3%BC%EC%B0%A8/EXERCISE/Q10.py)

![image](https://user-images.githubusercontent.com/114078946/196029121-35bf3721-862d-422a-a98d-8661efd50605.png)

##### 풀이 및 해설

for문을 이용해서 0도에서 180도까지 10도 차이는 range(0,190,10)으로 표현하면 되고,

sin,cos,tan 인자로 radians()를 사용해야 합니다.

```python
import math as m

for i in range(0,190,10):
    n=m.radians(i)
    print('sin({:3}) = {:7.4f}, cos({:3}) = {:7.4f}, tan({:3}) = {:7.4f}'.format(i,m.sin(n),i,m.cos(n),i,m.tan(n)))
```

***









