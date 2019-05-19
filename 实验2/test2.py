nums = input()
nums = sorted(list(map(int,list(nums))),reverse = 1)
print(nums[0],sum(nums))