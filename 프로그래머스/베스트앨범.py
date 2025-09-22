from collections import defaultdict
def solution(genres, plays):
    answer = []
    dic = defaultdict(lambda: [0])
    for i in range(len(genres)):
        dic[genres[i]].append([i, plays[i]])
        dic[genres[i]][0] += plays[i]
    d = dict(sorted(dic.items(), key=lambda x: x[1][0], reverse=True))

    for genre in d.keys():
        play = d[genre][1::]
        play.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        for i in range(min(2, len(play))):
            answer.append(play[i][0])
    return answer