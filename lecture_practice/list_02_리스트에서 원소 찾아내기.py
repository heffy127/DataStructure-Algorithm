# L : 리스트 삽입
# x : 정수 삽입

def solution(L, x):
    answer = []
    
    for idx, val in enumerate(L):
        if x == val:
            answer.append(idx)
    
    if len(answer)==0:
        answer.append(-1)
    
    return answer
