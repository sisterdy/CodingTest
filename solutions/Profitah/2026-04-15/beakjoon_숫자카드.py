"""
[문제]
숫자 카드 목록에 특정 숫자가 존재하는지 확인.

[출력]
각 숫자에 대해
있으면 1, 없으면 0 출력.

[풀이]
카드 정렬 → 이진 탐색으로 존재 여부 확인.


"""




import sys
input = sys.stdin.readline

N = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
num = list(map(int, input().split())) # 숫자 카드에 적혀 있는 정수의 값
M = int(input()) # 상근이가 이 숫자를 가지고 있는지 아닌지를 확인한다.
my_cards = list(map(int, input().split())) # 이 숫자들 중에 상근이가 가지고 있는 숫자 카드가 있는지 없는지 확인한다.
num = sorted(num) # 리스트 정렬

# 이진탐색을 위한 변수 
pl = 0 # 리스트 왼쪽
pr = len(num) # 리스트 오른쪽
result = 0 # 결과값 저장

for i in my_cards:
    pl = 0
    pr = len(num) - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        if num[pc] == i:
            result = 1
            break
        elif num[pc] < i:
            pl = pc + 1
        else:
            pr = pc - 1
    print(result, end=' ')
    result = 0
print()