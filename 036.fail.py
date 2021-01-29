import operator
def solution(N, stages):

    answer = []

    failStages = {} 
    stage = {} 

   

    for i in range(0,N+1):
        cnt = 0
        for j in range(0, len(stages)):

            if i < stages[j]:
                cnt += 1
                
        failStages[i+1] = cnt
        

    for i in range(0,N):
        if failStages[i+1]>1 and failStages[i+2]==0:
            stage[i+1] = 100
        else:
            try:
                stage[i+1] = failStages[i+1]/failStages[i+2]
            except:
                stage[i+1] = 0
                pass
                
    
    answer = list(stage.items())
    answer.sort(key = lambda x : (x[1]), reverse=True)

    answer = [a for a,b in answer]

    
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
# [1,2,2,1,3]
# result :  [3,2,1,4,5]