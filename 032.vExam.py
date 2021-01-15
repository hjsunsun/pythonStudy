
def solution(answers):
    answer = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    stAnswer = [0,0,0]

    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(0,len(answers)):
        if cnt1 == 4:
            cnt1 = 0
        elif cnt2 == 7:
            cnt2 = 0
        elif cnt3 == 9:
            cnt3 = 0

        student1.append(student1[cnt1])
        student2.append(student2[cnt2])
        student3.append(student3[cnt3])

        cnt1 += 1
        cnt2 += 1
        cnt3 += 1

        if student1[i]==answers[i] :
            stAnswer[0]+=1

        if student2[i]==answers[i]:
            stAnswer[1]+=1

        if student3[i]==answers[i]:
            stAnswer[2]+=1

    for i in range(0,3):
        if stAnswer[i] == max(stAnswer):
            answer.append(i+1)
        
    answer.sort()
    return answer

answers = [1,3,2,4,2]
answer = solution(answers)
print(answer)
