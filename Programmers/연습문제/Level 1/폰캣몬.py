def solution(nums):
    result = len(nums) // 2
    
    if result >= len(set(nums)):
        return len(set(nums))
    else:
        return result