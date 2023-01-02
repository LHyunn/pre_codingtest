def solution(s):
    list = [element.capitalize() for element in s.split(" ")]
    return " ".join(list)
    