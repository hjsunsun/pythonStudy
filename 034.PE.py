def solution(n, lost, reserve):
    answer = 0
    tmpCnt = len(lost)

    dualStudents = list(set(lost) & set(reserve))
    for i in range(0,len(dualStudents)):
        del lost[lost.index(dualStudents[i])]
        del reserve[reserve.index(dualStudents[i])]
        tmpCnt-=1

    for i in range(0,len(lost)):
        if reserve.count(lost[i]+1)>0:
            del reserve[reserve.index(lost[i]+1)]
            tmpCnt-=1
        elif reserve.count(lost[i]-1)>0:
            del reserve[reserve.index(lost[i]-1)]
            tmpCnt-=1

    answer = n - tmpCnt

    return answer

print(solution(5,[2, 4,3]	,[9,3]))