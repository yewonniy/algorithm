# 연산자만 stack에 넣고 숫자는 다 출력하기
arr = list(input())
stack = []

for i in range(len(arr)):
    if arr[i].isdigit(): # 숫자인 경우 바로 출력
        print(arr[i], end='')
    else: # 연산자인 경우
        if arr[i] == "*" or arr[i] == "/": # 앞이 *, / 일때만 팝
            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                print(stack.pop(), end='')
            # 스택이 비었거나, 앞이 +, -, ( 인 경우 그냥 append
            stack.append(arr[i])
        elif arr[i] == "+" or arr[i] == "-":
            # ( 이 나오기 전까지 다 pop
            while stack:
                if (not stack) or stack[-1] == "(": # stack에 원소가 없거나, stack[-1]이 (이면 멈추기
                    break
                print(stack.pop(), end='')
            stack.append(arr[i])
        elif arr[i] == "(":
            stack.append(arr[i])
        else: # arr[i] == ")"
            while stack:
                if stack[-1] == "(":
                    stack.pop()
                    break
                print(stack.pop(), end='')
while stack:
    print(stack.pop(), end='')



