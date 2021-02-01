def solution(d, budget):
    answer = 0

    d.sort()

    tmp = 0
    for i in d:
        tmp += i
        
        if tmp > budget:
            break
        answer+=1
        
        
    return answer

solution(	[1, 3, 2, 5, 4], 9)