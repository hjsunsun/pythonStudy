
def solution(arr):
    answer = []
    temp = arr[0] + 1
    
    for ii in arr:
        if ii != temp:
            answer.append(ii)
        temp = ii

    return answer

arr = [1,5,5,6,6,6,8,9,9,9,10]
answer = solution(arr)
print(answer)