def solution(n):
    answer = []

    tmpStr = str(n)
    for i in range(0,len(tmpStr)):
        answer.append(int(tmpStr[len(tmpStr)-i-1]))

    return answer