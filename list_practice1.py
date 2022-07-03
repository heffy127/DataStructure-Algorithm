def solution(L, x):
    answer = []
    check_add = False
    
    for idx, val in enumerate(L) :
        if x <= val :
            print(x)
            L.insert(idx, x)
            check_add = True
            break
            
    if check_add==False :
        L.append(x)
        
    answer = L
    return answer
