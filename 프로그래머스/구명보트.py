def solution(people, limit):
    count = 0
    people.sort(reverse=True)
    left, right = 0, len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        left += 1
        count += 1
        
        
    return count