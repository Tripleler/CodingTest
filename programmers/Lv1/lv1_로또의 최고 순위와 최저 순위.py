def solution(lottos, win_nums):
    low = 0
    zeros = 0
    answer = []
    for i in lottos:
        if i in win_nums:
            low += 1
        if i == 0:
            zeros += 1
    if zeros == 6:
        zeros = 5
        low = 1
    if (low == 0) & (zeros == 0):
        low = 1
    answer.append(7 - (low + zeros))
    answer.append(7 - low)
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
