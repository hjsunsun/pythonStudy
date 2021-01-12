def solution(arr):
    answer = []

    if len(arr)==1:
        answer.append(-1)
        
    else:
        # deleteNum = arr[0]
        # for i in range(0,len(arr)):
        #     if deleteNum > arr[i]:
        #         deleteNum = arr[i]
                
        deleteNum = min(arr)
        for i in range(0, arr.count(deleteNum)):
            del arr[arr.index(deleteNum)]

        answer = arr

    return answer

#5,7,3,2,6
arguArr = [1,5,7,3,2,6]
arr = solution(arguArr)
print(arr)