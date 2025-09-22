def sol(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[j] < prices[i]:
                break
        answer.append(cnt)
    return answer


def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while len(stack) != 0 and stack[-1][1] > prices[i]:
            p_idx, p_price = stack.pop()
            answer[p_idx] = i-p_idx
        stack.append([i, prices[i]])
    for i in range(len(stack)):
        answer[stack[i][0]] = len(prices) - stack[i][0] -1
    return answer