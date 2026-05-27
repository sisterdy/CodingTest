"""
video_len, pos, op_start, op_end를 일단 초단위로 변환할까?
"""
def toSeconds(str_time):
    minute, second = map(int, str_time.split(':'))
    return minute * 60 + second

def toMinutesAndSeconds(total_seconds):
    minute = total_seconds // 60
    second = total_seconds % 60
    return f"{minute:02d}:{second:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    curr = toSeconds(pos)
    video_limit = toSeconds(video_len)
    opening_start = toSeconds(op_start)
    opening_end = toSeconds(op_end)
    
    # 명렁 실행 전에 현재 pos(curr)이 오프닝 범위 안에 있는지 체크
    if opening_start <= curr <= opening_end:
        curr = opening_end
    
    for cmd in commands:
        if cmd == 'next':
            curr = min(video_limit, curr + 10)
        elif cmd == 'prev':
            curr = max(0, curr - 10)
                         
        if opening_start <= curr <= opening_end:
            curr = opening_end
                         
    
    return toMinutesAndSeconds(curr)