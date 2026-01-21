def solution(nums):
    limit = len(nums) // 2
    kinds = len(set(nums))
    answer = min(limit, kinds)

    return answer
