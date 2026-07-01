"""
num을 포함해서 그 위의 상자들까지 세기
"""
def solution(n, w, num):
    answer = 0
    warehouse = []
    box = 1
    target_floor = 0
    target_col = 0
    floor = 0
    
    while box <= n:
        row = [0] * n
        
        # 0,2 같은 짝수층(맨 밑을 0층이라고 했을 때)
        if floor % 2 == 0:
            columns = range(w)
        else:
            columns = range(w - 1, -1, -1)
        
        # 상자를 만들어 둔 가상의 빈 공간에 삽입
        for column in columns:
            if box > n:
                break
                
            row[column] = box
            
            # num 발견하면 타겟 위치 저장
            if box == num:
                target_floor = floor
                target_col = column
                
            box += 1
            
        # 현재 층을 다 채웠으면 창고에 넣고
        warehouse.append(row)
        floor += 1      # 윗층으로
        
    for floor in range(target_floor, len(warehouse)):   # num이 위치한 층부터 세기
        if warehouse[floor][target_col] != 0:
            answer += 1
            
    return answer
    
