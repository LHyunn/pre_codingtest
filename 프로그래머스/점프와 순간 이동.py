def solution(n):
    return(len(str(bin(n)).replace("0","").replace("b","")))