def solution(n):
    
    a = 0
    if n%2==1:
        a = n//2+1
    else:
        a = n//2

    answer = "수박"*a
    if n%2==1:    
        answer = answer[:-1]
        
    return answer

def water_melon(n):
    s = "수박" * n
    return s[:n]

n = 9
answer = water_melon(n)
print(answer)