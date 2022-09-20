def solution(triangle):
    if len(triangle) == 1 : return triangle[0]
    else : 
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

    for i in range(2, len(triangle)) :
        for j in range(1, len(triangle[i]) - 1) :
            if triangle[i - 1][j] > triangle[i - 1][j - 1] :
                triangle[i][j] += triangle[i - 1][j]
            else :
                triangle[i][j] += triangle[i - 1][j - 1]

        triangle[i][0] += triangle[i - 1][0] 
        triangle[i][len(triangle[i]) - 1] += triangle[i - 1][len(triangle[i - 1]) - 1]

    return max(triangle[len(triangle) -  1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)