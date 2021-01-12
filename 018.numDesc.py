def solution(n):
    answer = 0

    tmpList = []
    for i in range(0,len(str(n))):
        tmpList.append(int(str(n)[i]))
    
    tmpList.sort(reverse=True)
    answer = int(''.join(str(e) for e in tmpList))

    return answer