def solution(progresses, speeds):
    done_count = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        if progresses[0] >= 100:
            count = 0 
            while progresses != [] and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count = count + 1
            done_count.append(count)
            
    return done_count
                