def aSolution(n):
    answer = 0

    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    answer = len(primes)
    return answer

def solution(n):
    answer = 0

    for i in range(2,n+1):
        divide = 3
        tempi = i

        if i==2:
            answer+=1
        elif i%2==0:
            continue
        else:
            while tempi!=1:
                if tempi%divide==0:
                    tempi = tempi/divide
                else: 
                    divide+=1
            if divide == i:
                answer+=1

    return answer
    

n = 10
answer = solution(n)
print(answer)
