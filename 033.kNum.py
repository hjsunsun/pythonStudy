def solution(array, commands):
    answer = []

    for l in range(0,len(commands)):

        tempList = []

        i = int(commands[l][0])
        j = int(commands[l][1])
        k = int(commands[l][2])

        tempList = array[i-1:j]

        tempList.sort()

        answer.append(tempList[k-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution(array, commands)
print(answer)