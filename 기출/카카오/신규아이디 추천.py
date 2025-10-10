def trim_spot(arr):
    if len(arr) > 0 and arr[0] == ".":
        arr.pop(0)
    if len(arr) > 0 and arr[-1] == ".":
        arr.pop()


def solution(new_id):
    # 1단계 소문자화
    ans = new_id.lower()
    # 2단계 -_.빼고 없애기
    answer = []
    for i in range(len(list(ans))):
        if (97 <= ord(ans[i]) <= 122) or (ord(ans[i]) == 45 or ord(ans[i]) == 95 or ord(ans[i]) == 46) or ans[
            i].isdigit():
            answer.append(ans[i])

    # 3단계 마침표 2개 이상을 1개로 치환
    stack = []
    for x in answer:
        while x == "." and stack and stack[-1] == ".":
            stack.pop()
        stack.append(x)

    # 4단계
    trim_spot(stack)

    # 5단계
    if len(stack) == 0:
        stack.append("a")

    # 6 단계
    if len(stack) >= 16:
        stack = stack[0:15]
        trim_spot(stack)

    # 7단계
    if len(stack) <= 2:
        for _ in range(3 - len(stack)):
            stack.append(stack[-1])

    return ''.join(stack)