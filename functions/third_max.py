
#Third Maximum Number in a List

class Solution:
    def thirdMax(self, nums):
        max1 = max2 = max3 = None
        for n in nums:
            if n == max1 or n == max2 or n == max3:
                continue
            if max1 is None or n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif max2 is None or n > max2:
                max3 = max2
                max2 = n
            elif max3 is None or n > max3:
                max3 = n
        return max1 if max3 is None else max3


s = Solution()
print(s.thirdMax([3,2,1]))   