def solution(s):
    string_length = len(s)
    answer_list = []
    for i in range(1, int(string_length/2)+2, 1):
        if string_length % i == 0:
            cut_num = string_length // i
        else:
            cut_num = string_length // i + 1

            
        tmp_list = []
        for j in range(cut_num):
            tmp_list.append(s[j*i:(j+1)*i])
        
        
        answer_length = []
        for i in range(len(tmp_list)):
            if i == 0:
                answer_length.append(1)
                answer_length.append(tmp_list[i])

            if i > 0:
                if tmp_list[i] == tmp_list[i-1]:
                    answer_length[-2] += 1
                else:
                    answer_length.append(1)
                    answer_length.append(tmp_list[i])

        while 1 in answer_length:
            answer_length.remove(1)

        answer_list.append(len(''.join(map(str, answer_length))))
    return min(answer_list)


        