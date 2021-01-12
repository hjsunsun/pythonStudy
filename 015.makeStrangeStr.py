def solution(s):
    answer = ''

    wordList = s.split(" ")

    for i in range(0, len(wordList)):
        tmpStr = wordList[i]
        for j in range(0,len(tmpStr)):
            if j==0 or j%2==0:
                answer+=tmpStr[j].upper()
            else:
                answer+=tmpStr[j].lower() 
        answer += " "

    answer = answer[:-1]
                
        
    return answer