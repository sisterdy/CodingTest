def solution(nums):
    solution = set(nums)  # nums 배열을 set으로 변환 (중복 제거)
    return min(len(solution), len(nums) // 2)  
    """ set의 크기(len(solution)) = 폰켓몬 종류 수 와
     배열 길이 // 2 = 선택할 수 있는 최대 마리 수 중
     더 작은 값을 반환 """

def solution(nums):
    solution = set(nums)  # nums 배열을 set으로 변환 (중복 제거)
    return min(len(solution), len(nums) // 2)  
    """ set의 크기(len(solution)) = 폰켓몬 종류 수 와
     배열 길이 // 2 = 선택할 수 있는 최대 마리 수 중
     더 작은 값을 반환 """
