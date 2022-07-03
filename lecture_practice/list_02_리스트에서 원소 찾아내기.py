def solution(L, x):
    answer = []
    
    for idx, val in enumerate(L):
        if x == val:
            answer.append(idx)
    
    if len(answer)==0:
        answer.append(-1)
    
    return answer
