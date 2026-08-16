# 제일 멀리있는 집부터

def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0 # 배달 남은 양
    pickup = 0 # 수거 남은 양
    
    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            # i 번까지 가야함
            answer += (i + 1) * 2
            
            # 한번 왕복하면서 cap만큼 처리
            delivery -= cap
            pickup -= cap
    
    return answer