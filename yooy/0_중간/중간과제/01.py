array = ['도', '레', '미', '파', '솔']

n = int(input())
result = []


def solution():
    while True:
        for i, x in enumerate(array):
            if x[-1] == '도':
                new_arr = array[i]+'레'
                array.append(new_arr)
            elif x[-1] == '레':
                new_arr = array[i] + '도'
                array.append(new_arr)
                new_arr = array[i] + '미'
                array.append(new_arr)
            elif x[-1] == '미':
                new_arr = array[i] + '레'
                array.append(new_arr)
                new_arr = array[i] + '파'
                array.append(new_arr)
            elif x[-1] == '파':
                new_arr = array[i]+'미'
                array.append(new_arr)
                new_arr = array[i] + '솔'
                array.append(new_arr)
            else:
                new_arr = array[i]+'파'
                array.append(new_arr)
            for k in array:
                if len(k) > n:
                    return array


sol = solution()
for x in sol:
    if len(x) == n:
        result.append(x)
print(result)
print(len(result))