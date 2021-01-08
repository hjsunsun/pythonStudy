def solution(strings, n):
    answer = []
    strings.sort()

    temp = []
    
    for str in strings:
        temp.append(str[n])

    temp.sort()

    for i in temp:
        for str in strings:
            if i == str[n]:
                answer.append(str)
                del strings[strings.index(str)]
                break

    return answer

def strange_sort(strings, n):
    #람다 이용하여 정렬...
    return sorted(strings, key=lambda x: x[n])


strings = ["sun", "bed", "car"]
n = 1
answer = solution(strings, n)
print(answer)

strings2 = ["abce", "abcd", "cdx"]
n2 = 2
answer = solution(strings2, n2)
print(answer)

strings3 =  ["sun", "bed", "car"]
n3 = 2
answer = strange_sort(strings3, n3)
print(answer)

strings4 = ["abce", "abcd", "cdx"]
n4 = 2
answer = strange_sort(strings4, n4)
print(answer)