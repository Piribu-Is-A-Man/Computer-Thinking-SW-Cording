#4. print_hash(6)을 호출하여 다음과 같은 출력이 나타나도록 하여라.
#   다음 화면과 같이 매번 해시가 출력될 때마다 앞 칸에 줄 번호를 0부터 표시하도록 하여라.

def print_hash(n):
    for i in range(n):
        print(i,'####################')

print_hash(6)