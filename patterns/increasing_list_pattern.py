
#Increasing List right angle triangle Pattern

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in range(1, len(nums) + 1):
    for j in range(i):
        print(nums[j], end=" ")
    print("\n")

