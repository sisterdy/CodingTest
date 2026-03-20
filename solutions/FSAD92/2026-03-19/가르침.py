"""
뭐라는 거지...?
백준에는 이상하게 지민이라는 이름이 많이 나온다...


anta tica
북극의 단어들을
k개의 알파벳을 배웠을 때
몇 개의 주어진 단어를 읽을 수 있는지
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

if K < 5:
    print(0)
    raise SystemExit

if K == 26:
    print(N)
    raise SystemExit

mandatory = {'a', 'n', 't', 'i', 'c'}   # 적어도 이 글자는 알아야 anta와 tica를 읽을 수 있음
learned = set(mandatory)

word_needs = []
candidate_set = set()

for word in words:
    middle = word[4:-4]   # anta / tica 제거
    need = set()

    # b
    for ch in middle:
        if ch not in mandatory:
            need.add(ch)

    word_needs.append(need)
    candidate_set.update(need)

candidate_letters = list(candidate_set)

if len(candidate_letters) <= K - 5:
    print(N)
    raise SystemExit

max_readable = 0
target = K - 5

def count_readable():
    count = 0

    for need in word_needs:
        can_read = True

        for ch in need:
            if ch not in learned:
                can_read = False
                break

        if can_read:
            count += 1

    return count

def dfs(index, chosen_count):
    global max_readable

    if chosen_count == target:
        readable = count_readable()
        if readable > max_readable:
            max_readable = readable
        return

    if index == len(candidate_letters):
        return

    remaining = len(candidate_letters) - index
    if chosen_count + remaining < target:
        return

    ch = candidate_letters[index]

    learned.add(ch)
    dfs(index + 1, chosen_count + 1)    # 글자를 배운 경우
    learned.remove(ch)

    dfs(index + 1, chosen_count)    # 글자를 안 배운 경우

dfs(0, 0)
print(max_readable)