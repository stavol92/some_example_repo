def foo(nums):
    current = 0
    best = 0
    for n in  nums:
        if n > 0:
            current += 1
            best = max(current, best)
        else:
            current = 0
    return best