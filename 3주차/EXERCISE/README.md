# 3주차: 컴퓨팅사고와 SW코딩 예제문제

### Q1.	다음과 같이 사용자로부터 3개의 임의의 정수를 입력으로 받아서 가장 작은 수부터 큰 수까지 나열하는 프로그램을 if-else 문을 사용하여 작성하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q1.py)

![image](https://user-images.githubusercontent.com/114078946/196036607-c9609dd8-4032-49b9-8f31-970a2b16baca.png)

##### 풀이 및 해설

먼저 숫자 3개를 입력 받아야 하는데, 그냥 input으로는 str형식이라서 튜플형식으로 저장할수가 없습니다.

그래서 map()을 이용해서 입력받은 숫자를 int형식으로 한꺼번에 변환해줍니다.

```python
a,b,c=map(int,input('세 정수를 입력하시오 : ').split(' '))
```

split() 메소드를 사용해 띄어쓰기를 기준으로 구분했고, a,b,c에 각각 입력받은 정수 하나씩 값을 저장했습니다.

이후에는 일단 먼저 가장 작은 숫자를 a에 저장하려고 했습니다.

경우의 수는 3가지인데, 1)a에 이미 최소값이 있는경우, 2)b에 최솟값이 있는경우, 3)c에 최솟값이 있는경우 입니다.

순서대로 a,b,c를 정렬한다고 생각하면 1)경우는 건드릴 필요가 없고 2), 3)경우만 수정해주면 됩니다.

먼저 2)경우 입니다.

```python
if(b<a and b<c):
    a,b=b,a
```
b과 최솟값인 경우 a랑 자리를 바꿔줍니다.

다음은 3)경우 입니다.
```python
elif(c<a and c<b):
    a,c=c,a
```
c과 최솟값인 경우 a랑 자리를 바꿔줍니다.

이제 최솟값은 a에 위치했으니 최댓값도 똑같이 위치를 옮겨줍니다.

위와 같은 형식으로 최댓값 코드도 짜면 

```python
if(a>c and a>b):
    a,c=c,a
elif(b>a and b>c):
    b,c=c,b
```

이렇게 나옵니다.

위 코드대로면 최댓값은 c에 저장이 되고, a,b,c 모두 크기순으로 나열이 되어있으므로 그대로 출력하기만 하면됩니다.

```pyhton
print(a,b,c)
```

***

### Q2.	사용자로부터 x, y 좌표를 가진 한 점을 입력으로 받아서 이 점이 1, 2, 3, 4 분면의 어디에 속하는지를 알려주는 프로그램을 작성하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q2.py)

