def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1]:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    answer = answer + 2 
                    del bucket[-2:]
                break
    return answer