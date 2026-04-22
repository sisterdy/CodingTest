"""
단순구현문제

리스트에 값을 입력받고 더한뒤 sort()로 정렬해서 출력했다.

여담으로 중복값 제거 없이 출력해야하는 줄 알고 딕셔너리를 사용했다가
왜 답이 아니지? 하며  뻘짓을 했음...

"""



import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # A배열의 크기 N, B배열의 크기 M

A = list(map(int, input().split())) # A배열의 원소들을 입력받아 리스트로 저장
B = list(map(int, input().split())) # B배열의 원소들을 입력받아 리스트로 저장

nums = A + B # A배열과 B배열을 합쳐서 nums 리스트에 저장
nums.sort() # nums 리스트를 오름차순으로 정렬

print(*nums) # 정렬된 nums 리스트의 요소들만 출력