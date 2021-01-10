def solution(s):
    answer = True

    s = s.lower()
    
    if s.count("p") == s.count("y"):
        return True
    else:
        return False

    return True

s = "ooo"
answer = solution(s)
print(answer)