import operator
def solution(N, stages):

    answer = []

    failStages = {} 
    stage = {} 


    for i in range(0,N):
        cnt = 0
        for j in range(0, len(stages)):
            if i < stages[j]:
                cnt += 1
                failStages[i+1] = cnt
                
    for i in range(0,N):
        stage[i+1] = 0
        if i==N-1:
            try:
                stage[i+1] = failStages[i+1]
            except:
                pass
            break
        
        try:
            stage[i+1] = failStages[i+1]/failStages[i+2]
        except:
            pass

    for i in list(stage.keys()):
        for key, value in stage.items():
            if value == max(stage.values()):
                answer.append(key)
                del stage[key]
                break

    return answer

print(solution(5,[0,6,6,0,0,2,3,0]))