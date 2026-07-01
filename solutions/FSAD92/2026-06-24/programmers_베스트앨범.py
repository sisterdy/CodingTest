"""
장르마다 베스트 2곡만 저장
순회중 1,2등만 갱신

딱 순위표 2칸만 유지하는 느낌
"""
def solution(genres, plays):
    genre_total = {}
    genre_best = {}

    def is_better(song_a, song_b):
        if song_b is None:
            return True

        play_a, index_a = song_a
        play_b, index_b = song_b

        if play_a != play_b:
            return play_a > play_b

        return index_a < index_b

    for index, genre in enumerate(genres):
        play = plays[index]
        current_song = (play, index)

        if genre not in genre_total:
            genre_total[genre] = 0
            genre_best[genre] = [None, None]

        genre_total[genre] += play

        first_song = genre_best[genre][0]
        second_song = genre_best[genre][1]

        if is_better(current_song, first_song):
            genre_best[genre][0] = current_song
            genre_best[genre][1] = first_song

        elif is_better(current_song, second_song):
            genre_best[genre][1] = current_song

    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda genre: genre_total[genre],
        reverse=True
    )

    answer = []

    for genre in sorted_genres:
        for song in genre_best[genre]:
            if song is not None:
                play, index = song
                answer.append(index)

    return answer
