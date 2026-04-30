"""
상태 추적을 해야하는 변수는 연속 성공과 시간

만약 현재 체력이 0 이하면 return -1
시간을 1초 추가
    만약 현재 시간에 들어올 공격이 있다면
        연속 성공을 0으로 바꾼다
        그리고 체력에서 해당 공격의 데미지만큼 뺀다
    continue

    만약 현재 시간에 들어올 공격이 없다면
        체력에 x만큼 더한다.
        연속 성공에 1을 더한다.
        만약 연속 성공이 bandage[2]와 같다면
            체력에 추가 회복 y를 더한다.
            연속 성공을 0으로 초기화한다.
    continue
"""
def solution(bandage, health, attacks):
    clock = 0
    success_streak = 0
    player_health = health
    bandage_time, x, y = bandage
    dict_attacks = dict(attacks)
    last_attack_time = attacks[-1][0]
    
    for clock in range(1, last_attack_time + 1):
        
        if clock in dict_attacks:   # 공격이 있으면
            player_health -= dict_attacks[clock]
            success_streak = 0
            
            if player_health <= 0:
                return -1
            
        else:   # 공격이 없으면
            success_streak += 1 
            # 게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능
            player_health = min(health, player_health + x)
            
            if success_streak == bandage_time:
                player_health = min(health, player_health + y)
                success_streak = 0
                
    return player_health