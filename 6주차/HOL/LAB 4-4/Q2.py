#2. [코드4-5]를 수정하여 별표(*) 표시 대신 해시마크(#)가 출력되도록 하시오.
#   이를 위해 함수 이름을 print_hash(n)으로 수정하고 수정된 함수를 print_hash(10)과 같이 호출하시오.

def print_hash(n):
    for _ in range(n):
        print('####################')

print_hash(10)