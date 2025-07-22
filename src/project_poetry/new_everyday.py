nums = [0,0,1,1,1,2,2,3,3,4]
for i in range(len(nums)):
    if i == 0:
        continue
    elif nums.count(nums[i]) > 0:
        print(1)

print(nums)