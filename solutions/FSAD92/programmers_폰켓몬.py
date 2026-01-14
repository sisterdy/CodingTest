"""
N/2 마리를 선택 가능한 상황에서
가장 많은 종류의 포켓몬을 선택하는 방법을 찾는 것

주어진 nums를 for문으로 순회
리스트 poncket 만들고
리스트 개수가 0일 때 또는 poncket[-1]이 nums[x]의 값과 같지 않으면 poncket[-1]에 append
만약 len(poncket) == len(nums) / 2가 되면
for문을 빠져나옴

근데 이렇게 하면
1,2,1,2,3,3 같은 케이스는 커버가 안 되지 않나?
이미 poncket에 1,2가 있음에도 불구하고 세번째 원소인 1이 poncket[-1](이건 당연히 2일 거고)의 값과 같지 않으니까 poncket에 append가 된다...
즉 가장 많은 종류의 포켓몬을 선택할 수 없음

이걸 방지하려면 어떻게 해야하는가?
nums를 순회하면서 해당 값이 poncket에 있는지 체크해야 한다.
poncket에 없을 경우에만 append 한다.

근데 이렇게 하면 이중 for문이 돼서 너무 시간이 오래 걸릴 거 같은데

아니면 nums를 set으로 바꿀까? 그러면 nums에 중복된 값이 있는지 체크할 필요가 줄어들잖아
그리고 다시 list로 바꾸는 거지

기존 코드

def solution(nums):
    answer = 0
    nums_list = list(set(nums))
    poncket = []
    
    for x in nums_list:
        if len(poncket) == 0:
            poncket.append(x)
        elif len(poncket) < (len(nums) / 2):
            poncket.append(x)
        elif len(poncket) <= (len(nums) / 2):
            break
            
    answer = len(poncket)
    return answer
"""
def solution(nums):
    nums.sort() # 오름차순 정렬
    count = 1   # 포켓몬 종류 초기화(종류는 최소 1 이상의 자연수...)
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            count += 1
            
    return min(count, len(nums) // 2)