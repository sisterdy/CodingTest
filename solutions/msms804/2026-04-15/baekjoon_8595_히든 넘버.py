import sys

n = int(sys.stdin.readline())
# for문을 돌면서 숫자인지 체크 


word = sys.stdin.readline()

answer = 0
num = ""

for w in word:
    if '0' <= w <= '9':
      num += w
    else: 
      if num != "": # 빈 문자열이 아닐때만 더하기
        answer += int(num)
        # 알파벳을 만나면 num을 리셋
        num = ""

print(answer)