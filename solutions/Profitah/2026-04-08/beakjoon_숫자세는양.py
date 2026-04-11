"""
N이 주어진다.
N, 2xN, 3xN 4xN... 을 구하며, 1~9까지의 모든 숫자가 나오면 양은 잠에 들고
N이 0이면 양은 잠에 들지 못한다.

양이 잠에 들때 마지막으로 구한 숫자를 출력한다.

 예) N=1692
      1N=1692  -> {1,6,9,2}
      2N=3384  -> {1,6,9,2,3,8,4}
      3N=5076  -> {1,6,9,2,3,8,4,5,0,7} -> 0~9 모두 수집 -> 5076 출력
"""

# 마지막 숫자를 구하는 함수
def find_last_number(n): #n을 인자로 받는데

    # 마지막 숫자를 구할 수 없는 경우를 우선 생각하자.
    if n == 0: # 만약 n이 0이면 무엇을 곱해도 0이 나오므로
        return "INSOMNIA" # "INSOMNIA (= 불면증)"를 반환하는 것으로 시작.

    # 이후에는
    number_0_9 = set() # 0~9까지의 숫자를 저장할 set을 만들고
    multiplier = 1 # 곱할 수를 1로 초기화한 후 (Nx1 부터 시작해야하니까)

    # 0~9까지의 숫자가 모두 나올 때까지 반복하는 while 루프를 시작한다.
    while len(number_0_9) <=9: # number_0_9의 길이가 9 이하일때
        current = n * multiplier # n * multiplier를 current에 저장하며
        multiplier += 1 # multiplier를 1씩 증가시키고
        collect_digits(current, number_0_9) # 어떠한 함수를 써서 current값을 반환받는다. 
    return current # 이게 뭔지는 아래에 가서 자세히보자 

# current의 각 자릿수를 number_0_9에 추가해서 0~9까지의 숫자를 수집하는 함수
def collect_digits(current, number_0_9):
    for digit in str(current):  # current를 문자열로 변환해 한 글자씩 순회
        number_0_9.add(digit)   # 각 자릿수를 set에 추가 (이미 있으면 자동 무시)

# 입력 처리
def solve():
    t = int(input()) # 첫 번째 줄에서 테스트 케이스의 수 t를 입력받는다.

    for case_idx in range(1, t + 1): # 테스트 케이스에 맞는 출력을 위해 각 테스트 케이스에 대해 1부터 t까지 반복하면서 case_idx를 1씩 증가시킨다.
        n = int(input()) # 각 테스트 케이스마다 n을 입력받는다.
        result = find_last_number(n) # find_last_number 함수를 호출하여 n에 대한 결과를 result에 저장한다.
        print(f"Case #{case_idx}: {result}") # 결과 출력


solve() # solve 함수를 호출하여 프로그램을 실행