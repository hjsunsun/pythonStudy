def solution(n, m):
    answer = []

    nList = []
    mList = []

    if(n>m):
        temp = n
        n = m
        m = temp

    for i in range(1,n+1):
        if(n%i==0):
            nList.append(i)

    for i in range(1,m+1):
        if(m%i==0):
            mList.append(i)

    for i in range(0,len(mList)):
        for j in range(0,len(nList)):
            if mList[i]==nList[j]:
                answer.append(mList[i])
                break
    
    answer = answer[-1:]

    answer.append(n*m/answer[0])

    return answer

answer = solution(3,12)
print(answer)