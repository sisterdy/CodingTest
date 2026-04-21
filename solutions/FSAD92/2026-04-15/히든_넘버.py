"""
모든 히든 넘버의 합을 구한다!
간단한 문제인 줄 알았으나 연속된 숫자를 처리해야 한다.

for문을 돌며 숫자를 만나면 temp에 '문자'로 추가한다.
만약 i가 n-1 보다 작거나 같고, word[i+1]이 numbers에 속하지 않는다면 sum에 temp를 int로 변형 후 추가한다.
"""
import sys
n = int(sys.stdin.readline().strip())
word = sys.stdin.readline().strip()

sum = 0
i = 0
temp = ''
numbers = ['0','1','2','3','4','5','6','7','8','9']

for i in range(n):
    if word[i] in numbers:
        temp += word[i]

        if i <= (n - 2) and word[i + 1] not in numbers:
            sum += int(temp)
            temp = ''
        
    i += 1

# 위 for문에서 temp에는 추가되었지만 알파벳을 만나지 않아 출력되지 않은 잔여 문자 처리
if temp:
    sum += int(temp)

print(sum)