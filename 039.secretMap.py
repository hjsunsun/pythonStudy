def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []

    for i in range(0,n):
        map1.append(format(arr1[i],'b').zfill(n))
        map2.append(format(arr2[i],'b').zfill(n))

    for i in range(0,n):
        tmp = ""
        for j in range(0,n):
            if map1[i][j] == "1" or map2[i][j] == "1":
                tmp += "#"
            elif map1[i][j] == "0" and map2[i][j] == "0":
                tmp += " "
        
        answer.append(tmp)

    return answer

solution(5,[9, 20, 28, 18, 11],	[30, 1, 21, 17, 28])