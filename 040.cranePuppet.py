def solution(board, moves):
    answer = 0
    basket = []

    for i in range(0,len(moves)):
        cnt = 0
        for j in range(len(board)):
            if board[cnt][moves[i]-1] == 0:
                cnt+=1
            else:
                basket.append(board[cnt][moves[i]-1])
                board[cnt][moves[i]-1] = 0
                break
                

        if len(basket)>1 and basket[-1] == basket[-2]:
            del basket[-1]
            del basket[-1]
            answer+=2


    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))