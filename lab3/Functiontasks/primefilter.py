def filter_prime(nums):
    arr = []
    for i in range(len(nums)):
        for j in range(2,nums[i]):
            if(nums[i]%j==0):
                break
            if(j==nums[i]-1):
                arr.append(nums[i])
    return arr