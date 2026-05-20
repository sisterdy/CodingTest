"""
구해야 할 것 : 커맨드 입력시 결과값

각 커멘드에 맞는 동작을 정의한다.
단, 문자열은 5이상이 되어서는 안된다. (ex : 01:12 === 5 (가능)

2001:10:21 === 10 (불가능))


"""


def solution(video_len, pos, op_start, op_end, commands):

    # mm:ss -> 초 변환
    def to_seconds(time):
        mm, ss = map(int, time.split(":"))
        return mm * 60 + ss

    # 초 -> mm:ss 변환
    def to_time(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{mm:02d}:{ss:02d}"


    # 문자열 시간을 초로 변환
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)


    # 현재 위치가 오프닝 구간이면 스킵
    if op_start <= pos <= op_end:
        pos = op_end


    # 명령 실행
    for command in commands:

        # 10초 전
        if command == "prev":
            pos -= 10

            # 0초보다 작아지면 0초
            if pos < 0:
                pos = 0


        # 10초 후
        elif command == "next":
            pos += 10

            # 영상 길이 초과 방지
            if pos > video_len:
                pos = video_len


        # 이동 후 오프닝 구간이면 스킵
        if op_start <= pos <= op_end:
            pos = op_end


    # 다시 mm:ss 형태로 변환
    return to_time(pos)