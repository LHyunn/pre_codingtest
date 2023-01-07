
def solution(n):
    answer = ''
    while n:
        if n%3 == 1:
            answer+='1'
            n = n // 3
        elif n%3 == 2:
            answer+='2'
            n = n // 3
        elif n%3 == 0:
            answer+='4'
            n = n // 3 - 1

    list1 = list(answer)
    list1.reverse()
    return ''.join(list1)