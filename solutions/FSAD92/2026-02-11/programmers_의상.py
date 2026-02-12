"""
주어진 배열을 재정렬 해야 하나? 해야 한다면 어떻게?
DFS를 사용해야 하나?
DFS를 사용하면서 푸는 도중 시간 안에 풀지 못함

기존 코드 : 
def solution(clothes):
    answer = 0
    n = len(clothes)
    wore = [False] * n
    
    def dfs(clothes, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n):
            if not wore[i]:
                wore[i] = True
                dfs()
    
    return answer

"""
# 이 코드는 정확도는 맞지만, 효율성 테스트에서 100% 시간 초과가 발생합니다.
def solution(clothes):
    # 1. 종류별로 개수 세기 (해시 맵)
    closet = {}
    for _, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1
    
    # 종류 리스트: ['headgear', 'eyewear', ...]
    kinds = list(closet.keys())
    n = len(kinds)
    
    count = 0

    # DFS 함수 정의
    def dfs(index):
        nonlocal count
        
        # 기저 사례: 모든 종류를 다 살펴봤을 때
        if index == n:
            count += 1 # 하나의 조합 완성!
            return

        # 경우의 수 1: 이번 종류의 옷을 입지 않고 넘어감
        dfs(index + 1)
        
        # 경우의 수 2: 이번 종류의 옷 중 하나를 선택해서 입음
        # (해당 종류의 옷 개수만큼의 경우의 수가 발생)
        # 하지만 단순히 개수만 더하는 게 아니라 분기(Branch)를 쳐야 함
        # 여기서 for문을 돌리면 정말로 모든 조합을 다 방문하게 됨 -> 시간 폭발
        for _ in range(closet[kinds[index]]):
            dfs(index + 1)

    dfs(0)
    return count - 1 # 아무것도 안 입은 경우(공집합) 제외