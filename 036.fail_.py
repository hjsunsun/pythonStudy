def solution(N, stages):
    answer = []
    length = len(stages)
   
    # 스테이지 수만큼
    for i in range(1, N+1):

        # 스테이지에 도전중인 사람 수
        count = stages.count(i)
       
        # >if one-liner<
        # if True: fail=0 default 값 따라감
        # if False(else) : else 뒤의 값이 fail에 들어감.
        fail = 0 if length == 0 else (count / length)

        # 스테이지, 실패율 append
        answer.append((i, fail))

        # 스테이지 성공한 사람 수 = 이전 스테이지를 성공한 사람 수 - 스테이지에 도전중인 사람 수 
        length -= count
 
    # lambda answer list의 n번째 값(스테이지N, 실패율)=x
    # x[0]=스테이지, x[1]=실패율
    # x[1]기준으로 sort한다는 뜻
    answer.sort(key = lambda x : x[1], reverse = True)

    # answer에 정렬된 스테이지만 삽입
    answer = [i[0] for i in answer]
   
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))