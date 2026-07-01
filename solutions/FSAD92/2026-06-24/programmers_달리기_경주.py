"""
자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부름
현재 등수 순서와 해설진이 부른 이름을 담은 배열을 토대로
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return

매번 replace 하는 건 좀 그런데
연결리스트를 써서 해결할까

player의 앞 선수를 저장할 prev
player의 뒷 선수를 저장할 nxt

before - cur - front - after
"""

def solution(players, callings):
    prev = {}
    nxt = {}

    for i, name in enumerate(players):
        if i == 0:
            prev[name] = None
        else:
            prev[name] = players[i - 1]

        if i == len(players) - 1:
            nxt[name] = None
        else:
            nxt[name] = players[i + 1]

    head = players[0]

    for cur in callings:
        front = prev[cur]

        if front is None:
            continue

        before = prev[front]
        after = nxt[cur]
        
        # 연결 리스트라 cur의 앞이 없다는 것은 cur이 head라는 것.
        if before is None:
            head = cur
        else:
            nxt[before] = cur

        prev[cur] = before
        nxt[cur] = front

        prev[front] = cur
        nxt[front] = after

        if after is not None:
            prev[after] = front

    result = []
    cur = head

    while cur is not None:
        result.append(cur)
        cur = nxt[cur]

    return result
