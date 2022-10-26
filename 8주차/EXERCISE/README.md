# 8주차: 컴퓨팅사고와 SW코딩

***

### 1.	다음과 같은 내용을 포함하고 있는 greet.txt 파일을 파이썬의 write() 메소드를 이용하여 작성하시오. 이때 greet.txt 파일이 이미 존재할 경우를 가정하고 이 파일이 쓰기 금지 모드(읽기 모드)로 되어 있을 가능성이 있기 때문에 이를 위한 예외처리 기능을 구현하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q1.py)

<greet.txt>

![image](https://user-images.githubusercontent.com/114078946/197965203-e511fd65-5136-4ba1-9566-54502e55c7d1.png)

<읽기 모드 설정 방법: txt 파일 오른쪽 클릭 -> 속성 -> 읽기 전용 체크하기>

<읽기 모드에서 코드 실행 시, 예외 처리를 이용해 다음과 같이 에러 출력하기>

![image](https://user-images.githubusercontent.com/114078946/197965344-580939a2-0ace-4166-8733-08edf8a34fd6.png)

##### 풀이 및 해설

일단 파일이 'w'모드로 생성가능한지, 불가능한지(읽기모드로 이미 파일이 존재하는 경우) 구분해야 합니다.

그러기 위해서 try를 사용할텐데, 생성불가능한 경우를 except, 가능한 경우를 else로 두면 됩니다.

위 사실대로 코드를 짜면 아래와 같이 나옵니다.

```python
try:
    f=open("greet.txt","w")
except Exception as e:
    print('error :',e)
else:
    f.write('Hi, everyone.\n')
    f.write('Welcome to Python.')
    f.close()
```
출력결과1) 'greet.txt' 파일이 읽기모드로 이미 존재할 때
```python
error : [Errno 13] Permission denied: 'greet.txt'
```

출력결과2) 이외의 경우

