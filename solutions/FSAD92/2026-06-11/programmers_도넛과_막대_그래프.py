"""
result에는 들어가야 할 것이 많다.
생성한 정점의 번호, 도넛 모양 갯수, 막대 모양 갯수, 8자 모양 갯수.

일단 그래프의 모든 정점들을 확인해야 할 것 같다.
1. 도나쓰 : 각 노드는 1개가 나가고 1개가 들어온다. 그리고 원래 출발했던 정점으로 돌아온다.
2. 막대 : size가 1일 때는 아무 것도 나가고 들어오는 게 없다.
         size가 2 이상일 때는 시작 정점은 나가는 거만 1, 중간 노드는 나가는 거 1 and 들어오는 거 1, 끝 정점은 들어오는 거만 1
3. 8자 모양 : 중간 노드는 들어오는 거 2 and 나가는 거 2, 나머지 노드는 나가는 거 1 and 들어오는 거 1

'모양' 그래프의 수의 합은 2 이상이라고 되어 있으니까... 생성한 정점은 out이 2이상이고 in이 0인 노드를 찾으면 되는 걸까?

2 -> 3
4 -> 3
1 -> 1
2 -> 1

1 : 1
2 : 1, 3
4 : 3

일단 이 상황에서는 생성한 정점은 2가 된다. 근데 문제에서 이 생성한 정점은 모양 그래프의 임의의 정점을 가리킨다고 했다... 그럼 굳이 모든 노드를 다 돌아봐야 할까?

노드 기준으로 모양 그래프를 다시 정리해보자
1. 도나쓰 : 정점 in=1, out=1
2. 막대 :
    when size = 1, 정점 in=0, out=0
    when size >= 2, 정점 in=1, out=0 or in=0, out=1
3. 8자 : 정점 in=2, out=2(중간 노드), in=1, out=1(양 끝 노드)

순간 정점의 in - out 값으로 판단할까 생각했다가 도나쓰와 8자의 정점의 in - out = 0이 되는 걸 보고 포기

1. edges를 순회하며 in=0, out=2 이상인 '생성된 노드'를 찾고 result에 append 한다.
1-1. 아니, 그냥 append하면 안될 것 같다. result[0]에 저장하자.

아니 근데 문제를 다시 제대로 읽어보니 애초에 모든 노드가 정점이구나. 그럼 굳이 모든 노드를 다 돌아봐야 하네.
그리고 도넛 모양과 8자 모양의 유사성(in=1, out=1)은 어떻게 구분해야 하지? 이게 레벨 2짜리 문제가 맞아?



"""


def solution(edges):
    counts = {} 
    
    for u, v in edges:      # u -> v
        if u not in counts: counts[u] = [0, 0]
        if v not in counts: counts[v] = [0, 0]
        
        counts[u][1] += 1 # out-degree count
        counts[v][0] += 1 # in-degree count

    
    result = [0, 0, 0, 0]   # [생성정점, 도넛, 막대, 8자]
    
    for node in counts:
        in_d, out_d = counts[node]
        
        
        if in_d == 0 and out_d >= 2:    # 생성된 정점은 in=0, out >= 2
            result[0] = node
            
        
        elif out_d == 0:    # 막대 모양의 끝 정점은 나가는 게 0이다. size=1도 포함하기 위해 out_d == 0으로 체크
            result[2] += 1
            
        elif out_d == 2:    # 8자의 중간 노드의 out_d는 반드시 2다. 들어오는 간선은 생성된 정점으로부터 오는 화살표에 의해 바뀔 수 있으니 기준에서 배제.
            result[3] += 1
            
    # 도넛 그래프는 특징적인 노드가 없으므로, 전체 그래프 수에서 나머지를 빼서 계산한다. 
    total_graphs = counts[result[0]][1] # '생성된 정점'에서 나간(out-degree) 화살표의 수를 count
    result[1] = total_graphs - (result[2] + result[3])  # 거기서 막대와 8자를 빼면 그게 곧 도나쓰의 수가 된다.
    
    return result
