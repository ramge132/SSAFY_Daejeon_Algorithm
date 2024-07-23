# https://school.programmers.co.kr/learn/courses/30/lessons/176963

# 사진 속 인물들의 그리움 점수를 합산하여 각 사진의 추억 점수를 구하는 문제.
# 분류: 구현
# 시간복잡도: O(n + m * k) / n은 name 배열의 길이, m은 photo 배열의 길이, k는 각 사진 속 인물의 평균 길이.

def solution(name, yearning, photo):
    # 이름을 키, 그리움 점수를 값으로 하는 딕셔너리 생성
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    
    result = []
    for p in photo:
        # 각 사진 속 인물들의 그리움 점수를 합산
        score = sum(yearning_dict.get(person, 0) for person in p)
        result.append(score)
    
    return result
