"""
genres와 plays가 같으니까... 둘 중 하나의 n만큼 순회.
순회하면서 genres: (plays, 인덱스) 형태로 딕셔너리에 저장하자.
그러면 classic: (500,0) (150,1) (800,2) 이런 식으로 저장되겠고.

그 다음에 딕셔너리의 키-값에서 '값'의 total의 내림차순으로 genres를 정렬.
정렬된 genres에 해당하는 값들도 내림차순으로 정렬.
그 중에 제일 값이 큰 2개씩만 answer에 append 해서 return

"""

def solution(genres, plays):
    answer = []
    genre_map = {}
    n = len(genres)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_map:
            genre_map[genre] = []
        genre_map[genre].append((play, i))
        
    # 장르 내부 정렬(내림 차순)
    for genre in genre_map:
        genre_map[genre].sort(key = lambda x: (-x[0], x[1]))    # 재생횟수 기준으로 내림차순, 재생횟수가 같으면 고유번호 오름차순 정렬
        
    sorted_genres = sorted(genre_map.keys(), key=lambda genre: sum(play[0] for play in genre_map[genre]), reverse=True)     # 해당 장르의 모든 노래 재생 횟수를 더한 합계값을 기준으로 장르 이름을 내림 차순으로 정렬
    
    for genre in sorted_genres:     # 그러면 가장 많이 재생된 장르부터 순회하며
        top_two = genre_map[genre][:2]  # 슬라이싱으로 해당 장르에서 이미 정렬된 노래 리스트의 앞 2개만 가져옴
        for play, idx in top_two:
            answer.append(idx)    
    #print(genre_map)
    #print(sorted_genres)
    return answer