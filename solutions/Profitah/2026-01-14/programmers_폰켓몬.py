def solution(nums):
    solution = set() #리스트를 set으로 변경 (자동중복제거, 서로 다른 원소의 개수를 바로 구할 수 있는 자료구조)
    
    for num in nums:
        solution.add(num) # 입력받은 값을 차례대로 set에 추가
    
    return min(len(solution), len(nums) // 2) # (서로 다른 종류 수)와 (고를 수 있는 최대 마리 수 = 전체의 절반) 중 더 작은 값을 반환 (= 최대 N/2마리 선택가능임으로)
