
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)

    answer.sort()

    return answer

def solution2(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

arr = [5,6,10,15,17,20,30]
divisor = 5
answer = solution(arr,divisor)
print(answer)

arr = [6,8,9,14,16,17]
answer = solution(arr,divisor)
print(answer)