def sum67(nums):
    total = 0
    i = 0
    
    while i < len(nums):
        if nums[i] == 6:
            i += 1
            while nums[i] != 7:
                i += 1
            i += 1  # пропускаем 7
        else:
            total += nums[i]
            i += 1
    
    return total