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

# 후기
"""
아 문제 풀때 split을 깜빡 잊고 있었다. 그리고 sort()같은 메소드를 사용해도 상관없는건지..? 이 문제가 묻고싶은건 정렬 알고리즘이 아니었을까? 아닌가?
정답률 70퍼센트 대 문제인 만큼 쉬웠다. 
"""
