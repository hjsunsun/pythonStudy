def solution(participant, completion):
    answer = ''
    pName = {}
    cName = {}
    participant.sort()
    
    completion.sort()
    
    for i in range(0,len(participant)):
        pName[i] = participant[i]

    for i in range(0,len(completion)):
        cName[i] = completion[i]

    for i in range(0,len(participant)):
        if pName.get(i)==cName.get(i) :
            continue
        else:
            answer = pName[i];
            break

    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = solution(participant, completion)
print(answer)