import operator
def solution(N, stages):
    answer = []

    failStages = {}

    for i in range(0,N):
        if stages.count(i+1)==0:
            failStages[i+1] = 0

        for j in range(0,stages.count(i+1)):
            failStages[i+1] = j+1

    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))