def solution(s):
    answer = ''
    temp = list(s)

    temp.sort(reverse=True)

    answer = ''.join(temp)

    return answer

s = "Zbcdefg"
answer = solution(s)
print(answer)