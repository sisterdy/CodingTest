"""
입력 X는 8, 10, 16진수 중 하나인데 이걸 10진수로 변환해야 한다.

8진수는 앞에 0
16진수는 앞에 0x

10진수 변환 방법은 int('str', 바꾸고 싶은 진수)
"""
import sys
num = sys.stdin.readline().strip()

if num[0] == '0':   # 앞에가 0이고
    if num[1] == 'x':   # 앞에서 두 번째가 x면 16진수다.
        print(int(num, 16))
    else:   # 아니면 8진수다
        print(int(num, 8))
else:   # 앞에가 0이 아니면 10진수다.
    print(int(num))
