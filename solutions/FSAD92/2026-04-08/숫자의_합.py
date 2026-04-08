import sys

n = int(sys.stdin.readline().strip())
num = sys.stdin.readline().strip()
sum = 0

for i in range(n):
    sum += int(num[i])

print(sum)