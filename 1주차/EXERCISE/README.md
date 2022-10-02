# 01주차: 컴퓨팅사고와 SW코딩
***

## **Q1. 다음 파이썬 코드의 출력결과는 무엇인가?** [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/1%EC%A3%BC%EC%B0%A8/EXERCISE/Q1.py)

![image](https://user-images.githubusercontent.com/114078946/193454780-69980d5c-f817-4820-b11c-e1e782731c53.png)

##### **풀이 및 해설**
```python
(1) print(100+200)
```
값의 합을 ''없이 표현했으니 결과값인 300이 출력됩니다.

출력값 : 300


```python
(2) print('100 + 200')
```
''를 통해 표현하였으니 ''안에 있는 문자 그대로 출력됩니다.

출력값 : 100 + 200
```python
(3) print(100, 200)
```
,를 통해 표현하였으니 100 200라고 출력됩니다.

출력값 : 100 200

```python
(4) print('100','200')
```
''안에 있는 문자 그대로 출력되나 ,를 기점으로 스페이스바 포함되어 출력됩니다.

출력값 : 100 200

```python
(5) print('Hello','Python','!')
```
위와 동일하게 ''사이엔 공백을 두고 출력됩니다.

출력값 : Hello Python !

```python
(6) print('Hello' + 'Python'+'!')
```
''안에 있는 문자가 출력되나 사이에 공백 없이 출력됩니다.

출력값 : HelloPython!
```python
(7) print('Hello''Python''!')
```
위와 동일하게 ''사이에 공백 없이 출력됩니다

출력값 : HelloPython!
```python
(8) print('*'*10)
```
''안에 있는 문자를 10번 반복해서 출력됩니다.
출력값 : **********

***
## **Q2. 다음 코드들은 어떤 오류를 출력하는가? 실행시 나타나는 오류를 적고, 이 오류를 수정한 후 실행시켜 보시오.** [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/1%EC%A3%BC%EC%B0%A8/EXERCISE/Q2.py)
 
 
 ![image](https://user-images.githubusercontent.com/114078946/193455438-1547ccb6-40ce-480c-b873-97173f5633ff.png)


##### **풀이 및 해설**
```python
(1) Print('Hello Phyton!')
```
NameError: name 'Print' is not defined. Did you mean: 'print'?

'Print'라는 함수가 정의되어 있지 않아서 생기는 오류입니다.

실존하는 print함수로 이름을 변경하던가, 직접 'Print'라는 함수를 정의해서 해결할 수 있습니다.

* 해결방법1 : print함수 이용하기
```python
print('Hello Pyhton!')
```
* 해결방법2 : 함수 'Print' 선언하기

(5주차 내용 습득후 수정예정)

```python
(2) Print('Hello Phyton!')
```
SyntaxError: unterminated string literal

직역하자면 구문오류, 문법오류 입니다.

'로 시작하였다면 '로, "로 시작하였다면 "로 포괄해야 위와 같은 오류가 발생하지 않습니다.

* 해결방법1 : '로 통일하기
```python
print('Hello Phyton!')
```

* 해결방법2 : "로 통일하기
```python
print("Hello Phyton!")
```

```python
(3) print(Hello Python!)
```
SyntaxError: invalid syntax. Perhaps you forgot a comma?

이또한 구문오류, 문법오류로 위 의문문에 나와있듯 '(콤마)나 "를 추가해야 합니다.

* 해결방법1 : ' 추가하기
```python
print('Hello Phyton!')
```

* 해결방법2 : " 추가하기
```python
print("Hello Phyton!")
```

```python
(4) print(100 + '200')
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
형오류로 정수와 문자열끼린 더할 순 없다는 의미입니다. 형을 통일시켜주면 해결됩니다.
* 해결방법1 : 'int'형으로 통일하기
```python
print(100+200)
```
* 해결방법2 : 'str'형으로 통일하기
```python
print('100+200')
```
***
## ** 3. 50과 30 두 값이 있을 경우, 이 값에 대한 사칙 연산을 다음과 같이 수행하는 프로그램을 작성하시오. 이때 각 출력문은 print(‘1 + 1 = ‘, 1 + 1)과 같이 출력문과 연산을 쉼표로 구분하시오.** [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/1%EC%A3%BC%EC%B0%A8/EXERCISE/Q3.py)

![image](https://user-images.githubusercontent.com/114078946/193456594-65fc2cc6-d03c-42cf-b68d-53884d9fdbbf.png)


##### ** 풀이 및 해설

문제 안에 답이 있습니다.

문제에서 알려준대로 출력문과 연산을 쉼표로 구분해 출력하면 됩니다.
```python
print('50 + 30 =',50 + 30)
print('50 - 30 =',50-30)
print('50 * 30 =',50*30)
print('50 / 30 =',50/30)

출력값
50 + 30 = 80
50 - 30 = 20
50 * 30 = 1500
50 / 30 = 1.6666666666666667
```
***
## ** 4. 다음과 같이 출력되도록 triangle.py라는 프로그램을 작성한 후 파이썬 인터프리터에서 실행해 보시오.** [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/1%EC%A3%BC%EC%B0%A8/EXERCISE/Q4.py)

![image](https://user-images.githubusercontent.com/114078946/193456766-1a6987eb-3769-4d8d-9088-eed937a9d798.png)

##### ** 풀이 및 해설

* 해결방법1 : print 여러번 사용하기
```python
print('   *   ')
print('  ***  ')
print(' ***** ')
print('*******')

출력값
   *   
  ***
 *****
*******
```
단순하지만 확실한 코딩방법입니다.

효율적이라고 할 순 없지만 문제에서 주어진 상황을 가장 단순하고 정확하게 표현할 수 있는 방법이 아닌가 싶습니다.

* 해결방법2 : for문 사용해 출력하기
```python
for i in range(4):
    print(' '*(3-i)+'*'*(2*i+1)+' '*(3-i))
    
출력값
   *   
  ***
 *****
*******
```
위에있는 1주차 예제문제 1번과 4주차까지의 for문을 제대로 이해했다면 위 코드도 이해하기 쉬울 것 같습니다.

문자열끼리의 +연산도 가능함과 동시에 for문안의 i를 통해서 공백과 * 의 길이도 조절이 가능합니다.
***
## ** 5.n 팩토리얼은 n * (n-1) * (n-2) * ... * 2 * 1로 정의한다. 이 정의를 바탕으로 다음 값을 구하는 프로그램을 작성해 보시오. ** [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/1%EC%A3%BC%EC%B0%A8/EXERCISE/Q5.py)

(1) 3!

(2) 5!

(3) 12!

(4) 20!

##### ** 풀이 및 해설

* 해결방법1 : 나열
```python
print('3!=',3*2*1)
print('5!=',5*4*3*2*1)
print('12!=',12*11*10*9*8*7*6*5*4*3*2*1)
print('20!=',20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)

#출력값
3!= 6
5!= 120
12!= 479001600
20!= 2432902008176640000
```
위 예제문제 4번에서도 봤듯이 가장 단순하지만 확실한 코딩방법 입니다.

하지만 팩토리얼을 구하는 숫자가 커지면 커질수록 코딩하기는 힘들어 질 것입니다. ex)100!=? 5000!=? 1000000!=?

그래서 이후에 보여드리는 for문으로 해결하는 방법이 더 좋다고 생각이 듭니다.

* 해결방법1 : for문 사용하기
```python
num=3
fac=1
for i in range(0,num):
    fac=fac*(i+1)
print(num,'! = ',fac)

num=5
fac=1
for i in range(0,num):
    fac=fac*(i+1)
print(num,'! = ',fac)

num=12
fac=1
for i in range(0,num):
    fac=fac*(i+1)
print(num,'! = ',fac)

num=20
fac=1
for i in range(0,num):
    fac=fac*(i+1)
print(num,'! = ',fac)

#출력값
3 ! =  6
5 ! =  120
12 ! =  479001600
20 ! =  2432902008176640000
```
for문을 통해서 팩토리얼 이후로 나열될 숫자를 일일히 입력하지 않아도 될 뿐만 아니라, 

더 큰 숫자를 넣어서 팩토리얼을 구하더라도 num의 숫자만 변경해 준다면 쉽게 구할 수 있습니다.
***
***
***

######수정날짜 221002
