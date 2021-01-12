def solution(s, n):
    answer = ''
    originList = []
    cipherList = []

    from string import ascii_lowercase
    originList = list(ascii_lowercase)

    tmpCnt = 0
    for i in range(0, len(originList)):
        if i+n < len(originList):
            cipherList.append(originList[i+n])
        else:
            cipherList.append(originList[tmpCnt])
            tmpCnt+=1

    for i in range(0, len(s)):
        if s[i]==" ":
            answer += " "
        elif s[i].isupper():
            answer += cipherList[originList.index(s[i].lower())].upper()
        elif s[i].islower():
            answer += cipherList[originList.index(s[i].lower())].lower()


    return answer

print(solution("uxAz bc", 2))
