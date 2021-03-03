def solution(dartResult):
    answer = 0

    score = []

    tmp = 0
    for i in range(0,len(dartResult)):
        if i==len(dartResult)-1:
            continue;

        if dartResult[i].isdigit():
            if dartResult[i].isdigit() == True and dartResult[i+1].isdigit() == True:
                score.append(dartResult[tmp:i+1])
            else :
                score.append(dartResult[tmp:i])

            tmp = i

    print()

    return answer

solution("1D2S#10S")