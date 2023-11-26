def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = int(nums[mid])
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return mid



