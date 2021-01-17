
def solution(answers):
    answer = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    stAnswer = [0,0,0]

    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(0,len(answers)):
        if student1[i%5]==answers[i] :
            stAnswer[0]+=1

        if student2[i%8]==answers[i]:
            stAnswer[1]+=1

        if student3[i%10]==answers[i]:
            stAnswer[2]+=1

    if max(stAnswer) > 0:
        for i in range(0,3):
            if stAnswer[i] == max(stAnswer):
                answer.append(i+1)
        
    return answer

answers = [6,7,8,9,4,5]
answer = solution(answers)
print(answer)
