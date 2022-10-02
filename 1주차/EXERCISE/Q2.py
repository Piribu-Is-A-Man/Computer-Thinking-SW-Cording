print('Hello Phyton!')
#NameError: name 'Print' is not defined. Did you mean: 'print'?
#정의되지 않았다는 오류. P를 소문자로 변환하면 해결됨.
print("Hello Python")
#SyntaxError: unterminated string literal
#"로 시작하였다면 "로 마무리를,'로 시작하였다면 '로 마무리를 하면 해결됨.
print('Hello Python!')
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
#직역하자면 문법 오류, 구문 오류. 
#프로그래밍 언어로 이해하기 위해선 위에 나온 의무문 같이 콤마를 추가해야함.
#수정1
#print('Hello Python!')

print(100+'200')
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#정수와 문자열끼린 더할순 없다는 의미, 
#수정1) 정수로 생각해 수정할 경우
#print(100+200)
#수정2) 문자열로 생각해 수정할 경우
#print('100'+'200')