# 리스트 L이 오름차순으로 나열되어있으며 중복되는 요소는 없다고 가정할 때 이진탐색 수행
def solution(L, x):
    
    lower = 0
    upper = len(L)-1
    idx = (upper+lower)//2
    
    while lower <= upper:
        if x < L[idx]:
            upper = idx-1
            idx = (upper+lower)//2
        elif x > L[idx]:
            lower = idx + 1
            idx = (upper+lower)//2
        elif x == L[idx]:
            return idx
            break
    return -1
