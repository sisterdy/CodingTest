"""
dfs
백트래킹
조합
"""
import sys

cases = []
results = []

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    
    if nums[0] == 0:
        break

    cases.append(nums[1:])

def dfs(start, stack, case):
    if len(stack) == 6:
        results.append(" ".join(map(str, stack)))
        return
    
    for i in range(start, len(case)):
        stack.append(case[i])
        dfs(i + 1, stack, case)
        stack.pop()

for i in range(len(cases)):
    dfs(0, [], cases[i])

    if i < len(cases) - 1:
        results.append("")

print("\n".join(results))