![image](https://user-images.githubusercontent.com/114078946/197965203-e511fd65-5136-4ba1-9566-54502e55c7d1.png)

***

### 2.	다음과 같은 내용을 포함하고 있는 number1to10.txt 파일을 한 줄씩 읽어들이도록 하여라.

#### (1)	이 파일을 읽어서 각 행의 정수에 곱하기 10을 수행한 후 다음과 같은 numberby10.txt라는 이름의 파일로 저장하여라. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q2-(1).py)

<(좌측) number1to10.txt  &  (우측) numberby10.txt >

![image](https://user-images.githubusercontent.com/114078946/197966636-a1d2e8c0-c604-420c-83db-6f44bbb91698.png) ![image](https://user-images.githubusercontent.com/114078946/197966715-c6faf1a5-2868-487a-9dba-4f4b97f4b2d7.png)

##### 풀이 및 해설

파일이 안열릴 경우를 대비해서 아래와 같이 생각해줍니다.

```python
try:
    #파일오픈
except Exception as e:
    #오류 출력
else:
    #파일에서 숫자 입력받은 후 10곱해서 출력
```

파일 입출력은 str 형으로만 가능한점을 상기하면서 코드를 짜면 아래와 같이 나옵니다.

```python
try:
    f1=open("number1to10.txt","r")
except Exception as e:
    print('error :',e)
else:
    f2=open("numberby10.txt","w")
    for i in range(10):
        num=int(f1.readline())
        f2.write(str(num*10))
        f2.write('\n')
    f1.close()
    f2.close()
```

***

#### (2)	위 두 파일을 읽어서 다음과 같이 각 행의 값을 하나의 내용으로 묶어서 저장하는 프로그램을 작성하여라. 이 파일의 이름은 merge.txt이다. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q2-(2).py)

##### 풀이 및 해설

일단 위의 두 파일을 'r'모드로 열어줍니다.

```python
f1=open('number1to10.txt','r')
f2=open('numberby10.txt','r')
```

다음은 'merge.txt'파일을 'w'모드로 만들어주고 format 메소드로 write해줍니다.

주의할점은 파일에서 입력을 readline()로 읽으면 마지막에 있는 줄바꿈까지 입력됩니다.

그러니 추가적으로 .rstrip()을 입력해서 줄바꿈까지 입력받지 않도록 주의합시다.

(rstrip()을 입력하지 않으면 어떻게 출력되는지도 아래에 보여드리겠습니다.)

전부 입력받았으면 모든 파일을 닫아줍니다.

```python
f3=open('merge.txt','w')
for i in range(10):
    f3.write('{} : {}\n'.format(f1.readline().rstrip(),f2.readline().rstrip()))
f1.close()
f2.close()
f3.close()
```

<merge.txt>

![image](https://user-images.githubusercontent.com/114078946/197968453-c98e379a-a2d7-43f3-84d4-d67664d9b2e5.png)


rstrip()을 입력하지 않은 <merge.txt>

![image](https://user-images.githubusercontent.com/114078946/197968764-46d750dc-695a-4ca4-88b1-60189ec062d2.png)

***

### 3.	“Hello Python”이라는 문자열을 파일로 저장하기 위하여 my_hello.txt 라는 파일을 열고 쓰기를 시도하였다. 이때 이 파일이 이미 존재하고 있으며 문제 1번의 읽기 모드 설정 방법을 참고하여 이미 이 파일이 읽기 모드로 설정되어 있다고 가정한다.

#### (1)	이 상황에서는 어떤 예외가 발생하는지, 실제로 파일을 만들어서 이러한 상황을 테스트하는 프로그램을 작성하여 예외를 출력하여라 [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q3-(1).py)

##### 풀이 및 해설

<출력된 예외상황>

![image](https://user-images.githubusercontent.com/114078946/197969199-3bc009b9-78a9-4bee-ac89-5ca2b98c6d4a.png)

#### (2)	이 예외를 처리하는 try-exception 문을 구현하여라 [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q3-(2).py)

##### 풀이 및 해설

try와 except를 이용해서 예외를 설정하였습니다.

```python
try:
    f=open('my_hello.txt','w')
except(PermissionError):
    print('이미 존재하는 파일을 읽을수가 없습니다.')
```

<출력된 예외상황>

![image](https://user-images.githubusercontent.com/114078946/197969671-8aba74ee-a47b-40d2-ac7b-356bfc9783dd.png)

***

### 4.	다음과 같은 내용을 포함하고 있는 hello.txt 파일을 텍스트 편집기를 이용하여 작성하시오 

<hello.txt>

![image](https://user-images.githubusercontent.com/114078946/197970213-f75bb6b7-6eb6-492e-ad64-98100541862c.png)

#### (1)	이제 이 파일을 open() 함수를 통해 읽어서 이 파일의 내용을 다음과 같이 화면에 출력하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q4-(1).py)

##### 풀이 및 해설

파일을 오픈한 뒤, read()를 이용해 읽어주면 파일 끝까지 읽어냅니다.

```python
f=open('hello.txt','r')
print('hello.txt 파일 : ')
print(f.read())
```

<출력값>

![image](https://user-images.githubusercontent.com/114078946/197970560-b99a6370-7d8d-4d9b-a58d-fc900f2e2448.png)

***

#### (2)	이 파일을 open() 함수를 통해 읽어서 원래 파일의 내용 아래쪽에 ‘Welcome to Python!’을 추가한 후 저장하시오. 그리고 다시 한번 파일을 읽어서 다음과 같이 화면에 출력하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q4-(2).py)

##### 풀이 및 해설

먼저 hello.txt 파일을 'a'형식으로 읽어줍니다.

그렇게 해야 덮어쓰지 않으면서 뒤에 문자열을 추가할 수 있습니다.

```python
f=open('hello.txt','a')
f.write('Welcome to Python!')
f.close()
```

이제 다시 hello.txt 파일을 'r'형식으로 읽어줍니다.

(a+r 형식으로도 열어보고 a+형식으로도 열어봤지만 read()가 제대로 작동하지 않았습니다.

파일을 다시 읽는 것 만이 정답인 듯 합니다.)

```python
f=open('hello.txt','r')
print('hello.txt 파일 : ')
print(f.read())
f.close()
```

<출력값>

![image](https://user-images.githubusercontent.com/114078946/197971221-93df6db6-192c-435c-9d57-8a2e52ce3ce0.png)

***

### 5. 1에서 10사이의 랜덤한 숫자를 30개 가진 randint30.txt 라는 파일을 random 모듈을 사용하여 생성하시오. 이 때 생성한 숫자는 다음과 같이 공백으로 구분하여 나열하시오. [코드](https://github.com/Piribu-Is-A-Man/Computer-Thinking-SW-Cording/blob/master/8%EC%A3%BC%EC%B0%A8/EXERCISE/Q5.py)

![image](https://user-images.githubusercontent.com/114078946/197972016-df233ece-61a1-48ae-9aaa-0552a3619358.png)

**위의 randint30.txt라는 파일을 읽어서 1에서 10까지 정수의 출현횟수를 다음과 같이 출력하여라.**

![image](https://user-images.githubusercontent.com/114078946/197972033-78018eab-ff69-4947-adee-2a3e5e0a9f3d.png)

##### 풀이 및 해설

랜덤한 수를 30개 만드는 함수를 만들긴 위해서, random 모듈을 import 해줍니다.

파일 randint30.txt 를 w로 열어줍니다

rd.randint(1,10) 를 이용하면 1에서 10사이의 랜덤한 숫자를 생성할 수 있으니, for를 이용해 30번 반복해줍니다.

위 처럼 작동하는 함수를 선언해줍니다.

```python
def makeRandInt30():
    f=open('randint30.txt','w')
    for i in range(30):
        f.write('{} '.format(rd.randint(1,10)))
    f.close()
```

이제 생성된 숫자가 어떤 숫자인지 확인 하는 작업이 필요합니다.

randint30.txt를 r로 열어준 후, read()를 통해 문자열 전체를 읽어줍니다.

문자열을 split()을 통해 공백으로 구분한 뒤, 리스트로 정리해줍니다.

```python
a=list(map(int,nums.split()))
```

그다음 for를 통해 각 숫자가 얼마나 있는지 확인해줍니다.

중요한건, count인자로는 str형식만 전달이 가능하니, i를 str로 변환해주어야 합니다.

```python
for i in range(1,11):
        print('{} : {}개'.format(i,nums.count(str(i))))
```

위와같이 함수를 만들어준 다음 각각 한번씩 실행해줍니다.

```python
def readtxt():
    f=open('randint30.txt','r')
    nums=f.read()
    a=list(map(int,nums.split()))
    
    for i in range(1,11):
        print('{} : {}개'.format(i,nums.count(str(i))))
        
makeRandInt30()
readtxt()        
```

<randint30.txt>

![image](https://user-images.githubusercontent.com/114078946/197973964-f80b2fb4-4327-4f73-b18c-746756a0ae1a.png)


<출력값>

![image](https://user-images.githubusercontent.com/114078946/197974039-5a8113c4-0667-482e-ab91-9f8ec26abdc7.png)

***


