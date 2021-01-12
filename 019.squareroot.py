import math
def solution(n):
    answer = 0
    squareRoot = math.sqrt(float(n))
    if squareRoot%1==0:
        answer = (squareRoot+1)**2
    else:
        answer = -1
    return answer