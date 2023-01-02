def solution(s):
    list = []
    num = ''
    for i in s:
        if i != ' ':
            num = num+i
        if i == ' ':
            list.append(int(num))
            num = ''
    list.append(int(num))
    list.sort()
    answer = '{} {}'.format(list[0], list[len(list)-1])
    return answer
