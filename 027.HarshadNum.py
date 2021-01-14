def solution(x):
    answer = True

    tmpStr = str(x)
    Harshad = 0
    for i in range(len(tmpStr)):
        Harshad += int(tmpStr[i])

    if x%Harshad!=0:
        answer = False

    return answer