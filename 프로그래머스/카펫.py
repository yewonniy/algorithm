def solution(brown, yellow):
    for n in range(1, 5000):
        for m in range(1, n+1):
            if brown < 2*n + 2*m -4 and yellow < (m-2) * (n-2):
                break
            if brown == 2*n + 2*m -4 and yellow == (m-2) * (n-2):
                answer = [n, m]
                return answer