![image](https://user-images.githubusercontent.com/114078946/196036854-2b796b3c-f8f4-456a-af44-7c52f1fe42ef.png)

##### 풀이 및 해설

1번문제에서 사용했던 map()을 여기서도 사용해서 x,y값을 각각 입력받습니다.

```python
x,y=map(int, input('점의 좌표 x, y를 입력하시오 : ').split(' '))
```

이제 각각 사분면에 따라 조건을 수정해주면 됩니다.

1사분면인 경우 x>0,y>0, 2사분면인 경우 x<0,y>0,

3사분면인 경우 x<0,y<0, 4사분면인 경우 x>0,y<0 임을 생각하며 코드를 짜면 아래와 같이 나옵니다

```python
if(x>0):
    if(y>0):
        print('1사분면에 있음')
    elif(y<0):
        print('4사분면에 있음')
elif(x<0):
    if(y>0):
        print('2사분면에 있음')
    elif(y<0):
        print('3사분면에 있음')
```

***

### Q3.	사용자로부터 점수를 입력받은 다음 게임 사용자의 게임점수(game_score)가 1000점 이상이면 ‘고수입니다.’를 출력하고 1000점 미만이면 ‘입문자입니다.’를 출력하는 프로그램을 if-else문을 이용하여 작성하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q3.py)

![image](https://user-images.githubusercontent.com/114078946/196036968-715ca822-3347-4c00-8aff-e2cddb984552.png)
![image](https://user-images.githubusercontent.com/114078946/196036972-f00b1bcc-27a3-41df-87f2-2f6dc7cd66dc.png)

##### 풀이 및 해설

input을 통해 game_score에 게임점수를 입력 받습니다.

```python
game_score=int(input('게임점수를 입력하시오 : '))
```

그다음 if문으로 game_score<1000인경우'입문자입니다.', 아닌경우 '고수입니다.'를 출력하도록 합니다.

```python
if(game_score<1000):
    print('입문자입니다.')
else:
    print('고수입니다.')
```

***

### Q4.	다음의 프로그램은 어떤 결과 값을 출력하는가? 출력결과를 미리 예측한 후 타이핑하여 그 결과가 맞는지 확인해 보도록 하자. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q4.py)

#### 1)
```python
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN!')
```

##### 풀이 및 해설

for문에 의해 3번 반복되므로 아래와 같이 출력됩니다.

주의할점은 들여쓰기 된 부분까지만 반복된다는 점입니다.

```python
Python 
is
FUN!
Python
is
FUN!
Python
is
FUN!
```

#### 2)

```python
for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')
```

##### 풀이 및 해설

들여쓰기가 된 부분까지 for문으로 반복이 됩니다.

즉, 아래와 같이 출력됩니다.

```python
Python 
is
Python
is
Python
is
FUN!
```

***

### Q5.	소수란 양의 자연수 중에서 1과 자기 자신이외의 약수를 가지지 않는 수를 말한다. 사용자로부터 양의 정수 n을 입력받은 후 이 숫자가 소수인지 아닌지를 판별하는 프로그램을 작성하시오. 이때 수행 속도를 개선하기 위하여 2로 나누어 본 후 나누어지지 않을 경우 3, 5, 7, … 과 같은 홀수로 나눗셈을 시도하도록 코딩하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q5.py)
-	힌트: n을 2부터 n-1까지의 정수로 모두 나누어 본다. 이 때 나누어 떨어지는 원소가 하나라도 있으면 소수가 아니다.

![image](https://user-images.githubusercontent.com/114078946/196037199-23a3f213-5629-4ca7-abd6-beb2a8db1ff0.png)

##### 풀이 및 해설

먼저 n에 정수를 입력 받습니다.

```python
n=int(input('숫자를 입력하세요 : '))
```

n이 소수이려면 1<i<n에 존재하는 모든 i에 관해 나누어졌을때, 나머지가 0이 아니어야합니다.

즉 for문으로 나눠보면서 나머지가 0이 나오면 소수가 아니라고 출력하고 break하고,

끝까지(n-1)까지 문제없이 나머지가 0이 아니라면 소수라고 출력하면 됩니다.

```python
for i in range(2,n):
    if(n%i==0):
        print(n,'는 소수가 아닙니다.')
        break
    else:
        if(i==n-1):
            print(n,'는 소수입니다.')
```

***

### Q6.	암스트롱 수란 세 자리의 정수 중에서 각 자리의 수를 세제곱한 수의 합과 자신이 같은 수를 말한다. 구체적인 예를 들면 153은 1 + 125 + 27 의 합으로 구성될 수 있는데 이러한 수가 암스트롱 수이다. 세 자리 정수들 중에서 모든 암스트롱 수를 구하여 다음과 같이 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q6.py)
        
![image](https://user-images.githubusercontent.com/114078946/196037392-dc1be84e-bcab-49b0-8f32-17d1c8a22c3e.png)

##### 풀이 및 해설

세자리 정수중에서란 조건이 붙었으니 for문에서 i범위를 range(100,1000)으로 하면 됩니다.

또 백의자리는 100으로 나눈 몫,

십의자리는 100으로 나눈 나머지를 10으로 나눈 몫,

일의 자리는 10으로 나눈 나머지라는 점을 이용해서 코드를 짜면 아래와 같이 나옵니다.

```python
st=''
for i in range(100,1000):
    if((i//100)**3+(i%100//10)**3+(i%10)**3==i):
        st+=' '+str(i)

print('세 자리의 암스트롱 수 :',st)
```

예제와 같이 출력하려면 st를 통해 str형식으로 출력해야 할것 같습니다.

***

### Q7.	다음과 같이 사용자로부터 1에서 9사이의 숫자를 입력받아 입력받은 숫자의 절에 해당하는 구구단을 출력하는 프로그램을 for문과 while 문을 사용하여 작성하여라. 만일 1에서 9 이외의 숫자가 입력되면 ‘1에서 9까지의 수를 다시 입력하세요’라는 안내문을 출력하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q7.py)

![image](https://user-images.githubusercontent.com/114078946/196037628-d371866d-ede5-4f84-b33c-37e1a019809e.png)

먼저 1에서 9사이의 숫자를 입력 받으려면 while문을 통해 올바른 값이 입력될때까지 입력 받다가 올바른 값인 경우 break 통해 반복문을 종료하면됩니다.

```python
n=int(input('1에서 9까지의 수를 입력하세요:'))

while(1):
    if(n>0 and n<10):
        break
    else:
        n=int(input('1에서 9까지의 수를 다시 입력하세요:'))
```

이후 for문을 통해 구구단 형식을 출력하면 됩니다.

```python
for i in range(1,10):
    print(n,'*',i,'=',n*i)
```

***

### Q8.	맛나 식당의 메뉴 주문 프로그램을 개발하고자 한다. 이를 위해 사용자에게 다음과 같은 메뉴를 보여주고 이중에서 메뉴에 대응되는 하나의 알파벳을 선택하도록 하자. 이때 메뉴에 없는 알파벳이 입력되면 ‘메뉴를 다시 입력하세요:  ’가 출력되도록 한 후 다시 입력을 받도록 하자. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q8.py)

![image](https://user-images.githubusercontent.com/114078946/196037749-1984d359-102d-4b14-b731-0d4d19970c50.png)

##### 풀이 및 해설

메뉴 선택까지 예시에서 보여준 멘트 그대로 출력하면서 입력받습니다.

```python
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print(' - 삼겹구이 (입력 s)')
print(' - 오삼불고기 (입력 o)')
print(' - 된장찌개 (입력 d)')

str=input('메뉴를 선택하세요(알파벳 s,o,d 입력) : ')
```

이후 while문을 통해 제대로 입력 받았다면 break하고, 아니면 반복해서 다시 입력받는 코드를 아래와 같이 짜면 됩니다.

```python
while(1):
    if(str=='s'):
        print('삼겹구이를 선택하였습니다.')
        break
    elif(str=='o'):
        print('오삼불고기를 선택하였습니다.')
        break
    elif(str=='d'):
        print('된장찌개를 선택하였습니다.')
        break
    else:
        str=input('메뉴를 다시 입력하세요 : ')
```

***

### Q9.	이중 for 문을 사용하여 숫자를 입력 받아 다음과 같은 삼각형을 출력하는 프로그램을 작성하시오. 이때 아래 결과와 같이 숫자 10이 입력되면 높이가 10이고 제일 마지막 줄의 별이 10개가 삼각형 형태로 나타나도록 하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q9.py)
힌트: 첫번째줄은 공백 9개, 별1개 / 마지막줄은 공백이 없다. 

![image](https://user-images.githubusercontent.com/114078946/196037815-3875ad1e-aa63-4b81-8cb8-502c859a7edd.png)

먼저 숫자를 입력 받습니다.

```python
n=int(input('숫자를 입력하세요 : '))
```

그다음 예시에 있는걸로 생각해본다면

n=10인경우

1번쨰 줄은 공백 9, 별 1

2번쨰 줄은 공백 8, 별 2

...

10번째 줄은 공백 0, 별 10 라는 형식으로 만들어집니다.

먼저 10줄이 반복되어야 하므로

for i in range(1,11)을 먼저 만들고 이후를 생각한다면

i=1인경우 공백 9, 별 1이 만들어져야 하므로

공백은 for j in range(n-i) 한다면 9번 반복하게 되고,

별은 for j in range(i) 한다면 1번 반복하게 됩니다.

위처럼 코드를 만들면 아래와 같이 나옵니다.

```python
for i in range(1,n+1):
    st=''
    for j in range(n-i):
        st+=' '
    for j in range(i):
        st+='*'
    print(st)
```

***

### Q10.	사용자로부터 숫자 1보다 크고 10보다 작은 값 n을 입력으로 받아서 다음과 같이 뱀의 몸통처럼 증가하는 이차원 배열을 출력하여라. (이 배열은 마치 뱀의 몸통처럼 ‘ㄹ’과 같은 패턴을 그리며 수가 1씩 증가하는 형태의 배열이다.)  [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/3%EC%A3%BC%EC%B0%A8/EXERCISE/Q10.py)

![image](https://user-images.githubusercontent.com/114078946/196038034-0614e98b-ca24-4ebd-aae1-b0c0a117a4e9.png)
![image](https://user-images.githubusercontent.com/114078946/196038036-c6014a21-8961-44e5-a390-4f797980b3c0.png)


##### 풀이 및 해설

먼저 n을 입력받습니다.

```python
n=int(input('n을 입력하시오 : '))
```

n을 첫번째 예시처럼 5라고 생각한다면 

for i in range(5)만큼 반복하는거고, i가 홀수인 경우만 역순으로 숫자가 커집니다.

설명이 복잡하니 코드 먼저 보여드리겠습니다.

```python
for i in range(n):
    if(i%2==0):
        st=''
        for j in range(1,n+1):
            st+=str(n*i+j)+'\t'
        print(st)
    else:
        st=''
        for j in range(0,n):
            st+=str(n*i+n-j)+'\t'
        print(st)
```

for i in range(n): 부분은 n으로 입력받은 만큼 행이 만들어지는 것이고,

if 와 else로 나뉘는 부분이 숫자가 오름차순일지, 내림차순일지 결정하는 부분입니다.

i를 기준으로 짝수면(0 포함) 오름차순, 홀수면 내림차순으로 만들어지게 만들었습니다.

***











