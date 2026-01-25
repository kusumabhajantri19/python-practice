

#pattern

nums =[1,2,3,4,5]
for i in range(len(nums)):
    for j in range(5-i):
        print(nums[j], end = " ")
    print("\n")