def solution(a, b):
    answer = 0

    temp = 0

    if a>b:
        temp = a
        a = b
        b = temp

    for i in range(a,b+1):
        answer += i

    return answer

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

a = 3
b = 5
answer = solution(a,b)
print(answer)

a = 3
b = 5
answer = adder(a,b)
print(answer)