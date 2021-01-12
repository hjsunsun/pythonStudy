def solution(n):
    answer = 0

    tmpStr = str(n)

    for i in range(0,len(tmpStr)):
        answer += int(tmpStr[i])

    return answer