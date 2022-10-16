# 2주차: 컴퓨팅사고와 SW코딩

***

### Q1.	정사각형의 면적을 구하기 위하여 사용자로부터 밑변의 길이를 정수로 입력받아서 다음과 같이 출력하시오(힌트: int(input(‘정사각형의 밑변을 입력하시오 : ‘))를 사용함). [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/2%EC%A3%BC%EC%B0%A8/EXERCISE/Q1.py)

![image](https://user-images.githubusercontent.com/114078946/196032308-92672b00-014a-4b08-8532-0c5c3fd5ab0d.png)

##### 풀이 및 해설

문제 안에 힌트를 먼저 봅니다.

(힌트: int(input('정사각형의 밑변을 입력하시오 : '))를 사용함)라고 적혀있는데 알려준 코드를 활용해서 정사각형의 밑변을 입력 받습니다.

```python
n=int(input('정사각형의 밑변을 입력하시오 :'))
```

위 코드로 입력받은 숫자를 n 변수에 저장했습니다.

그럼 n을 활용해 정사각형의 면적을 출력하기만 하면 됩니다

```python
print('정사각형의 면적 :',n*n)
```

제곱을 활용한다면 아래와 같이 표현할 수 있습니다.

결과는 같습니다.

```python
print('정사각형의 면적 :',n**2)
```

***

### Q2.	섭씨온도(celsius)를 화씨온도(fahrenheit)로 변환하는 식을 바탕으로 사용자로부터 섭씨온도를 입력받아서 다음과 같이 화씨온도로 출력하시오(힌트: int(input(‘섭씨온도를 입력하세요 : ‘))를 사용함). [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/2%EC%A3%BC%EC%B0%A8/EXERCISE/Q2.py)
-	섭씨온도를 화씨온도로 변환하는 공식: fahrenheit = (9/5) * celsius + 32

![image](https://user-images.githubusercontent.com/114078946/196032475-2a5e43cb-1a6a-4d71-ba2d-b00e5a90f6a0.png)

##### 풀이 및 해설

먼저 input을 활용해 섭씨온도를 입력 받습니다.

```python
c=int(input('섭씨온도를 입력하세요 :'))
```

이러면 변수c에 섭씨온도 값이 저장이 됩니다.

힌트에 있는 화씨온도로 변환하는 공식을 통해 화씨온도로 변환 후 출력합니다.

```python
f=(9/5)*c+32
print('섭씨',c,'도는 화씨',f,'도 입니다.')
```

***

### Q3.	비트 이동 연산자를 이용하여 2의 거듭제곱 수 10개를 다음과 같이 출력하라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/2%EC%A3%BC%EC%B0%A8/EXERCISE/Q3.py)
-	힌트: 2 << 0 = 2, 2 << 1 = 4, 2 << 2 = 8

![image](https://user-images.githubusercontent.com/114078946/196032573-321333b1-04a2-44b1-b508-d21d8800711a.png)

##### 풀이 및 해설

힌트에 설명 되어 있듯이, 비트연산자 <<를 사용하면 비트를 기준으로 왼쪽방향으로 이동합니다.

**ex1) 2 << 0**

2를 비트 형식으로 표현하면 0000 0010인데, 여기서 왼쪽으로 0칸 이동한다는 뜻이니 똑같이 0000 0010 즉, 2가 됩니다.

**ex2) 2 << 1**

2를 비트 형식으로 표현하면 0000 0010인데, 여기서 왼쪽으로 1칸 이동한다는 뜻이니 0000 0100 즉, 4가 됩니다.

위 사실을 생각하며 2의 거듭제곱 수를 표현하는 코드를 짠다면 아래와 같습니다.

```python
print(2<<0,2<<1,2<<2,2<<3,2<<4,2<<5,2<<6,2<<7,2<<8,2<<9)
```

***

### Q4.	사용자의 키보드 입력을 통해 n값을 입력받아, 주어진 정수 n이 짝수이면 True, 홀수이면 False를 출력하는 코드를 작성해 보라. n이 20, 21인 경우에 대하여 다음과 같이 출력된다. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/2%EC%A3%BC%EC%B0%A8/EXERCISE/Q4.py)

![image](https://user-images.githubusercontent.com/114078946/196032734-cc6e67ac-990a-46df-8947-20cd77a3a429.png)

##### 풀이 및 해설

이제는 익숙해진 input을 통해 변수n에 정수를 입력받습니다.

```python
n=int(input('정수를 입력하세요 : '))
```

이제 짝수인지, 홀수인지 구분을 해야하는데, 짝수는 2로 나누면 나머지가 0이고, 홀수는 2로 나누면 나머지가 1인것을 이용합니다.

```python
print('이 수가 짝수인가요?',n&2==0)
```

이렇게 코드를 짠다면 n이 짝수인 경우 Treu, n이 홀수인 경우 False를 출력합니다.

***

### Q5.	사용자로부터 세 자리 정수를 입력으로 받으시오. 이때 입력받은 정수 n에 대한 백의 자리, 십의 자리, 일의 자리 십진수 값을 다음과 같이 출력하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/2%EC%A3%BC%EC%B0%A8/EXERCISE/Q5.py)
-	힌트: // 연산자와 % 연산자를 사용하시오. 예를 들어 백의 자리는 n//100을 통해서 구할 수 있다.

![image](https://user-images.githubusercontent.com/114078946/196032852-5d5c6f48-e8df-466a-9458-91ebf8e2ad1d.png)

먼저 input을 통해 세자리 정수를 입력 받습니다.

```python
n = int(input('세 자리 정수를 입력하세요 : '))
```

이제 백의자리, 십의자리, 일의자리 나눠서 출력하면 되는데

백의 자리는 n을 100으로 나눈 몫입니다.

십의 자리는 n을 100으로 나눈 나머지를 10으로 나눈 몫입니다.

일의 자리는 n을 10으로 나눈 나머지입니다.

위 설명대로 코드를 짜면 아래와 같이 나옵니다.

```python
print('백의 자리 :',n//100)
print('십의 자리 :',n%100//10)
print('일의 자리 :',n%10)
```






