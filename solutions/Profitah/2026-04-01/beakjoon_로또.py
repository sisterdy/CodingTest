"""
로또 번호 조합을 구하는 문제.

문제 설명:
- 첫 번째 입력값 k는 로또 번호 후보의 개수 (6 ≤ k ≤ 12)
- 그 다음 k개의 입력값은 로또 번호 후보 (1 ≤ 번호 ≤ 49
- 6개의 번호를 조합하여 오름차순으로 출력
- 각 테스트 케이스 사이에는 빈 줄 출력

풀이 방식:
- itertools의 combinations 함수를 사용하여 후보 번호에서 6개를 뽑는 모든 조합을 구하고,
  완전탐색으로 각 조합을 출력한다.
- 후보 번호를 오름차순 정렬한 상태로 combinations에 넣으면 출력 결과도 자동으로 오름차순이 된다.



"""


from itertools import combinations 

while True: 
    data = list(map(int, input().split())) # data라는 리스트 요소값을 공백을 기준으로 구분, 정수로 입력받아 넣음. 
    
    if data[0] == 0:  # 첫 번째 값(k)이 0이면
        break # while루프 종료

    k = data[0] # 리스트 data의 첫번째 값을 k라 칭하고
    nums = data[1:] #나머지 data 요소는 nums라 칭한 뒤 

    for comb in combinations(nums, 6):  # nums에서 6개를 뽑는 모든 조합 순서대로(오름차순) 탐색
        print(*comb)  # 조합을 공백으로 구분해서 한 줄 출력
    print()  # 각 테스트케이스 사이 빈 줄 출력
