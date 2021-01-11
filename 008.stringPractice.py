def solution(s):
    answer = False
    s.strip()
    if len(s) == 4 or len(s) == 6:
        answer=True
        try:
            type(int(s))==int
        except ValueError:
            answer=False
    return answer

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

s = "123a"
answer = solution(s)
print(answer)

s = "123a"
answer = alpha_string46(s)
print(answer)